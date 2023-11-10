#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 tw=90:

import sys
import os
import argparse
import struct
import fcntl
import termios
import signal
import warnings
from datetime import datetime
from stat import S_IRGRP, S_IWGRP, S_IXGRP, S_IROTH, S_IWOTH, S_IXOTH, S_IRWXG, S_IRWXO
from urllib.parse import quote_plus
import shutil
import pexpect
import namedtupled
from yaml import safe_load, dump, YAMLLoadWarning
import subprocess
from mfconnect.version import __version__ as version

warnings.simplefilter(action='ignore', category=YAMLLoadWarning)

# configuration file
config_file = os.path.join(os.environ['HOME'], '.meteorc')

hostname_re = '(?i)>> host name:.*'
login_prompt_re = ['(?i)user:.*', '(?i)login:.*', '(?i).*username.*']
login_prompt_re.insert(0, hostname_re)

# Global variables for the unique virtual term
vterm = None
use_x11 = None


def end(pterm):
    """
       Close the connection as well as possible
       This makes sure the child is dead
       although it would be killed when Python exits.
    """
    if pterm.isalive():
        pterm.sendline('exit')
        pterm.close()


def begin(phost, cfg):
    """
        Begin the connection with a spawn to server host.
    """

    telnet_cmd = shutil.which('telnet')
    if not telnet_cmd:
        print(f'telnet command not found: please contact your system administrator')
        sys.exit(1)

    try:
        concat = ''.join([telnet_cmd, ' ', phost])
        pterm = pexpect.spawn(concat, timeout=cfg.timeout)
        pterm.delaybeforesend = cfg.delaybeforesend
        if cfg.debug:
            logfile = os.path.join(os.environ['HOME'], '.meteo.log')
            print(f"Warning: you have activated debug, remove {logfile} after your debug session")
            pterm.logfile = open(logfile, 'wb')

    except pexpect.TIMEOUT as e:
        end(pterm)
        raise e("Cannot begin session: {e}")

    except pexpect.EOF as e:
        end(pterm)
        raise e

    return pterm


def login(user, password, pterm):
    """Log the user with is password."""
    try:
        index = pterm.expect(login_prompt_re, timeout=50)
        if index == 0:
            raise pexpect.EOF("can't find a valid login banner")
        pterm.sendline(user)
        pterm.expect(['(?i)password:.*', '(?i).*password.*'])
        pterm.sendline(password)

    except pexpect.TIMEOUT as e:
        end(pterm)
        raise e(f"can't login as {user}: {e}")

    except pexpect.EOF as e:
        end(pterm)
        raise e


def interact_output_filter(data):
    """
        used to detect end of session, when we are back to MOI telnet proxy.
    """
    try:
        if '>> Host name:' in data.decode('utf-8'):
            sys.exit(0)
    except UnicodeDecodeError:
        pass

    return data


def interact(pterm):
    """Prepare  pterm for user interaction."""
    sys.stdout.flush()

    """ Try Interact now
        until the escape caracter or exit command (exception),
        script is now blocked here:
    """
    try:
        pterm.interact(output_filter=interact_output_filter)

    except pexpect.TIMEOUT as e:
        end(pterm)
        raise e(f"something went wrong: {e}")
    except pexpect.EOF as e:
        end(pterm)
        raise e


def do_input(ask):
    try:
        v = input(ask)
    except (EOFError, KeyboardInterrupt):
        sys.exit(0)
    return v


def user_password(cfg, entry):
    from getpass import getpass
    print(f"Configuration of section {entry}:")

    new_host = False
    try:
        cur_host = cfg[entry]['hostname']
        update_host = do_input(f"current host for section {entry} is {cur_host}. Is this ok ? (Y/N): ")
        if update_host in ['n', 'N']:
            new_host = do_input("Hostname: ")
    except KeyError:
        pass

    username = do_input("Username: ")

    password = 1
    password_verif = 2
    try:
        while password != password_verif:
            password = getpass()
            password_verif = getpass("Verification: ")
    except (EOFError, KeyboardInterrupt):
        sys.exit(0)

    # set config
    cfg[entry]['username'] = username
    cfg[entry]['password'] = password
    if new_host:
        cfg[entry]['hostname'] = new_host


def load_config():
    """
       return config as a dict
    """
    with open(config_file, 'r') as cfgs:
        cfg = safe_load(cfgs.read())
    return cfg


def save_config(new_cfg):
    """
        dump dict to config file
    """
    with open(config_file, 'w') as cfgs:
        dump(new_cfg, cfgs, explicit_start=True)


def interactive_configuration():
    v = do_input("Do you want to configure mfconnect ? (Y/N): ")
    if v != 'y' and v != 'Y':
        print(f"You will have to create the ~/{config_file} yourself")
        sys.exit(0)

    cfg = load_config()

    for e in ['proxymo', 'proxymf', 'ldapmf']:
        user_password(cfg, e)

    save_config(cfg)


def create_new_cfg():
    from site import getsitepackages
    from shutil import copyfile
    tmpl = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'meteorc')
    copyfile(tmpl, config_file)
    mode = os.stat(config_file).st_mode
    mode -= (mode & (S_IRWXG | S_IRWXO))
    os.chmod(config_file, mode)
    interactive_configuration()


def update_cfg(section=None, opts=None, delete=False):
    cfg = load_config()

    if section == 'hosts':
        if delete:
            to_del = []
            for idx, h in enumerate(cfg['hosts']):
                if h['hostname'] == opts[0]:
                    to_del.append(idx)
            del(cfg['hosts'][to_del[0]])
        else:
            cfg['hosts'].append({
                'hostname': opts[0],
                'alias': opts[1],
            })
    else:
        cfg[section]['username'] = opts[0]
        cfg[section]['password'] = opts[1]

    save_config(cfg)

    sys.exit(0)


def load_db():
    """
        sanity check, then return cfg as a namedtupled which is immutable
    """
    try:
        mode = os.stat(config_file).st_mode
        if mode & (S_IRGRP | S_IWGRP | S_IXGRP | S_IROTH | S_IWOTH | S_IXOTH):
            print(f'your configuration file {config_file} is not protected: please use chmod 600 {config_file}')
            sys.exit(1)
    except FileNotFoundError:
        create_new_cfg()

    return namedtupled.yaml(path=config_file)


def sigwinch_passthrough(sig, data):
    """ Catch signals for re-sizing the virtual term. """
    size = user_term_size()
    vterm.setwinsize(size[0], size[1])


def user_term_size():
    """ Get the current user terminal size. """
    s = struct.pack("HHHH", 0, 0, 0, 0)
    a = struct.unpack('hhhh', fcntl.ioctl(sys.stdout.fileno(), termios.TIOCGWINSZ, s))
    return a


def do_command(cfg=None, host=None, cmd=[]):
    global vterm
    try:
        vterm = begin(cfg.proxymo.hostname, cfg.parameters)
        vterm.expect([hostname_re])
        vterm.sendline(host.hostname)
        login(cfg.proxymf.username, cfg.proxymf.password, vterm)
        login(cfg.ldapmf.username, cfg.ldapmf.password, vterm)
        vterm.expect([cfg.ldapmf.username + '.*', 'hendrix>.*'])
        vterm.sendline(cmd[1])
        rv = vterm.readline()  # consume cmd
        while True:
            try:
                rv = vterm.readline()
                print(rv.decode('utf-8').strip('\n'))
            except(Exception):
                break
        vterm.sendline('logout')
    except(Exception):
        end(vterm)
        return False
    return True


def new_bookmark_line(cfg=None, host=None):
    bm_name = host.alias
    bm_user = quote_plus(f"{cfg.ldapmf.username}@{cfg.proxymf.username}@{host.hostname}")
    bm_pass = quote_plus(f"{cfg.ldapmf.password}@{cfg.proxymf.password}")
    bm_host = host.hostname
    return f"{bm_name} ftp://{bm_user}:{bm_pass}@{bm_host}\n"


def add_host_to_bookmarks(cfg=None, host=None):
    bookmarks = None
    bfile = os.path.join(os.environ['HOME'], '.lftp/bookmarks')
    with open(bfile, 'r') as bkm:
        bookmarks = bkm.readlines()

    with open(bfile, 'w+') as bkm:
        missing = True
        for i, l in enumerate(bookmarks):
            ba, bv = l.split()
            if ba == host.alias or ba == host.hostname:
                bookmarks[i] = new_bookmark_line(cfg, host)
                missing = False
            bkm.write(bookmarks[i])
        if missing:
            bkm.write(new_bookmark_line(cfg, host))


def exec_lftp(host=None, cmd=None):
    lftp_cmd = shutil('lftp')
    if not lftp_cmd:
        print('lftp command not found: please contact your system administrator')
        sys.exit(1)

    args = [lftp_cmd, ]
    if cmd:
        args.append("-c")
        args.append(f"open {host}; {cmd};")
    else:
        args.append(host)
    subprocess.run(args, shell=False)


def do_ftp(cfg=None, host=None, cmd=[]):
    add_host_to_bookmarks(cfg, host)
    mycmd = None
    try:
        mycmd = ' '.join(cmd[1:])
    except Exception:
        pass
    exec_lftp(host.alias, mycmd)
    sys.exit(0)


def try_connect(cfg=None, host=None, cmd=[], opts=None):
    """ connect to proxymo and manage X11 if needed,
        then connect to proxymf.

        if everything is ok, then call do_connect
    """
    x11display = None
    global vterm

    if opts.ftp:
        return do_ftp(cfg, host, cmd)

    if len(cmd) > 1:
        return do_command(cfg, host, cmd)

    try:
        if use_x11:
            os.system('xhost + > /dev/null 2>&1')

        vterm = begin(cfg.proxymo.hostname, cfg.parameters)
        vterm.expect([hostname_re])

        if use_x11:
            vterm.sendline(use_x11)
            vterm.expect([hostname_re])

        vterm.sendline(host.hostname)

        if use_x11:
            vterm.expect(['DISPLAY.*\n'])
            x11display = vterm.after.split()

        login(cfg.proxymf.username, cfg.proxymf.password, vterm)

    except pexpect.TIMEOUT:
        print(f'Timeout: No response from {cfg.proxymo.hostname}, can\'t connect to {host}')
        end(vterm)
        return False

    except (pexpect.EOF, OSError):
        end(vterm)
        return False

    return do_connect(cfg, x11display, host)


def do_connect(cfg, x11display, host):
    """ Connect on final host,
        export DISPLAY and LANG
        set winwdow size to the current window size (yes that's strange)
        and bypass SIGWINCH:    28,28,20    Ign     Window resize signal (4.3BSD, Sun)
        run the interaction.
    """
    try:
        login(cfg.ldapmf.username, cfg.ldapmf.password, vterm)
    except (pexpect.TIMEOUT, pexpect.EOF):
        if cfg.parameters.debug:
            print(f"can't login as {cfg.ldapmf.username}@{host.hostname}")
        end(vterm)
        return False

    try:
        vterm.expect([cfg.ldapmf.username + '.*', 'hendrix>.*'])
        if host.hostname != 'hendrix.meteo.fr':
            vterm.sendline("export LANG='en_US.UTF-8'")
    except pexpect.TIMEOUT:
        end(vterm)
        return False

    if use_x11:
        vterm.sendline(''.join(['export ', x11display[0].decode('utf-8'), '=', x11display[1].decode('utf-8')]))

    signal.signal(signal.SIGWINCH, sigwinch_passthrough)
    current_size = user_term_size()
    vterm.setwinsize(*current_size[0:2])

    interact(vterm)


def getopts(test_args=None, epilog=""):
    """ Parsing arguments and options """
    metavar_user = ('<username>', '<password>')
    parser = argparse.ArgumentParser(prog='meteo', allow_abbrev=True, epilog=epilog)
    parser.add_argument('host', nargs='*', type=str, metavar='HOST',
                        help='hostname to connect to')
    parser.add_argument('-d', '--debug', action='store_true',
                        help='display connection attempts, store full chat to ~/.meteo.log')
    parser.add_argument('-v', '--version', action='store_true',
                        help='show version number and exit')
    parser.add_argument('-x', '--x11', action='store_true',
                        help='use X11 protocol over telnet')
    parser.add_argument('-f', '--ftp', action='store_true',
                        help='use LFTP instead of telnet')
    parser.add_argument('--proxymo', nargs=2, required=False, metavar=metavar_user,
                        help='set the Mercator Ocean proxy username and password')
    parser.add_argument('--proxymf', nargs=2, required=False, metavar=metavar_user,
                        help='set the Meteo France proxy username and password')
    parser.add_argument('--ldapmf', nargs=2, required=False, metavar=metavar_user,
                        help='set the Meteo France ldap username and password')
    parser.add_argument('--add-host', nargs=2, required=False, metavar=('<hostname>', '<alias>'),
                        help='add the Meteo France hostname and alias to your host list')
    parser.add_argument('--del-host', nargs=1, required=False, metavar=('<hostname>'),
                        help='remove the Meteo France hostname from your host list')

    opts = parser.parse_args(test_args)

    if opts.version:
        print(f"meteo version {version}")
        sys.exit(0)

    if opts.x11:
        """ In order to have X11, we need to send x HOSTNAME:X.Y
            where HOSTNAME:X.Y is the actual display, to the proxymo service.
            see try_connect for the details.
        """
        ldisplay = str(os.getenv('DISPLAY'))
        host, dis = ldisplay.split(':')
        global use_x11
        use_x11 = "x " + str(os.getenv('HOSTNAME')) + ':' + dis

    if opts.proxymo:
        update_cfg('proxymo', opts.proxymo)
    if opts.proxymf:
        update_cfg('proxymf', opts.proxymf)
    if opts.ldapmf:
        update_cfg('ldapmf', opts.ldapmf)
    if opts.add_host:
        update_cfg('hosts', opts.add_host)
    if opts.del_host:
        update_cfg('hosts', opts.del_host, delete=True)

    if not isinstance(opts.host, list) or len(opts.host) == 0:
        parser.print_help()
        parser.exit()

    return opts


def meteo():
    """ Initialization """
    db = load_db()

    if not (db.proxymf.username and db.proxymf.password):
        print('Please fill ~/.meteorc with your meteo ids')
        sys.exit(1)

    opts = getopts()

    if opts.debug:
        dbr = namedtupled.reduce(db)
        dbr['parameters']['debug'] = opts.debug
        db = namedtupled.map(dbr)

    """ check and setup the target machine """
    host = None
    for h in db.hosts:
        if h.hostname == opts.host[0] or h.alias == opts.host[0]:
            host = h
            break

    if not host:
        print(f"Unknown host: {opts.host[0]}")
        sys.exit(1)

    """ Try to connect """
    ok = False
    mtries = 20
    ctry = 0
    while not ok and ctry <= mtries:
        if opts.debug:
            print(f"{datetime.now()}: try #{ctry}/{mtries}")
        try:
            ok = try_connect(db, host, opts.host, opts)
        except KeyboardInterrupt:
            sys.exit(0)
        ctry += 1


if __name__ == '__main__':
    meteo()
