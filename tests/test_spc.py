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
# from io import StringIO
# import mock
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

	@freeze_time("2019-10-13 15:46:20")
	def test_specs(self):
		for file in glob.glob('specs/desc*.yml'):
			base = os.path.basename(os.path.splitext(file)[0])
			print(base)
			result1 = self.runner.invoke(phoebe.cli.cli, [file, 'matlab'])
			self.assertEqual(result1.exit_code, Err.NOOP)
			# print(result1.output)
			with open('tests/answers/matlab/' + base + '.m') as base_reader1:
				self.assertEqual(result1.output, base_reader1.read())
			result2 = self.runner.invoke(phoebe.cli.cli, [file, 'latex'])
			self.assertEqual(result2.exit_code, Err.NOOP)
			# print(result2.output)
			with open('tests/answers/latex/' + base + '.tex') as base_reader2:
				self.assertEqual(result2.output, base_reader2.read())


def main():
	unittest.main()


if __name__ == '__main__':
	main()

# end.
