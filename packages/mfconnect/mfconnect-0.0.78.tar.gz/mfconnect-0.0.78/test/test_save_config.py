#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 tw=90:
import unittest

from mfconnect import meteo


class TestSaveconfig(unittest.TestCase):
    def setUp(self):
        self.a = meteo.load_config()

        self.b = self.a
        self.b['ldapmf']['username'] = 42

    @unittest.skip("there is a problem here")
    def test_diff(self):
        self.assertNotEqual(self.a, self.b)

    def test_mod(self):
        self.assertEqual(self.b['ldapmf']['username'], 42)


if __name__ == '__main__':
    unittest.main()
