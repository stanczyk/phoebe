# -*- coding: utf-8 -*-
"""
	**test_mat.py**
	unit tests for *src/mat.py*

	in the module:
	* *class* **TestMat**

	Copyright (c) 2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
"""
import os
import sys
import unittest
from freezegun import freeze_time  # https://github.com/spulec/freezegun
from io import StringIO
import mock
from tests.answers.ans_mat import MAT_HEADER, MAT_PREFACE, MAT_END, MAT_EQ1, MAT_EQ2, MAT_EQ3

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
			self.assertEqual(self.mat.equation([['a0'],['a1'], None, [], ['a4']], [['b0']], ['c'], ['d']), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), MAT_EQ3)

	@unittest.skip("not implemented yet")
	def test_clean_value(self):
		pass

	@unittest.skip("not implemented yet")
	def test_time_values(self):
		pass

	def test_vector(self):
		self.assertEqual(self.mat.vector(None, None), Err.ERR_NO_NAME)
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.vector('a', None), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), 'disp(\'a(k) = [ ]\');\n')
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.vector('b', ['b1', 'b_2', 'b_{3}']), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), 'disp(\'b(k) = [ b1(k); b_2(k); b_{3}(k); ]\');\n')

	@unittest.skip("not implemented yet")
	def test_get_matrix_value(self):
		pass

	@unittest.skip("not implemented yet")
	def test_matrix_desc(self):
		pass

	@unittest.skip("not implemented yet")
	def test_matrix(self):
		pass

	@unittest.skip("not implemented yet")
	def test_input_vec(self):
		pass

	@unittest.skip("not implemented yet")
	def test_start_vec(self):
		pass

	@unittest.skip("not implemented yet")
	def test_adds(self):
		pass

	def test_end(self):
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.end(), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), MAT_END)

	@unittest.skip("not implemented yet")
	def test_inits(self):
		pass

	@unittest.skip("not implemented yet")
	def test_vectors(self):
		pass


def main():
	unittest.main()


if __name__ == '__main__':
	main()

# end.
