#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 tw=90:
import unittest
import os

from mfconnect import meteo


@unittest.skip('need a running terminal')
class TestUsertermsize(unittest.TestCase):
    def setUp(self):
        self.a = meteo.user_term_size()

    def test_class(self):
        self.assertIsInstance(self.a, tuple)

    def test_len(self):
        self.assertTrue(len(self.a) == 4)

    def test_type(self):
        for x in self.a:
            self.assertIsInstance(x, int)


if __name__ == '__main__':
    unittest.main()
