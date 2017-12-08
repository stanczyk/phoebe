# -*- coding: utf-8 -*-
"""
	**test_parser.py**
	unit tests for *src/worker.py*

	in the module:
	* *class* **TestWorker**

	Copyright 2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl
"""
import os
from StringIO import StringIO
import unittest
import phoebe.err
import phoebe.worker
import mock
from answers import ANS_VEC2, ANS_VEC4,\
	ANS_DET3_2, ANS_DET3_4, ANS_DET3_5,\
	ANS_MAT4, ANS_MAT5,\
	ANS_LAT4, ANS_LAT5,\
	GEN_TIME


class TestWorker(unittest.TestCase):
	""" class for testing *Generator* """
	def setUp(self):
		self.worker = phoebe.worker.Worker()
		self.var = {
			'u': [],
			'x': [],
			'y': [],
			'A0': [],
			'A1': [],
			'B0': [],
			'C': [],
			'mapping': {},
			'parser': None,
			'values': None
		}
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
		self.assertEqual(self.worker.__dict__, self.var)

	@mock.patch('phoebe.parser.docopt.docopt')
	def test_get_vectors2(self, mock_docopt):
		args = self.args
		args['--vectors'] = True
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f2.yml'
		mock_docopt.return_value = args
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			with self.assertRaises(SystemExit) as system_exit:
				self.worker.main()
		self.assertEqual(system_exit.exception.code, phoebe.err.Err.NOOP)
		self.assertEqual(mock_stdout.getvalue(), ANS_VEC2)

	@mock.patch('phoebe.parser.docopt.docopt')
	def test_get_vectors4(self, mock_docopt):
		args = self.args
		args['--vectors'] = True
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f4.yml'
		mock_docopt.return_value = args
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			with self.assertRaises(SystemExit) as system_exit:
				self.worker.main()
		self.assertEqual(system_exit.exception.code, phoebe.err.Err.NOOP)
		self.assertEqual(mock_stdout.getvalue(), ANS_VEC4)

	@mock.patch('phoebe.parser.docopt.docopt')
	def test_get_det3_2(self, mock_docopt):
		args = self.args
		args['--det3'] = True
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f2.yml'
		mock_docopt.return_value = args
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			with self.assertRaises(SystemExit) as system_exit:
				self.worker.main()
		self.assertEqual(system_exit.exception.code, phoebe.err.Err.NOOP)
		self.assertEqual(mock_stdout.getvalue(), ANS_DET3_2)

	@mock.patch('phoebe.parser.docopt.docopt')
	def test_get_det3_4(self, mock_docopt):
		args = self.args
		args['--det3'] = True
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f4.yml'
		mock_docopt.return_value = args
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			with self.assertRaises(SystemExit) as system_exit:
				self.worker.main()
		self.assertEqual(system_exit.exception.code, phoebe.err.Err.NOOP)
		self.assertEqual(mock_stdout.getvalue(), ANS_DET3_4)

	@mock.patch('phoebe.parser.docopt.docopt')
	def test_get_det3_5(self, mock_docopt):
		args = self.args
		args['--det3'] = True
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f5.yml'
		mock_docopt.return_value = args
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			with self.assertRaises(SystemExit) as system_exit:
				self.worker.main()
		self.assertEqual(system_exit.exception.code, phoebe.err.Err.NOOP)
		self.assertEqual(mock_stdout.getvalue(), ANS_DET3_5)

	@mock.patch('phoebe.parser.docopt.docopt')
	def test_no_desc1(self, mock_docopt):
		args = self.args
		args['--no-desc'] = False
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f1.yml'
		mock_docopt.return_value = args
		with self.assertRaises(SystemExit) as system_exit:
			self.worker.main()
		self.assertEqual(system_exit.exception.code, phoebe.err.Err.ERR_NO_DATA)

	@mock.patch('phoebe.parser.docopt.docopt')
	def test_no_desc2(self, mock_docopt):
		args = self.args
		args['--no-desc'] = False
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f2.yml'
		mock_docopt.return_value = args
		with self.assertRaises(SystemExit) as system_exit:
			self.worker.main()
		self.assertEqual(system_exit.exception.code, phoebe.err.Err.ERR_NO_DATA)

	@mock.patch('phoebe.parser.docopt.docopt')
	def test_no_desc3(self, mock_docopt):
		args = self.args
		args['--no-desc'] = False
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f3.yml'
		mock_docopt.return_value = args
		with self.assertRaises(SystemExit) as system_exit:
			self.worker.main()
		self.assertEqual(system_exit.exception.code, phoebe.err.Err.ERR_IO)

	@mock.patch('phoebe.parser.docopt.docopt')
	@mock.patch('phoebe.parser.Inf.get_time')
	def test_get_matlab_desc4(self, mock_time, mock_docopt):
		mock_time.return_value = GEN_TIME
		args = self.args
		args['--no-desc'] = False
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f4.yml'
		mock_docopt.return_value = args
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			with self.assertRaises(SystemExit) as system_exit:
				self.worker.main()
		self.assertEqual(system_exit.exception.code, phoebe.err.Err.NOOP)
		self.assertEqual(mock_stdout.getvalue(), ANS_MAT4)

	@mock.patch('phoebe.parser.docopt.docopt')
	@mock.patch('phoebe.parser.Inf.get_time')
	def test_get_matlab_desc5(self, mock_time, mock_docopt):
		mock_time.return_value = GEN_TIME
		args = self.args
		args['--no-desc'] = False
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f5.yml'
		mock_docopt.return_value = args
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			with self.assertRaises(SystemExit) as system_exit:
				self.worker.main()
		self.assertEqual(system_exit.exception.code, phoebe.err.Err.NOOP)
		self.assertEqual(mock_stdout.getvalue(), ANS_MAT5)

	@mock.patch('phoebe.parser.docopt.docopt')
	@mock.patch('phoebe.parser.Inf.get_time')
	def test_get_latex_desc4(self, mock_time, mock_docopt):
		mock_time.return_value = GEN_TIME
		args = self.args
		args['--latex'] = True
		args['--no-desc'] = False
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f4.yml'
		mock_docopt.return_value = args
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			with self.assertRaises(SystemExit) as system_exit:
				self.worker.main()
		self.assertEqual(system_exit.exception.code, phoebe.err.Err.NOOP)
		self.assertEqual(mock_stdout.getvalue(), ANS_LAT4)

	@mock.patch('phoebe.parser.docopt.docopt')
	@mock.patch('phoebe.parser.Inf.get_time')
	def test_get_latex_desc5(self, mock_time, mock_docopt):
		mock_time.return_value = GEN_TIME
		args = self.args
		args['--latex'] = True
		args['--no-desc'] = False
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f5.yml'
		mock_docopt.return_value = args
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			with self.assertRaises(SystemExit) as system_exit:
				self.worker.main()
		self.assertEqual(system_exit.exception.code, phoebe.err.Err.NOOP)
		self.assertEqual(mock_stdout.getvalue(), ANS_LAT5)


def main():
	unittest.main()


if __name__ == '__main__':
	main()

# end.
