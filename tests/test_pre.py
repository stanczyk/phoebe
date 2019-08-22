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
from tests.answers.ans_pre import ANS_FILE
# pylint: disable=missing-docstring


class TestPre(unittest.TestCase):
	""" class for testing *Generator* """
	def setUp(self):
		lib_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../phoebe')
		if lib_path not in sys.path:
			sys.path.append(lib_path)
		import phoebe.pre
		self.preparer = phoebe.pre.Preparer()
		import phoebe.err
		self.error = phoebe.err.Err()

	def tearDown(self):
		pass

	def test_set_file_handler(self):
		# no filename
		self.assertEqual(self.preparer.set_file_handler(None), self.error.ERR_NO_INPUT_FILE)
		self.assertEqual(self.preparer.set_file_handler(''), self.error.ERR_NO_INPUT_FILE)
		# wrong filename
		self.assertEqual(self.preparer.set_file_handler(' '), self.error.ERR_NO_FILE)
		self.assertEqual(self.preparer.set_file_handler('./tests/samples/not_existing_file'), self.error.ERR_NO_FILE)
		# no rights to read file
		os.chmod('./tests/samples/pre1.yml', 0o006)
		self.assertEqual(self.preparer.set_file_handler('./tests/samples/pre1.yml'), self.error.ERR_NO_PERMISSION)
		# normal file
		os.chmod('./tests/samples/pre1.yml', 0o666)
		self.assertEqual(self.preparer.set_file_handler('./tests/samples/pre1.yml'), self.error.NOOP)

	def test_read_file(self):
		# normal file
		self.preparer.set_file_handler('./tests/samples/pre2.yml')
		self.assertEqual(self.preparer.read_file(), self.error.NOOP)
		# wrong yaml file
		self.preparer.set_file_handler('./tests/samples/pre3.yml')
		self.assertEqual(self.preparer.read_file(), self.error.ERR_YAML)

	def test_show_file_content(self):
		self.preparer.set_file_handler('./tests/samples/pre2.yml')
		self.preparer.read_file()
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.preparer.show_file_content('tests/samples/pre2.yml')
			self.assertEqual(mock_stdout.getvalue(), ANS_FILE)


def main():
	unittest.main()


if __name__ == '__main__':
	main()

# end.
