# -*- coding: utf-8 -*-
"""
	**test_parser.py**
	unit tests for *src/parser.py*

	in the module:
	* *class* **TestParser**

	Copyright 2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl
"""
# pylama: ignore=E101
import os
from StringIO import StringIO
import unittest
import phoebe.parser
import phoebe.err
import mock
from answers import ANS_FILE, ANS_DET1_2, ANS_DET1_4, ANS_DET1_5, ANS_DET2_2, ANS_DET2_4, ANS_DET2_5


class TestParser(unittest.TestCase):
	""" class for testing *Parser* """
	def setUp(self):
		self.par = phoebe.parser.Parser()
		self.args = {
			'--det1': False,
			'--det2': False,
			'--det3': False,
			'--file': False,
			'--help': False,
			'--vectors': False,
			'--version': False,
			'--latex': False,
			'--no-desc': True,
			'-h': False,
			'-v': False,
			'<desc_file>': None
		}

	def tearDown(self):
		pass

	def test___init__(self):
		ans = {
			'args': None,
			'content_yaml': None,
			'file_handler': None,
			'file_name': None,
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
		self.assertEqual(self.par.main(), phoebe.err.Err.NOOP)

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
		self.assertEqual(mock_stdout.getvalue(), phoebe.parser.Inf().get_version() + '\n')

	@mock.patch('phoebe.parser.docopt.docopt')
	def test_get_file(self, mock_docopt):
		args = self.args
		args['--file'] = True
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f2.yml'
		mock_docopt.return_value = args
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.par.main()
		self.assertEqual(mock_stdout.getvalue(), ANS_FILE)

	@mock.patch('phoebe.parser.docopt.docopt')
	def test_get_det1_2(self, mock_docopt):
		args = self.args
		args['--det1'] = True
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f2.yml'
		mock_docopt.return_value = args
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.par.main()
		self.assertEqual(mock_stdout.getvalue(), ANS_DET1_2)

	@mock.patch('phoebe.parser.docopt.docopt')
	def test_get_det1_4(self, mock_docopt):
		args = self.args
		args['--det1'] = True
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f4.yml'
		mock_docopt.return_value = args
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.par.main()
		self.assertEqual(mock_stdout.getvalue(), ANS_DET1_4)

	@mock.patch('phoebe.parser.docopt.docopt')
	def test_get_det1_5(self, mock_docopt):
		args = self.args
		args['--det1'] = True
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f5.yml'
		mock_docopt.return_value = args
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.par.main()
		self.assertEqual(mock_stdout.getvalue(), ANS_DET1_5)

	@mock.patch('phoebe.parser.docopt.docopt')
	def test_get_det2_2(self, mock_docopt):
		args = self.args
		args['--det2'] = True
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f2.yml'
		mock_docopt.return_value = args
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.par.main()
		self.assertEqual(mock_stdout.getvalue(), ANS_DET2_2)

	@mock.patch('phoebe.parser.docopt.docopt')
	def test_get_det2_4(self, mock_docopt):
		args = self.args
		args['--det2'] = True
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f4.yml'
		mock_docopt.return_value = args
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.par.main()
		self.assertEqual(mock_stdout.getvalue(), ANS_DET2_4)

	@mock.patch('phoebe.parser.docopt.docopt')
	def test_get_det2_5(self, mock_docopt):
		args = self.args
		args['--det2'] = True
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f5.yml'
		mock_docopt.return_value = args
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.par.main()
		self.assertEqual(mock_stdout.getvalue(), ANS_DET2_5)


def main():
	unittest.main()


if __name__ == '__main__':
	main()

# end.
