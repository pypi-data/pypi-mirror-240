#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 tw=90:
import unittest

import namedtupled
import warnings
from yaml import YAMLLoadWarning

from mfconnect import meteo


class TestLoaddb(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter(action='ignore', category=YAMLLoadWarning)
        self.a = meteo.load_db()

    def test_class(self):
        self.assertTrue(namedtupled.namedtupled.isnamedtupleinstance(self.a))

    def test_proxymo(self):
        self.assertTrue(hasattr(self.a, 'proxymo'))

    def test_proxymo_username(self):
        self.assertTrue(hasattr(self.a.proxymo, 'username'))

    def test_proxymo_password(self):
        self.assertTrue(hasattr(self.a.proxymo, 'password'))

    def test_proxymf(self):
        self.assertTrue(hasattr(self.a.proxymf, 'password'))

    def test_proxymf_username(self):
        self.assertTrue(hasattr(self.a.proxymf, 'username'))

    def test_proxymf_password(self):
        self.assertTrue(hasattr(self.a.proxymf, 'password'))

    def test_ldapmf(self):
        self.assertTrue(hasattr(self.a.ldapmf, 'password'))

    def test_ldapmf_username(self):
        self.assertTrue(hasattr(self.a.ldapmf, 'username'))

    def test_ldapmf_password(self):
        self.assertTrue(hasattr(self.a.ldapmf, 'password'))

    def test_hosts(self):
        self.assertTrue(hasattr(self.a, 'hosts'))

    def test_hosts_list(self):
        self.assertTrue(isinstance(self.a.hosts, list))

    def test_host_hendrix(self):
        for h in self.a.hosts:
            if h.hostname == 'hendrix.meteo.fr':
                self.assertTrue(h.alias == 'hendrix')
                return

        self.fail('cannot find host hendrix')


if __name__ == '__main__':
    unittest.main()
