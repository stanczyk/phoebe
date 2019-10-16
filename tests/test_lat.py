# -*- coding: utf-8 -*-
"""
	**test_lat.py**
	unit tests for *src/lat.py*

	in the module:
	* *class* **TestLat**

	Copyright (c) 2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
"""
import os
import sys
import unittest
from freezegun import freeze_time  # https://github.com/spulec/freezegun
from io import StringIO
import mock
from tests.answers.ans_lat import LAT_HEADER, LAT_PREFACE, LAT_END, LAT_EQ1, LAT_EQ2, LAT_EQ3, \
	LAT_VEC1, LAT_VEC2, LAT_VEC3, LAT_VEC4, LAT_TV1, LAT_TV2, LAT_TV3, LAT_MAT1, LAT_MAT2, LAT_MAT3

lib_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../phoebe')
if lib_path not in sys.path:
	sys.path.append(lib_path)
import phoebe.lat
from phoebe.err import Err


class TestLat(unittest.TestCase):
	""" class for testing *Generator* """

	def setUp(self):
		self.lat = phoebe.lat.Lat()

	def tearDown(self):
		pass

	@freeze_time("2019-09-06 14:48:05")
	def test_header(self):
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.lat.header('nazwa-pliku'), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), LAT_HEADER)

	@freeze_time("2019-09-06 14:48:05")
	def test_preface(self):
		self.lat.header('plik')  # used to set the time only
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.lat.preface(), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), LAT_PREFACE)

	def test_do_matrices(self):
		self.assertEqual(self.lat.do_matrices([], 'A', 'x', None), '')
		self.assertEqual(self.lat.do_matrices(['a'], 'A', 'x', None), '\\mathbf{Ax}(k)')
		self.assertEqual(self.lat.do_matrices(['a'], 'A', 'x', 1), '\\mathbf{A}_{0}\\mathbf{x}(k+1)')
		self.assertEqual(self.lat.do_matrices(['a'], 'A', 'x', 0), '\\mathbf{A}_{0}\\mathbf{x}(k)')

	def test_equation(self):
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.lat.equation(None, None, None, None), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), LAT_EQ1)
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.lat.equation(['a'], ['b'], ['c'], ['d']), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), LAT_EQ2)
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.lat.equation([['a0'],['a1'], None, [], ['a4']], [['b0']], ['c'], ['d']), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), LAT_EQ3)

	def test_vector(self):
		self.assertEqual(self.lat.vector(None, None), Err.ERR_NO_NAME)
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.lat.vector('a', None), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), LAT_VEC1)
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.lat.vector('b', ['b1', 'b_2', 'b_{3}']), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), LAT_VEC2)

	def test_get_matrix_value(self):
		self.assertEqual(self.lat.get_matrix_value(None), '-')
		self.assertEqual(self.lat.get_matrix_value([]), '-')
		self.assertEqual(self.lat.get_matrix_value(['-']), '-')
		self.assertEqual(self.lat.get_matrix_value(['-', 'd_1']), 'd_1')
		self.assertEqual(self.lat.get_matrix_value(['d_1', '-']), 'd_1')
		self.assertEqual(self.lat.get_matrix_value(['d_1', 't_{1,2}']), 'd_1t_{1,2}')
		self.assertEqual(self.lat.get_matrix_value(['d_1', 'd_2', 'd_3']), 'd_1d_2d_3')
		self.assertEqual(self.mat.get_matrix_value(0), 0)
		self.assertEqual(self.mat.get_matrix_value(['-', 12]), 12)

	def test_matrix_desc(self):
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.lat.matrix_desc(), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), '\\\\\n\\\\\nmatrices:\n')

	def test_matrix(self):
		self.assertEqual(self.lat.matrix(None, None, None), Err.ERR_NO_NAME)
		self.assertEqual(self.lat.matrix('A', None, None), Err.ERR_NO_MATRIX)
		self.assertEqual(self.lat.matrix('A', None, []), Err.ERR_NO_MATRIX)
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.lat.matrix('A', None, ['a']), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), LAT_MAT1)
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.lat.matrix('A', None, [['-', '-', 'd_3'], [['d_1', 'd_{1,2}'], '-', '-'], ['-', ['d_2', 'd_{2,2}'], '-']]), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), LAT_MAT2)
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.lat.matrix('A', '3', [['-', '-', '-'], ['d1', ['d_{21}', 'd_{22}', 'd_{23}'], '-']]), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), LAT_MAT3)

	def test_time_values(self):
		self.assertEqual(self.lat.time_values(None), Err.ERR_NO_DATA)
		self.assertEqual(self.lat.time_values({}), Err.ERR_NO_DATA)
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.lat.time_values({'t1': 1}), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), LAT_TV1)
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.lat.time_values({'t_{0,1}': 1}), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), LAT_TV2)
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.lat.time_values({'t_1': 1, 'd_2': 2}), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), LAT_TV3)

	def test_end(self):
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.lat.end(), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), LAT_END)

	def test_inits(self):
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.lat.inits(None, None, None), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), '')
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.lat.inits([], [], {}), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), '')
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.lat.inits(['u0'], ['x_1'], {'t_{0,1}': 1}), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), LAT_TV2)

	def test_vectors(self):
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.lat.vectors(None, None, None), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), LAT_VEC3)
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.lat.vectors([], [], []), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), LAT_VEC3)
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.lat.vectors(['u1'], ['x1', 'x2'], ['y1', 'y2', 'y3']), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), LAT_VEC4)

	def test_adds(self):
		self.assertEqual(self.lat.adds(), Err.NOOP)


def main():
	unittest.main()


if __name__ == '__main__':
	main()

# end.
