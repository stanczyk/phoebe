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
from tests.answers.ans_lat import LAT_BEGIN, LAT_EQUEST1

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
	def test_begin(self):
		print(self.lat.begin('nazwa-pliku'))
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.lat.begin('nazwa-pliku'), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), LAT_BEGIN)


	def test_do_matrices(self):
		matrix = []


	# def test_equation(self):
		# 	mat_A = [['a_0'], ['a_1'], [], ['a_3']]
		# mat_B = [['b_0']]
		# mat_C = [[], ['c_1']]
		# mat_D = [[], ['d_1']]
		# with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			# 	self.assertEqual(self.lat.equation(mat_A, mat_B, mat_C, mat_D), Err.NOOP)
			# self.assertEqual(mock_stdout.getvalue(), LAT_EQUEST1)

	@unittest.skip("not implemented yet")
	def test_equation(self):
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
	def test_values(self):
		pass

	@unittest.skip("not implemented yet")
	def test_end(self):
		pass


def main():
	unittest.main()


if __name__ == '__main__':
	main()

# end.
