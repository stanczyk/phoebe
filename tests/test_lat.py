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
from tests.answers.ans_lat import LAT_HEADER, LAT_PREFACE, LAT_END

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
	def test_time_values(self):
		pass

	def test_end(self):
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.assertEqual(self.lat.end(), Err.NOOP)
			self.assertEqual(mock_stdout.getvalue(), LAT_END)

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
