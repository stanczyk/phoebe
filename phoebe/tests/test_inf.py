# -*- coding: utf-8 -*-
"""
	**test_inf.py**
	unit tests for *src/inf.py*

	in the module:
	* *class* **TestInf**

	Copyright 2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl
"""
# pylint: disable=relative-import, missing-docstring
import unittest
from StringIO import StringIO
import phoebe.inf
import mock
from answers import INF_ANS, INF_VER


class TestInf(unittest.TestCase):
	""" class for testing *Inf* """
	def setUp(self):
		self.inf = phoebe.inf.Inf()

	def tearDown(self):
		pass

	def test_get_version(self):
		self.assertEqual(self.inf.get_version(), INF_VER)

	def test_self_test(self):
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			phoebe.inf.self_test()
		self.assertEqual(mock_stdout.getvalue(), INF_ANS)


def main():
	unittest.main()


if __name__ == '__main__':
	main()

# end.
