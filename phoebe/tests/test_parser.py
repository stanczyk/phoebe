# -*- coding: utf-8 -*-
"""
	**test_parser.py**
	unit tests for *src/parser.py*

	in the module:
	* *class* **TestParser**

	Copyright 2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl
"""
# import os
# from StringIO import StringIO
import unittest
# import src.parser
# import src.err
# import mock


class TestParser(unittest.TestCase):
	""" class for testing *Generator* """
	def setUp(self):
		self.par = vcm.parser.Parser()
		self.args = {
			'--help': False,
			'--version': False,
			'-h': False,
			'-v': False,
			'<desc_file>': None
		}

	def tearDown(self):
		pass


def main():
	unittest.main()


if __name__ == '__main__':
	main()

# end.
