#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 tw=90:
import unittest
from unittest import mock

from mfconnect import meteo


class TestDoinput(unittest.TestCase):

    @mock.patch('mfconnect.meteo.do_input', create=True)
    def test_do_input(self, mocked_input):
        return_cases = ['toto', 'tutu', 'machin', '0$.!']
        mocked_input.side_effect = return_cases
        for i in return_cases:
            rv = meteo.do_input(i)
            self.assertEqual(rv, i)


if __name__ == '__main__':
    unittest.main()
