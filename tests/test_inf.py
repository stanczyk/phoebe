# -*- coding: utf-8 -*-
"""
	**test_inf.py**
	unit tests for *src/inf.py*

	in the module:
	* *class* **TestInf**

	Copyright 2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl
"""
# pylint: disable=missing-docstring
import unittest
from StringIO import StringIO
import phoebe.inf
import mock

INF_ANS = 'Inf.VER:\n\
phoebe: v.0.1\n\
\n\
Inf.DOC:\n\
Usage:\tphoebe [--file] [--details-1] [--details-2] [--vectors] <desc_file>\n\
\tphoebe -h | --help\n\
\tphoebe -v | --version\n\
\n\
Options:\n\
\t--file\t\tshow information from desc_file\n\
\t--details-1\tshow parsed information (1) from desc_file\n\
\t--details-2\tshow parsed information (2) from desc_file\n\
\t--vectors\tshow vectors: u(k), x(k) and y(k)\n\
\t-h, --help\tshows this help message and exit\n\
\t-v, --version\tshow version information and exit\n'


class TestInf(unittest.TestCase):
	""" class for testing *Generator* """
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_self_test(self):
		with mock.patch('sys.stdout', new=StringIO()) as fake_stdout:
			phoebe.inf.self_test()
			self.assertEqual(fake_stdout.getvalue(), INF_ANS)


def main():
	unittest.main()


if __name__ == '__main__':
	main()

# end.