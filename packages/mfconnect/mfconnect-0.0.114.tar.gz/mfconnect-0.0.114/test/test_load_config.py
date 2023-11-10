#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 tw=90:
import unittest
from mfconnect import meteo


class TestSaveconfig(unittest.TestCase):
    def setUp(self):
        self.a = meteo.load_config()

    def test_class(self):
        self.assertIsInstance(self.a, dict)

    def test_proxymo(self):
        self.assertIn('proxymo', self.a.keys())

    def test_proxymo_username(self):
        self.assertIn('username', self.a['proxymo'].keys())

    def test_proxymo_password(self):
        self.assertIn('password', self.a['proxymo'].keys())

    def test_proxymf(self):
        self.assertIn('proxymf', self.a.keys())

    def test_proxymf_username(self):
        self.assertIn('username', self.a['proxymf'].keys())

    def test_proxymf_password(self):
        self.assertIn('password', self.a['proxymf'].keys())

    def test_ldapmf(self):
        self.assertIn('ldapmf', self.a.keys())

    def test_ldapmf_username(self):
        self.assertIn('username', self.a['ldapmf'].keys())

    def test_ldapmf_password(self):
        self.assertIn('password', self.a['ldapmf'].keys())

    def test_hosts(self):
        self.assertIn('hosts', self.a.keys())

    def test_hosts_list(self):
        self.assertIsInstance(self.a['hosts'], list)


if __name__ == '__main__':
    unittest.main()
