# -*- coding: utf-8 -*-
"""
	**test_yml.py**
	unit tests for *src/yml.py*

	in the module:
	* *class* **TestYml**

	Copyright 2015--2018 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl
"""
import os
import unittest
from StringIO import StringIO
import mock
import yaml
import phoebe.yml
from answers import YML_ANS


class TestYml(unittest.TestCase):
	""" class for testing *Config* """
	def setUp(self):
		self.yml = phoebe.yml.Yml()
		self.cont1 = {'output': [{'y_1': {}}]}
		self.cont2 = 'output:\n- y_1: {}\n'

	def tearDown(self):
		pass

	def test_load(self):
		""" test method for *load* """
		# pylint: disable=redundant-unittest-assert
		# empty file - OK
		file_name = os.getcwd() + '/tests/samples/f1.yml'
		with open(file_name, 'r') as tmp:
			content = self.yml.load(tmp)
		self.assertEqual(content, None)
		# proper file - OK
		file_name = os.getcwd() + '/tests/samples/f2.yml'
		with open(file_name, 'r') as tmp:
			content = self.yml.load(tmp)
		self.assertEqual(content, self.cont1)
		# not yaml file - error
		file_name = os.getcwd() + '/tests/samples/f3.yml'
		with open(file_name, 'r') as tmp:
			try:
				self.yml.load(tmp)
			except yaml.YAMLError:
				self.assertTrue(True)
				return
		self.assertTrue(False)

	def test_dump(self):
		""" test method for *dump* """
		content = self.yml.dump(self.cont1)
		self.assertEqual(content, self.cont2)

	def test_show(self):
		""" test method for *show* """
		file_name = os.getcwd() + '/tests/samples/f2.yml'
		with open(file_name, 'r') as tmp:
			content = self.yml.load(tmp)
		with mock.patch('sys.stdout', new=StringIO()) as fake_stdout:
			print self.yml.show(content)
			self.assertEqual(fake_stdout.getvalue(), self.cont2 + '\n')

	def test_get_value(self):
		""" test method for *get_value* """
		self.assertEqual(self.yml.get_value(self.cont1, 'output', None), [{'y_1': {}}])
		self.assertEqual(self.yml.get_value(self.cont1, 'log_', None), None)
		self.assertEqual(self.yml.get_value(self.cont1, None, None), None)
		self.assertEqual(self.yml.get_value(None, None, None), None)
		self.assertEqual(self.yml.get_value(None, None, 'ala'), 'ala')
		self.assertEqual(self.yml.get_value({}, 'log_', None), None)

	def test_get_key(self):
		""" test method for *get_key* """
		self.assertEqual(self.yml.get_key(self.cont1), 'output')
		self.assertEqual(self.yml.get_key(self.yml.get_value(self.cont1, 'output')[0]), 'y_1')
		self.assertEqual(self.yml.get_key(None), None)
		self.assertEqual(self.yml.get_key(None, 'ala'), 'ala')

	def test_get_len(self):
		""" test method for *get_len* """
		self.assertEqual(self.yml.get_len(self.cont1), 1)
		self.assertEqual(self.yml.get_len('ala ma asa'), 10)
		self.assertEqual(self.yml.get_len(''), -1)
		self.assertEqual(self.yml.get_len(None), -1)

	def test_get_matrix_size(self):
		""" test method for *get_matrix_size* """
		self.assertEqual(self.yml.get_matrix_size(None), (None, None))
		self.assertEqual(self.yml.get_matrix_size([]), (None, None))
		self.assertEqual(self.yml.get_matrix_size(['123']), (1, 3))
		self.assertEqual(self.yml.get_matrix_size([['-', '-', ['d_3', 't_{3,4}']]]), (1, 3))
		self.assertEqual(
			self.yml.get_matrix_size([[['d_1'], '-', '-'], ['-', ['d_2'], '-'], ['-', '-', ['d_3']]]), (3, 3)
		)

	def test_self_test(self):
		""" test method for *self_test* """
		with mock.patch('sys.stdout', new=StringIO()) as fake_stdout:
			phoebe.yml.self_test()
			self.assertEqual(fake_stdout.getvalue(), YML_ANS)


if __name__ == "__main__":
	unittest.main()

# end.
