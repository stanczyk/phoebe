# -*- coding: utf-8 -*-
"""
	**test_parser.py**
	unit tests for *src/worker.py*

	in the module:
	* *class* **TestWorker**

	Copyright 2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl
"""
# pylint: disable=missing-docstring
import os
from StringIO import StringIO
import unittest
import phoebe.err
import phoebe.worker
import mock

ANS_VEC2 = '\
== VECTORS =================\n\
u(k) = [ ]\n\
x(k) = [ ]\n\
y(k) = [ y_1(k) ]\n'

ANS_VEC4 = '\
== VECTORS =================\n\
u(k) = [ u(k) ]\n\
x(k) = [ x_1(k) x_2(k) x_3(k) ]\'\n\
y(k) = [ y(k) ]\n'

ANS_DET2 = '\
== DETAILS 3 ===============\n\
{\'y_1\': 0}\n\
== MATRICES ================\n\
A0 = A1 = B0 = []\n\
A0 = A1 = B0 = []\n\
A0 = A1 = B0 = []\n\
C  = [[]]\n'

ANS_DET4 = '\
== DETAILS 3 ===============\n\
{\'M_3\': 2, \'M_2\': 1, \'M_1\': 0, \'u\': 0, \'y\': 0}\n\
== MATRICES ================\n\
A0 = [[\'-\', \'-\', \'-\'], [\'d_1t_{1,2}\', \'-\', \'-\'], [\'-\', \'d_2t_{2,3}\', \'-\']]\n\
A1 = [[\'d_1\', \'-\', \'-\'], [\'-\', \'d_2\', \'-\'], [\'-\', \'-\', \'d_3\']]\n\
B0 = [[\'t_{0,1}\'], [\'-\'], [\'-\']]\n\
C  = [[\'-\', \'-\', \'d_3t_{3,4}\']]\n'


class TestWorker(unittest.TestCase):
	""" class for testing *Generator* """
	# pylint: disable=bad-continuation, missing-docstring
	def setUp(self):
		self.worker = phoebe.worker.Worker()
		self.var = {
			'A0': [],
			'A1': [],
			'B0': [],
			'C': [],
			'mapping': {},
			'parser': None,
			'u': [],
			'x': [],
			'y': []
		}
		self.args = {
			'--details-1': False,
			'--details-2': False,
			'--details-3': False,
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
		args['--details-3'] = True
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f2.yml'
		mock_docopt.return_value = args
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			with self.assertRaises(SystemExit) as system_exit:
				self.worker.main()
		self.assertEqual(system_exit.exception.code, phoebe.err.Err.NOOP)
		self.assertEqual(mock_stdout.getvalue(), ANS_DET2)

	@mock.patch('phoebe.parser.docopt.docopt')
	def test_get_details4(self, mock_docopt):
		args = self.args
		args['--details-3'] = True
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f4.yml'
		mock_docopt.return_value = args
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			with self.assertRaises(SystemExit) as system_exit:
				self.worker.main()
		self.assertEqual(system_exit.exception.code, phoebe.err.Err.NOOP)
		self.assertEqual(mock_stdout.getvalue(), ANS_DET4)


def main():
	unittest.main()


if __name__ == '__main__':
	main()

# end.
