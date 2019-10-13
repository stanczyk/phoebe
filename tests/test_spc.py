# -*- coding: utf-8 -*-
"""
	**test_spc.py**
	tests of specs/descriptons

	in the module:
	* *class* **TestSpc**

	Copyright (c) 2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
"""
import glob
import os
import sys
import unittest
from builtins import staticmethod
from freezegun import freeze_time  # https://github.com/spulec/freezegun
from click.testing import CliRunner

lib_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../phoebe')
if lib_path not in sys.path:
	sys.path.append(lib_path)
import phoebe.cli
from phoebe.err import Err


class TestSpc(unittest.TestCase):
	""" class for testing *Generator* """

	def setUp(self):
		self.runner = CliRunner()

	def tearDown(self):
		pass

	@staticmethod
	def check_file(file, content):
		if not os.path.isfile(file):
			writer = open(file, 'w')
			writer.write(content)
			writer.close()

	@freeze_time("2019-10-13 15:46:20")
	def test_specs(self):
		for file in glob.glob('specs/desc*.yml'):
			base = os.path.basename(os.path.splitext(file)[0])
			# print(base)
			# matlab
			result = self.runner.invoke(phoebe.cli.cli, [file, 'matlab'])
			self.assertEqual(result.exit_code, Err.NOOP)
			# print(result.output)
			file_path = 'tests/answers/matlab/' + base + '.m'
			self.check_file(file_path, result.output)
			with open(file_path) as reader:
				self.assertEqual(result.output, reader.read())
			# latex
			result = self.runner.invoke(phoebe.cli.cli, [file, 'latex'])
			self.assertEqual(result.exit_code, Err.NOOP)
			# print(result.output)
			file_path = 'tests/answers/latex/' + base + '.tex'
			self.check_file(file_path, result.output)
			with open(file_path) as reader:
				self.assertEqual(result.output, reader.read())


def main():
	unittest.main()


if __name__ == '__main__':
	main()

# end.
