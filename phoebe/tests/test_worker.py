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
from answers import ANS_VEC2, ANS_VEC4, ANS_DET3_2, ANS_DET3_4, ANS_DET3_5


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
			'--details1': False,
			'--details2': False,
			'--details3': False,
			'--file': False,
			'--help': False,
			'--vectors': False,
			'--version': False,
			'--latex': False,
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
	def test_get_details2(self, mock_docopt):
		args = self.args
		args['--details3'] = True
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f2.yml'
		mock_docopt.return_value = args
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			with self.assertRaises(SystemExit) as system_exit:
				self.worker.main()
		self.assertEqual(system_exit.exception.code, phoebe.err.Err.NOOP)
		self.assertEqual(mock_stdout.getvalue(), ANS_DET3_2)

	@mock.patch('phoebe.parser.docopt.docopt')
	def test_get_details4(self, mock_docopt):
		args = self.args
		args['--details3'] = True
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f4.yml'
		mock_docopt.return_value = args
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			with self.assertRaises(SystemExit) as system_exit:
				self.worker.main()
		self.assertEqual(system_exit.exception.code, phoebe.err.Err.NOOP)
		self.assertEqual(mock_stdout.getvalue(), ANS_DET3_4)

	@mock.patch('phoebe.parser.docopt.docopt')
	def test_get_details5(self, mock_docopt):
		args = self.args
		args['--details3'] = True
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f5.yml'
		mock_docopt.return_value = args
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			with self.assertRaises(SystemExit) as system_exit:
				self.worker.main()
		self.assertEqual(system_exit.exception.code, phoebe.err.Err.NOOP)
		self.assertEqual(mock_stdout.getvalue(), ANS_DET3_5)


def main():
	unittest.main()


if __name__ == '__main__':
	main()

# end.
