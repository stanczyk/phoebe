# -*- coding: utf-8 -*-
"""
	**test_command_line.py**
	unit tests for *vcm/command_line.py*

	in the module:

	* *class* **TestConsole**

	Copyright 2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl
"""
# pylint: disable=missing-docstring, bad-continuation

import os
from StringIO import StringIO
import unittest
import vcm.parser
import vcm.err
import mock


class TestParser(unittest.TestCase):
	""" class for testing *Generator* """
	def setUp(self):
		self.par = vcm.parser.Parser()
		self.args = {
			'--body': False,
			'--help': False,
			'--info': False,
			'--metadata': False,
			'--stdin': False,
			'--verbose': False,
			'--version': False,
			'-b': False,
			'-h': False,
			'-i': False,
			'-m': False,
			'-s': False,
			'-v': False,
			'-V': False,
			'<vcf_file>': None
		}

	def tearDown(self):
		pass

	@mock.patch('vcm.parser.docopt.docopt')
	def test_main__non_existing_file(self, mock_docopt):
		# non existing file
		args = self.args
		args['<vcf_file>'] = os.getcwd() + '/tests/samples/non_existing_file'
		mock_docopt.return_value = args
		with self.assertRaises(SystemExit) as system_exit:
			self.par.main()
		self.assertEqual(system_exit.exception.code, vcm.err.Err.ERR_NO_FILE)

	@mock.patch('vcm.parser.docopt.docopt')
	def test_main__wrong_file(self, mock_docopt):
		# existing file, not vcf
		args = self.args
		args['<vcf_file>'] = os.getcwd() + '/tests/samples/01.vcf'
		mock_docopt.return_value = args
		with self.assertRaises(SystemExit) as system_exit:
			self.par.main()
		self.assertEqual(system_exit.exception.code, vcm.err.Err.ERR_VCF_READER)

	@mock.patch('vcm.parser.docopt.docopt')
	def test_main__wrong_file_gz(self, mock_docopt):
		args = self.args
		args['<vcf_file>'] = os.getcwd() + '/tests/samples/01.vcf.gz'
		mock_docopt.return_value = args
		with self.assertRaises(SystemExit) as system_exit:
			self.par.main()
		self.assertEqual(system_exit.exception.code, vcm.err.Err.ERR_VCF_READER)

	@mock.patch('vcm.parser.docopt.docopt')
	def test_main__file_40(self, mock_docopt):
		# vcf 4.0
		args = self.args
		args['<vcf_file>'] = os.getcwd() + '/tests/samples/example-4.0.vcf'
		mock_docopt.return_value = args
		with self.assertRaises(SystemExit) as system_exit:
			self.par.main()
		self.assertEqual(system_exit.exception.code, vcm.err.Err.NOOP)

	@mock.patch('vcm.parser.docopt.docopt')
	def test_main__file_40_gz(self, mock_docopt):
		args = self.args
		args['<vcf_file>'] = os.getcwd() + '/tests/samples/example-4.0.vcf.gz'
		mock_docopt.return_value = args
		with self.assertRaises(SystemExit) as system_exit:
			self.par.main()
		self.assertEqual(system_exit.exception.code, vcm.err.Err.NOOP)

	@mock.patch('vcm.parser.docopt.docopt')
	def test_main__file_41(self, mock_docopt):
		# vcf 4.1
		args = self.args
		args['<vcf_file>'] = os.getcwd() + '/tests/samples/example-4.1.vcf'
		mock_docopt.return_value = args
		with self.assertRaises(SystemExit) as system_exit:
			self.par.main()
		self.assertEqual(system_exit.exception.code, vcm.err.Err.NOOP)

	@mock.patch('vcm.parser.docopt.docopt')
	def test_main__file_41_gz(self, mock_docopt):
		args = self.args
		args['<vcf_file>'] = os.getcwd() + '/tests/samples/example-4.1.vcf.gz'
		mock_docopt.return_value = args
		with self.assertRaises(SystemExit) as system_exit:
			self.par.main()
		self.assertEqual(system_exit.exception.code, vcm.err.Err.NOOP)

	@mock.patch('vcm.parser.docopt.docopt')
	def test_main__file_42(self, mock_docopt):
		# vcf 4.2
		args = self.args
		args['<vcf_file>'] = os.getcwd() + '/tests/samples/example-4.2.vcf'
		mock_docopt.return_value = args
		with self.assertRaises(SystemExit) as system_exit:
			self.par.main()
		self.assertEqual(system_exit.exception.code, vcm.err.Err.NOOP)

	@mock.patch('vcm.parser.docopt.docopt')
	def test_main__file_42_gz(self, mock_docopt):
		args = self.args
		args['<vcf_file>'] = os.getcwd() + '/tests/samples/example-4.2.vcf.gz'
		mock_docopt.return_value = args
		with self.assertRaises(SystemExit) as system_exit:
			self.par.main()
		self.assertEqual(system_exit.exception.code, vcm.err.Err.NOOP)

	@mock.patch('vcm.parser.docopt.docopt')
	def test_main__no_args(self, mock_docopt):
		mock_docopt.return_value = self.args
		with self.assertRaises(SystemExit) as system_exit:
			self.par.main()
		self.assertEqual(system_exit.exception.code, vcm.err.Err.ERR_NO_INPUT_FILE)

	@mock.patch('vcm.parser.docopt.docopt')
	def test_main__verbose(self, mock_docopt):
		args = self.args
		args['-V'] = True
		mock_docopt.return_value = args
		# no file
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			with self.assertRaises(SystemExit) as system_exit:
				self.par.main()
		self.assertEqual(system_exit.exception.code, vcm.err.Err.ERR_NO_INPUT_FILE)
		ans = '---\n' \
			'vcmcli: v.0.1\n' \
			'parsing status:\n' \
			'- 1\n' \
			'- ERR_NO_INPUT_FILE\n' \
			'\n'
		self.assertEqual(mock_stdout.getvalue(), ans)

		# with file
		self.par.prn = False
		args['-V'] = False
		args['--verbose'] = True
		args['<vcf_file>'] = os.getcwd() + '/tests/samples/example-4.0.vcf'
		mock_docopt.return_value = args
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			with self.assertRaises(SystemExit) as system_exit:
				self.par.main()
		self.assertEqual(system_exit.exception.code, vcm.err.Err.NOOP)
		ans = '---\n' \
			'vcmcli: v.0.1\n' \
			'parsing status:\n' \
			'- 0\n' \
			'- NOOP\n' \
			'\n'
		self.assertEqual(mock_stdout.getvalue(), ans)

	@mock.patch('vcm.parser.docopt.docopt')
	def test_main__version(self, mock_docopt):
		args = self.args
		args['-v'] = True
		mock_docopt.return_value = args
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			with self.assertRaises(SystemExit) as system_exit:
				self.par.main()
		self.assertEqual(system_exit.exception.code, vcm.err.Err.NOOP)
		self.assertEqual(mock_stdout.getvalue(), self.par.get_version() + '\n')

	@mock.patch('vcm.parser.docopt.docopt')
	def test_main__info(self, mock_docopt):
		args = self.args
		args['-i'] = True
		args['<vcf_file>'] = os.getcwd() + '/tests/samples/example-4.0.vcf'
		mock_docopt.return_value = args
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			with self.assertRaises(SystemExit) as system_exit:
				self.par.main()
		self.assertEqual(system_exit.exception.code, vcm.err.Err.NOOP)
		ans = '---\n' \
			'file_format: VCFv4.0\n' \
			'file_name: %(pwd)s/tests/samples/example-4.0.vcf\n' \
			'rec_amount: 6\n' \
			'samples:\n' \
			'- NA00001\n' \
			'- NA00002\n' \
			'- NA00003\n' \
			'\n' % {'pwd': os.getcwd()}
		self.assertEqual(mock_stdout.getvalue(), ans)


def main():
	unittest.main()


if __name__ == '__main__':
	main()

# end.
