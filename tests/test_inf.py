# -*- coding: utf-8 -*-
"""
	**test_inf.py**
	unit tests for *src/inf.py*

	in the module:
	* *class* **TestInf**

	Copyright 2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl
"""
import unittest
import src.inf
import mock
from StringIO import StringIO

INF_ANS = 'Inf.VER:\n\
phoebe: v.0.1\n\
\n\
Inf.DOC:\n\
Usage:\tphoebe <desc_file>\n\
\tphoebe -h | --help\n\
\tphoebe -v | --version\n\
\n\
Options:\n\
\t-h, --help\tshows this help message and exit.\n\
\t-v, --version\tshow version information and exit.\n'


class TestInf(unittest.TestCase):
	""" class for testing *Generator* """
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_self_test(self):
		with mock.patch('sys.stdout', new=StringIO()) as fake_stdout:
			src.inf.self_test()
			self.assertEqual(fake_stdout.getvalue(), INF_ANS)


def main():
	unittest.main()


if __name__ == '__main__':
	main()

# end.
