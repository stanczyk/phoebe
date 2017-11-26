# -*- coding: utf-8 -*-
"""
	**test_config.py**
	unit tests for *battleship/config.py*

	in the module:

	* *class* **TestConfig**

	Copyright 2015--2016 Jarek Stanczyk, e-mail: j.stanczyk@hotmail.com
"""
import os
import unittest
import mock
from StringIO import StringIO
from battleship.yml import Yml


class TestYml(unittest.TestCase):
	""" class for testing *Config* """
	def setUp(self):
		self.yml = Yml()
		self.content = {
			'log_console_level': 'CRITICAL',
			'log_use_color': True,
		}

	def tearDown(self):
		pass

	def test_load(self):
		""" test method for *load* """
		file_name = os.getcwd() + '/tests/dir_test/config1.cfg'
		with open(file_name, 'r') as tmp_file:
			content = self.yml.load(tmp_file)
		self.assertEqual(content, None)
		file_name = os.getcwd() + '/tests/dir_test/config2.cfg'
		with open(file_name, 'r') as tmp_file:
			content = self.yml.load(tmp_file)
		self.assertEqual(content, self.content)

	def test_dump(self):
		""" test method for *dump* """
		content = self.yml.dump(self.content)
		self.assertEqual(content, '{log_console_level: CRITICAL, log_use_color: true}\n')

	def test_show(self):
		""" test method for *show* """
		cont = '{log_console_level: CRITICAL, log_use_color: true}\n\n'
		file_name = os.getcwd() + '/tests/dir_test/config2.cfg'
		with open(file_name, 'r') as tmp_file:
			content = self.yml.load(tmp_file)
		with mock.patch('sys.stdout', new=StringIO()) as fake_stdout:
			print self.yml.show(content)
			self.assertEqual(fake_stdout.getvalue(), cont)

	def test_parse_key(self):
		""" test method for *parse_key* """
		self.assertEqual(self.yml.parse_key(self.content, 'log_console_level', None), 'CRITICAL')
		self.assertEqual(self.yml.parse_key(self.content, 'log_', None), None)
		self.assertEqual(self.yml.parse_key(self.content, None, None), None)
		self.assertEqual(self.yml.parse_key(None, None, None), None)


if __name__ == "__main__":
	unittest.main()

# end.
