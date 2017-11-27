# -*- coding: utf-8 -*-
"""
	**test_yml.py**
	unit tests for *src/yml.py*

	in the module:
	* *class* **TestYml**

	Copyright 2015--2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl
"""
import os
import unittest
from StringIO import StringIO
import mock
import yaml
import phoebe.yml


class TestYml(unittest.TestCase):
	""" class for testing *Config* """
	def setUp(self):
		self.yml = phoebe.yml.Yml()
		self.cont1 = {'output': ['y_1']}
		self.cont2 = 'output: [y_1]\n'

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

	def test_parse_key(self):
		""" test method for *parse_key* """
		self.assertEqual(self.yml.parse_key(self.cont1, 'output', None), ['y_1'])
		self.assertEqual(self.yml.parse_key(self.cont1, 'log_', None), None)
		self.assertEqual(self.yml.parse_key(self.cont1, None, None), None)
		self.assertEqual(self.yml.parse_key(None, None, None), None)


if __name__ == "__main__":
	unittest.main()

# end.
