# -*- coding: utf-8 -*-
"""
	**test_inf.py**
	unit tests for *src/err.py*

	in the module:
	* *class* **TestErr**

	Copyright 2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl
"""
# pylint: disable=relative-import, missing-docstring
import unittest
from StringIO import StringIO
import phoebe.err
import mock
from answers import ERR_ANS


class TesErr(unittest.TestCase):
	""" class for testing *Generator* """
	def setUp(self):
		self.err = phoebe.err.Err()

	def tearDown(self):
		pass

	def test_value_to_name(self):
		self.assertEqual(self.err.value_to_name(self.err.ERR_IO), 'ERR_IO')
		with self.assertRaises(ValueError):
			self.err.value_to_name(33)

	def test_get_err_description(self):
		self.assertEqual(self.err.get_err_description(self.err.ERR_IO), 'ERR_IO')

	def test_self_test(self):
		with mock.patch('sys.stdout', new=StringIO()) as fake_stdout:
			phoebe.err.self_test()
			self.assertEqual(fake_stdout.getvalue(), ERR_ANS)


def main():
	unittest.main()


if __name__ == '__main__':
	main()

# end.
