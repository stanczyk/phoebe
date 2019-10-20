# -*- coding: utf-8 -*-
"""
	**test_mat.py**
	unit tests for *src/mat.py*

	in the module:
	* *class* **TestMat**

	Copyright (c) 2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
"""
""" @unittest.skip("not implemented yet") """
import os
import sys
import unittest
from freezegun import freeze_time  # https://github.com/spulec/freezegun
from io import StringIO
import mock
from tests.answers.ans_mat import MAT_HEADER, MAT_PREFACE, MAT_END, MAT_EQ1, MAT_EQ2, MAT_EQ3, MAT_VEC3, MAT_VEC4, \
	MAT_INI1, MAT_INI2, MAT_ADDS, MAT_MAT1, MAT_MAT2, MAT_MAT3

lib_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../phoebe')
if lib_path not in sys.path:
	sys.path.append(lib_path)
import phoebe.mat
from phoebe.err import Err


class TestMat(unittest.TestCase):
	""" class for testing *Generator* """

	def setUp(self):
		self.mat = phoebe.mat.Mat()

	def tearDown(self):
		pass

	@freeze_time("2019-09-06 14:48:05")
	def test_header(self):
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.header('nazwa-pliku'), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), MAT_HEADER)

	def test_preface(self):
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.preface(), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), MAT_PREFACE)

	def test_do_matrices(self):
		self.assertEqual(self.mat.do_matrices([], 'A', 'x', None), '')
		self.assertEqual(self.mat.do_matrices(['a'], 'A', 'x', None), 'Ax(k)')
		self.assertEqual(self.mat.do_matrices(['a'], 'A', 'x', 1), 'A0x(k+1)')
		self.assertEqual(self.mat.do_matrices(['a'], 'A', 'x', 0), 'A0x(k)')

	def test_equation(self):
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.equation(None, None, None, None), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), MAT_EQ1)
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.equation(['a'], ['b'], ['c'], ['d']), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), MAT_EQ2)
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.equation([['a0'],['a1'], None, [], ['a4']], [[], ['b0']], ['c'], ['d']), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), MAT_EQ3)

	def test_clean_value(self):
		self.assertEqual(self.mat.clean_value(None), '')
		self.assertEqual(self.mat.clean_value('-'), '-')
		self.assertEqual(self.mat.clean_value('d1'), 'd1')
		self.assertEqual(self.mat.clean_value('d_1'), 'd1')
		self.assertEqual(self.mat.clean_value('d_{1}'), 'd1')
		self.assertEqual(self.mat.clean_value('d_{1,0}'), 'd10')
		self.assertEqual(self.mat.clean_value(12), 12)

	def test_time_values(self):
		self.assertEqual(self.mat.time_values(None), Err.ERR_NO_DATA)
		self.assertEqual(self.mat.time_values({}), Err.ERR_NO_DATA)
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.time_values({'t1': 1}), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), 't1 = 1\n')
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.time_values({'t_{0,1}': 1}), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), 't01 = 1\n')
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.time_values({'t_1': 1, 'd_2': 2}), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), 'd2 = 2\nt1 = 1\n')

	def test_vector(self):
		self.assertEqual(self.mat.vector(None, None), Err.ERR_NO_NAME)
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.vector('a', None), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), 'disp(\'a(k) = [ ]\');\n')
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.vector('b', ['b1', 'b_2', 'b_{3}']), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), 'disp(\'b(k) = [ b1(k); b_2(k); b_{3}(k); ]\');\n')

	# TODO sprawdzic to
	# co powinno być dla [], None lub '-'? -> teraz jest ''
	def test_get_matrix_value(self):
		self.assertEqual(self.mat.get_matrix_value(None), '')
		self.assertEqual(self.mat.get_matrix_value([]), '')
		self.assertEqual(self.mat.get_matrix_value(['-']), '')
		self.assertEqual(self.mat.get_matrix_value(['-', 'd_1']), 'd1')
		self.assertEqual(self.mat.get_matrix_value(['d_1', '-']), 'd1')
		self.assertEqual(self.mat.get_matrix_value(['-', '-', 'd_3']), 'd3')
		self.assertEqual(self.mat.get_matrix_value(['d_1', 't_{1,2}']), 'mp_multi(d1, t12)')
		self.assertEqual(self.mat.get_matrix_value(['d_1', 'd_2', 'd_3']), 'mp_multi(mp_multi(d1, d2), d3)')
		self.assertEqual(self.mat.get_matrix_value(''), '')
		self.assertEqual(self.mat.get_matrix_value('-'), '')
		self.assertEqual(self.mat.get_matrix_value('d_3'), 'd3')
		self.assertEqual(self.mat.get_matrix_value('d_{1,3}'), 'd13')
		self.assertEqual(self.mat.get_matrix_value([1, 2]), 'mp_multi(1, 2)')
		self.assertEqual(self.mat.get_matrix_value(['-', 12]), '12')
		self.assertEqual(self.mat.get_matrix_value(0), '0')

	def test_matrix_desc(self):
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.matrix_desc(), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), '\ndisp(\'matrices:\');\n')

	def test_matrix(self):
		self.assertEqual(self.mat.matrix(None, None, None), Err.ERR_NO_NAME)
		self.assertEqual(self.mat.matrix('A', None, None), Err.ERR_NO_MATRIX)
		self.assertEqual(self.mat.matrix('A', None, []), Err.ERR_NO_MATRIX)
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.matrix('A', None, ['a']), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), MAT_MAT1)
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.matrix('A', None, [['-', '-', 'd_3'], [['d_1', 'd_{1,2}'], '-', '-'], ['-', ['d_2', 'd_{2,2}'], '-']]), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), MAT_MAT2)
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.matrix('A', '3', [['-', '-', '-'], ['d1', ['d_{21}', 'd_{22}', 'd_{23}'], '-']]), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), MAT_MAT3)

	def test_input_vec(self):
		self.assertEqual(self.mat.input_vec(None), Err.ERR_NO_VECTOR)
		self.assertEqual(self.mat.input_vec([]), Err.ERR_NO_VECTOR)
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.input_vec(['1']), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), 'U  = mp_ones(1, 1)\n')
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.input_vec(['1', '2', '3', '4', '5']), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), 'U  = mp_ones(5, 1)\n')

	def test_start_vec(self):
		self.assertEqual(self.mat.input_vec(None), Err.ERR_NO_VECTOR)
		self.assertEqual(self.mat.input_vec([]), Err.ERR_NO_VECTOR)
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.start_vec(['1']), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), 'X0 = mp_zeros(1, 1)\n')
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.start_vec(['1', '2', '3', '4', '5']), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), 'X0 = mp_zeros(5, 1)\n')

	def test_adds(self):
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.adds(), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), MAT_ADDS)

	def test_end(self):
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.end(), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), MAT_END)

	def test_inits(self):
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.inits(None, None, None), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), MAT_INI1)
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.inits([], [], {}), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), MAT_INI1)
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.inits(['u0'], ['x_1'], {'t_{0,1}': 0}), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), MAT_INI2)

	def test_vectors(self):
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.vectors(None, None, None), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), MAT_VEC3)
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.vectors([], [], []), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), MAT_VEC3)
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.vectors(['u1'], ['x1', 'x2'], ['y1', 'y2', 'y3']), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), MAT_VEC4)


def main():
	unittest.main()


if __name__ == '__main__':
	main()

# end.
