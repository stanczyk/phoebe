# -*- coding: utf-8 -*-
"""
	**test_parser.py**
	unit tests for *src/worker.py*

	in the module:
	* *class* **TestWorker**

	Copyright (c) 2017-2018 Jarosław Stańczyk <jaroslaw.stanczyk@upwr.edu.pl>
"""
import os
from StringIO import StringIO
import unittest
import mock
import phoebe.err
import phoebe.worker
import phoebe.yml
from answers import ANS_VEC2, ANS_VEC4,\
	ANS_DET3_2, ANS_DET3_4, ANS_DET3_5,\
	ANS_MAT4, ANS_MAT5,\
	ANS_LAT4, ANS_LAT5,\
	GEN_TIME,\
	ANS_INP1, ANS_INP2, ANS_SYS1, ANS_SYS2, ANS_OUT1, ANS_OUT2, ANS_MAP1, ANS_MAP2,\
	ANS_MX0, ANS_MX1, ANS_MX2, ANS_MX3, ANS_MX4, ANS_MX5, ANS_MX6, ANS_MX7, ANS_MX8, ANS_MX9, ANS_MX10


class TestWorker(unittest.TestCase):
	""" class for testing *Generator* """
	# pylint: disable=invalid-name, too-many-public-methods
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
			'--matrices': False,
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

	def test_create_matrix(self):
		# example of build matrix B0 according to specs/desc1_3.yml
		matrix = []
		vect_x = ['x_1', 'x_2', 'x_3', 'x_4', 'x_5', 'x_6', 'x_7']
		vect_y = ['y_1', 'y_2', 'y_3', 'y_4', 'y_5', 'y_6']
		self.assertEqual(self.worker.create_matrix(matrix, vect_x, vect_y), ANS_MX0)

	def test_fill_(self):
		self.worker.B0 = ANS_MX0
		self.worker.A0 = self.worker.A1 = self.worker.C = []
		con = {'X_1': {'tr-time': '0', 'buffers': '-'}}
		self.worker.init_parser()
		self.worker.parser.yml = phoebe.yml.Yml()
		self.worker.mapping = ANS_MAP1
		self.assertEqual(self.worker.fill_(self.worker.B0, 0, con, ['0']), ANS_MX1)

	def test_fill_matrix(self):
		# example of filling matrix B0 according to specs/desc1_3.yml
		self.worker.B0 = ANS_MX0
		self.worker.A0 = self.worker.A1 = self.worker.C = []
		we = ANS_INP1
		self.worker.init_parser()
		self.worker.parser.yml = phoebe.yml.Yml()
		self.worker.mapping = ANS_MAP1
		self.assertEqual(self.worker.fill_matrix(self.worker.B0, we), ANS_MX2)

	def test_add_feedback_u(self):
		we = ANS_INP2
		sy = ANS_SYS2
		wy = ANS_OUT2
		self.worker.A1 = ANS_MX9
		self.worker.mapping = ANS_MAP2
		self.worker.init_parser()
		self.worker.parser.yml = phoebe.yml.Yml()
		self.assertEqual(self.worker.add_feedback_u(self.worker.A1, we, sy, wy), ANS_MX10)

	def test_add_feedback_x(self):
		# example of filling matrix A1 from specs/desc1_3.yml
		self.worker.A1 = ANS_MX3
		sy = ANS_SYS1
		wy = ANS_OUT1
		self.worker.init_parser()
		self.worker.parser.yml = phoebe.yml.Yml()
		self.worker.mapping = ANS_MAP1
		self.assertEqual(self.worker.add_feedback_x(self.worker.A1, sy, wy), ANS_MX4)

	def test_optimize_matrix(self):
		self.worker.init_parser()
		self.worker.parser.yml = phoebe.yml.Yml()
		self.assertEqual(self.worker.optimize_matrix(ANS_MX4), ANS_MX5)

	def test_rm_repeated_zeros(self):
		self.worker.init_parser()
		self.worker.parser.yml = phoebe.yml.Yml()
		self.assertEqual(self.worker.rm_repeated_zeros(ANS_MX6), [['-', ['d_6', '0'], ['d_7', '0']]])

	def test_rm_redundant_zeros(self):
		self.worker.init_parser()
		self.worker.parser.yml = phoebe.yml.Yml()
		self.assertEqual(self.worker.rm_redundant_zeros(ANS_MX7), ANS_MX8)


def main():
	unittest.main()


if __name__ == '__main__':
	main()

# end.
