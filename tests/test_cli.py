# -*- coding: utf-8 -*-
"""
	**test_cli.py**
	unit tests for *src/cli.py*

	in the module:
	* *class* **TestCli**

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
import phoebe.cli
from phoebe.err import Err

# pylint: disable=missing-docstring
# https://click.palletsprojects.com/en/7.x/testing/
# https://stackoverflow.com/questions/53203500/unittest-for-click-module


class TestCli(unittest.TestCase):
	""" class for testing *Generator* """

	def setUp(self):
		self.runner = CliRunner()

	def tearDown(self):
		pass

	def test_help(self):
		result = self.runner.invoke(phoebe.cli.cli, ['-h'])
		self.assertEqual(result.exit_code, Err.NOOP)
		# print(result.output)
		self.assertEqual(result.output, ANS_HLP1)

	def test_cli_showfile(self):
		result = self.runner.invoke(phoebe.cli.cli, ['--showfile'])
		self.assertEqual(result.exit_code, 2) 	# Error: Missing argument "FILENAME".
		# print(result.output)
		self.assertEqual(result.output, ANS_HLP2)
		result = self.runner.invoke(phoebe.cli.cli, ['--showfile', 'tests/samples/cli1.yml'])
		self.assertEqual(result.exit_code, 0)
		# print(result.output)
		self.assertEqual(result.output, ANS_FILE)

	def test_cli_det1(self):
		self.maxDiff = None
		result = self.runner.invoke(phoebe.cli.cli, ['--det1', 'tests/samples/cli1.yml'])
		self.assertEqual(result.exit_code, Err.NOOP)
		print(result.output)
		self.assertEqual(result.output, ANS_DET1_1)
		result = self.runner.invoke(phoebe.cli.cli, ['--det1', 'tests/samples/cli2.yml'])
		self.assertEqual(result.exit_code, Err.NOOP)
		print(result.output)
		self.assertEqual(result.output, ANS_DET1_2)

	def test_cli_det2(self):
		result = self.runner.invoke(phoebe.cli.cli, ['--det2', 'tests/samples/cli1.yml'])
		self.assertEqual(result.exit_code, Err.NOOP)
		# print(result.output)
		self.assertEqual(result.output, ANS_DET2_1)
		result = self.runner.invoke(phoebe.cli.cli, ['--det2', 'tests/samples/cli2.yml'])
		self.assertEqual(result.exit_code, Err.NOOP)
		# print(result.output)
		self.assertEqual(result.output, ANS_DET2_2)

	def test_cli_det3(self):
		result = self.runner.invoke(phoebe.cli.cli, ['--det3', 'tests/samples/cli1.yml'])
		self.assertEqual(result.exit_code, Err.NOOP)
		# print(result.output)
		self.assertEqual(result.output, ANS_DET3_1)
		result = self.runner.invoke(phoebe.cli.cli, ['--det3', 'tests/samples/cli2.yml'])
		self.assertEqual(result.exit_code, Err.NOOP)
		# print(result.output)
		self.assertEqual(result.output, ANS_DET3_2)

	def test_cli_vectors(self):
		result = self.runner.invoke(phoebe.cli.cli, ['--vectors'])
		self.assertEqual(result.exit_code, 2) 	# Error: Missing argument "FILENAME".
		result = self.runner.invoke(phoebe.cli.cli, ['--vectors', 'tests/samples/cli1.yml'])
		self.assertEqual(result.exit_code, Err.NOOP)
		# print(result.output)
		self.assertEqual(result.output, ANS_VEC1)
		result = self.runner.invoke(phoebe.cli.cli, ['--vectors', 'tests/samples/cli2.yml'])
		self.assertEqual(result.exit_code, Err.NOOP)
		# print(result.output)
		self.assertEqual(result.output, ANS_VEC2)

	def test_cli_matrices(self):
		result = self.runner.invoke(phoebe.cli.cli, ['--matrices', 'tests/samples/cli1.yml'])
		self.assertEqual(result.exit_code, Err.NOOP)
		# print(result.output)
		self.assertEqual(result.output, ANS_MAT1)
		result = self.runner.invoke(phoebe.cli.cli, ['--matrices', 'tests/samples/cli2.yml'])
		self.assertEqual(result.exit_code, Err.NOOP)
		# print(result.output)
		self.assertEqual(result.output, ANS_MAT2)

	@unittest.skip("not implemented yet")
	def test_latex(self):
		pass

	@unittest.skip("not implemented yet")
	def test_matlab(self):
		pass


def main():
	unittest.main()


if __name__ == '__main__':
	main()

# end.
