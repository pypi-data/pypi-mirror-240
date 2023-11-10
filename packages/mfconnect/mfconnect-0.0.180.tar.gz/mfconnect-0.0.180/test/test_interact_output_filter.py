#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 tw=90:
import unittest

from mfconnect import meteo


class TestInteractoutputfilter(unittest.TestCase):
    def test_interact_output_filter_std(self):
        data = bytes('abcdef', encoding='utf-8')
        a = meteo.interact_output_filter(data)
        self.assertTrue(a is data)

    def test_interact_output_filter_exit(self):
        with self.assertRaises(SystemExit) as cm:
            data = bytes('abcdef >> Host name: ', encoding='utf-8')
            meteo.interact_output_filter(data)
            self.assertEqual(cm.exception_code, 0)


if __name__ == '__main__':
    unittest.main()
