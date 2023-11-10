#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 tw=90:
import unittest
import os
import argparse
from mfconnect import meteo


class Testgetopts(unittest.TestCase):
    hendrix = 'hendrix.meteo.fr'
    name = 'ocean.mercator-ocean.fr'
    alias = 'o'
    user = 'gontrand'
    upass = '01234'
    os.environ['DISPLAY'] = ':0.0'

    def setUp(self):
        self.db = meteo.load_db()

    def test_getopts_simple(self):
        popts = meteo.getopts(test_args=[self.hendrix])
        self.assertIsInstance(popts, argparse.Namespace)
        self.assertIn('host', popts)
        self.assertIs(popts.host[0], self.hendrix)

    def test_getopts_x11(self):
        popts = meteo.getopts(test_args=['-x', self.hendrix])
        self.assertIsInstance(popts, argparse.Namespace)
        self.assertIn('x11', popts)
        self.assertTrue(popts.x11)

    def test_getopts_add_host(self):
        with self.assertRaises(SystemExit) as cm:
            popts = meteo.getopts(test_args=['--add-host', self.name, self.alias])
            self.assertEqual(cm.exception_code, 0)
            self.assertIsInstance(popts, argparse.Namespace)

    def test_getopts_del_host(self):
        with self.assertRaises(SystemExit) as cm:
            popts = meteo.getopts(test_args=['--del-host', self.name])
            self.assertEqual(cm.exception_code, 0)
            self.assertIsInstance(popts, argparse.Namespace)

    def test_getopts_proxymo(self):
        with self.assertRaises(SystemExit) as cm:
            popts = meteo.getopts(test_args=['--proxymo', self.user, self.upass])
            self.assertEqual(cm.exception_code, 0)
            self.assertIsInstance(popts, argparse.Namespace)

    def test_getopts_proxymf(self):
        with self.assertRaises(SystemExit) as cm:
            popts = meteo.getopts(test_args=['--proxymf', self.user, self.upass])
            self.assertEqual(cm.exception_code, 0)
            self.assertIsInstance(popts, argparse.Namespace)

    def test_getopts_ldapmf(self):
        with self.assertRaises(SystemExit) as cm:
            popts = meteo.getopts(test_args=['--ldapmf', self.user, self.upass])
            self.assertEqual(cm.exception_code, 0)
            self.assertIsInstance(popts, argparse.Namespace)


if __name__ == '__main__':
    unittest.main()
