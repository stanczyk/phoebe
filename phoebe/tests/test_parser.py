# -*- coding: utf-8 -*-
"""
	**test_parser.py**
	unit tests for *src/parser.py*

	in the module:
	* *class* **TestParser**

	Copyright 2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl
"""
# pylint: disable=missing-docstring, bad-continuation
import os
from StringIO import StringIO
import unittest
import phoebe.parser
import phoebe.err
import mock


class TestParser(unittest.TestCase):
	""" class for testing *Generator* """
	def setUp(self):
		self.par = phoebe.parser.Parser()
		self.args = {
			'--details-1': False,
			'--details-2': False,
			'--file': False,
			'--help': False,
			'--vectors': False,
			'--version': False,
			'-h': False,
			'-v': False,
			'<desc_file>': None
		}

	def tearDown(self):
		pass

	def test___init__(self):
		ans = {
			'A0': [],
			'A1': [],
			'B0': [],
			'C': [],
			'args': None,
			'content_yaml': None,
			'file_handler': None,
			'file_name': None,
			'u': [],
			'x': [],
			'y': [],
			'yaml': None
		}
		phe = phoebe.parser.Parser()
		self.assertEqual(phe.__dict__, ans)

	@mock.patch('phoebe.parser.docopt.docopt')
	def test_main__non_existing_file(self, mock_docopt):
		args = self.args
		args['<desc_file>'] = os.getcwd() + '/tests/samples/non_existing_file'
		mock_docopt.return_value = args
		with self.assertRaises(SystemExit) as system_exit:
			self.par.main()
		self.assertEqual(system_exit.exception.code, phoebe.err.Err.ERR_NO_FILE)

	@mock.patch('phoebe.parser.docopt.docopt')
	def test_main__wrong_file(self, mock_docopt):
		args = self.args
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f3.yml'
		mock_docopt.return_value = args
		with self.assertRaises(SystemExit) as system_exit:
			self.par.main()
		self.assertEqual(system_exit.exception.code, phoebe.err.Err.ERR_IO)

	@mock.patch('phoebe.parser.docopt.docopt')
	def test_main__file(self, mock_docopt):
		args = self.args
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f2.yml'
		mock_docopt.return_value = args
		with self.assertRaises(SystemExit) as system_exit:
			self.par.main()
		self.assertEqual(system_exit.exception.code, phoebe.err.Err.NOOP)

	@mock.patch('phoebe.parser.docopt.docopt')
	def test_main__no_args(self, mock_docopt):
		mock_docopt.return_value = self.args
		with self.assertRaises(SystemExit) as system_exit:
			self.par.main()
		self.assertEqual(system_exit.exception.code, phoebe.err.Err.ERR_NO_INPUT_FILE)

	@mock.patch('phoebe.parser.docopt.docopt')
	def test_get_version(self, mock_docopt):
		args = self.args
		args['-v'] = True
		mock_docopt.return_value = args
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			with self.assertRaises(SystemExit) as system_exit:
				self.par.main()
		self.assertEqual(system_exit.exception.code, phoebe.err.Err.NOOP)
		self.assertEqual(mock_stdout.getvalue(), self.par.get_version() + '\n')

	# def test_epilog(self, err):
	# def test_main(self):


def main():
	unittest.main()


if __name__ == '__main__':
	main()

# end.
