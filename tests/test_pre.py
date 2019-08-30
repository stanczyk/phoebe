# -*- coding: utf-8 -*-
"""
	**test_pre.py**
	unit tests for *src/pre.py*

	in the module:
	* *class* **TestPre**

	Copyright (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
"""
import os
import sys
import unittest
from io import StringIO
import mock
from tests.answers.ans_pre import ANS_FILE, PRE_IMP1, PRE_ANS1, PRE_VEC1, PRE_VEC2

# pylint: disable=missing-docstring
lib_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../phoebe')
if lib_path not in sys.path:
	sys.path.append(lib_path)
import phoebe.pre
from phoebe.err import Err


class TestPre(unittest.TestCase):
	""" class for testing *Generator* """
	def setUp(self):
		self.pre = phoebe.pre.Preparer()

	def tearDown(self):
		pass

	def test_set_file_handler(self):
		# no filename
		self.assertEqual(self.pre.set_file_handler(None), Err.ERR_NO_INPUT_FILE)
		self.assertEqual(self.pre.set_file_handler(''), Err.ERR_NO_INPUT_FILE)
		# wrong filename
		self.assertEqual(self.pre.set_file_handler(' '), Err.ERR_NO_FILE)
		self.assertEqual(self.pre.set_file_handler('./tests/samples/not_existing_file'), Err.ERR_NO_FILE)
		# no rights to read file
		os.chmod('./tests/samples/pre1.yml', 0o006)
		self.assertEqual(self.pre.set_file_handler('./tests/samples/pre1.yml'), Err.ERR_NO_PERMISSION)
		# normal file
		os.chmod('./tests/samples/pre1.yml', 0o666)
		self.assertEqual(self.pre.set_file_handler('./tests/samples/pre1.yml'), Err.NOOP)

	def test_read_file(self):
		# normal file
		self.pre.set_file_handler('./tests/samples/pre2.yml')
		self.assertEqual(self.pre.read_file(), Err.NOOP)
		# wrong yaml file
		self.pre.set_file_handler('./tests/samples/pre3.yml')
		self.assertEqual(self.pre.read_file(), Err.ERR_YAML)

	def test_show_file_content(self):
		self.pre.set_file_handler('./tests/samples/pre2.yml')
		self.pre.read_file()
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.pre.show_file_content('tests/samples/pre2.yml')
			self.assertEqual(mock_stdout.getvalue(), ANS_FILE)

	def test_prepare_vectors(self):
		self.assertEqual(self.pre.prepare_vectors(), Err.NOOP)

	def test_prepare_vector(self):
		selector = 'prod-unit'
		vector = []
		name = 'x_'
		self.pre.content_yaml = None
		self.assertEqual(self.pre.prepare_vector(selector, vector, name), Err.NOOP)
		self.assertEqual(vector, [])
		self.pre.content_yaml = PRE_IMP1
		self.assertEqual(self.pre.prepare_vector(selector, vector, name), Err.NOOP)
		self.assertEqual(vector, PRE_ANS1)

	def test_show_vectors(self):
		self.pre.content_yaml = None
		self.pre.prepare_vectors()
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.pre.show_vectors()
			self.assertEqual(mock_stdout.getvalue(), PRE_VEC1)
		self.pre.content_yaml = PRE_IMP1
		self.pre.prepare_vectors()
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.pre.show_vectors()
			self.assertEqual(mock_stdout.getvalue(), PRE_VEC2)

	def test_print_vector(self):
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.pre.print_vector('x(k)', [])
			self.assertEqual(mock_stdout.getvalue(), 'x(k) = []\n')
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.pre.print_vector('x(k)', ['x_1', 'x_2', 'x_3'])
			self.assertEqual(mock_stdout.getvalue(), 'x(k) = [ x_1(k) x_2(k) x_3(k) ]\'\n')

	@unittest.skip("not implemented yet")
	def test_add_defaults(self):
		pass

	@unittest.skip("not implemented yet")
	def test_get_det1(self):
		pass

	@unittest.skip("not implemented yet")
	def test_get_det2(self):
		pass

	@unittest.skip("not implemented yet")
	def test_show_det1(self):
		pass

	@unittest.skip("not implemented yet")
	def test_show_det2(self):
		pass

	@unittest.skip("not implemented yet")
	def test_show_matrices(self):
		pass

	@unittest.skip("not implemented yet")
	def test_prn_matrix(self):
		pass

	@unittest.skip("not implemented yet")
	def test_prepare_mapping(self):
		pass

	@unittest.skip("not implemented yet")
	def test_matrix_preparation(self):
		pass

	@unittest.skip("not implemented yet")
	def test_create_matrix(self):
		pass

	@unittest.skip("not implemented yet")
	def test_fill_matrix(self):
		pass

	@unittest.skip("not implemented yet")
	def test_fill_(self):
		pass

	@unittest.skip("not implemented yet")
	def test_optimize_matrix(self):
		pass

	@unittest.skip("not implemented yet")
	def test_rm_repeated_zeros(self):
		pass

	@unittest.skip("not implemented yet")
	def test_rm_redundant_zeros(self):
		pass

	@unittest.skip("not implemented yet")
	def test_add_feedback_x(self):
		pass

	@unittest.skip("not implemented yet")
	def test_add_feedback_u(self):
		pass

	@unittest.skip("not implemented yet")
	def test_get_det3(self):
		pass

	@unittest.skip("not implemented yet")
	def test_show_det3(self):
		pass


def main():
	unittest.main()


if __name__ == '__main__':
	main()

# end.
