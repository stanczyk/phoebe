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
# from io import StringIO
# import mock
from click.testing import CliRunner
from tests.answers.ans_cli import ANS_HLP1, ANS_HLP2, ANS_FILE, ANS_VEC1, ANS_VEC2, \
	ANS_DET1_1, ANS_DET1_2, ANS_DET2_1, ANS_DET2_2, ANS_DET3_1, ANS_DET3_2, ANS_MAT1, ANS_MAT2

lib_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../phoebe')
if lib_path not in sys.path:
	sys.path.append(lib_path)
import phoebe.lat


class TestLat(unittest.TestCase):
	""" class for testing *Generator* """

	def setUp(self):
		pass

	def tearDown(self):
		pass

	@unittest.skip("not implemented yet")
	def test_begin(self):
		pass

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
