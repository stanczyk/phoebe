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
from tests.answers.ans_mat import MAT_BEGIN, MAT_EQUEST1

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
	def test_begin(self):
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.mat.begin('nazwa-pliku'), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), MAT_BEGIN)

	def test_do_matrices(self):
		matrix = []

	# def test_equation(self):
		# 	mat_A = [['a_0'], ['a_1'], [], ['a_3']]
		# mat_B = [[], ['b_1']]
		# mat_C = ['c']
		# mat_D = ['d']
		# with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			# 	self.assertEqual(self.mat.equation(mat_A, mat_B, mat_C, mat_D), Err.NOOP)
			# self.assertEqual(mock_stdout.getvalue(), MAT_EQUEST1)

	@unittest.skip("not implemented yet")
	def test_equation(self):
		pass

	@unittest.skip("not implemented yet")
	def test_clean_value(self):
		pass

	@unittest.skip("not implemented yet")
	def test_values(self):
		pass

	@unittest.skip("not implemented yet")
	def test_vector(self):
		pass

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

	@unittest.skip("not implemented yet")
	def test_end(self):
		pass


def main():
	unittest.main()


if __name__ == '__main__':
	main()

# end.
