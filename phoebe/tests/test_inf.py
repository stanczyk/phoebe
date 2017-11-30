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

INF_ANS = '\
Inf.VER:\n\
phoebe: v.0.1\n\
\n\
Inf.DOC:\n\
Usage:\tphoebe [--file] [--details-1] [--details-2] [--details-3] [--vectors] [--latex] <desc_file>\n\
\tphoebe -h | --help\n\
\tphoebe -v | --version\n\
\n\
Options:\n\
\t--file\t\tshow information from desc_file\n\
\t--details-1\tshow parsed information (1) from desc_file\n\
\t--details-2\tshow parsed information (2) from desc_file\n\
\t--details-3\tshow mapping and parsed matrices\n\
\t--vectors\tshow vectors: u(k), x(k) and y(k)\n\
\t--latex\t\tgenerate description for latex, default is matlab description\n\
\t-h, --help\tshows this help message and exit\n\
\t-v, --version\tshow version information and exit\n'

INF_VER = '\
phoebe: v.0.1\n\
author: Jaroslaw Stanczyk\n\
e-mail: jaroslaw.stanczyk@upwr.edu.pl\n\
copyright: (c) 2017 Jaroslaw Stanczyk'


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
