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
# import phoebe.cli
from tests.answers.ans_cli import ANS_HLP, ANS_FILE

# pylint: disable=missing-docstring
# https://click.palletsprojects.com/en/7.x/testing/
# https://stackoverflow.com/questions/53203500/unittest-for-click-module


class TestCli(unittest.TestCase):
	""" class for testing *Generator* """

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_cli_help(self):
		lib_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../phoebe')
		if lib_path not in sys.path:
			sys.path.append(lib_path)
		import phoebe.cli

		runner = CliRunner()
		result = runner.invoke(phoebe.cli.cli, ['-h'])
		self.assertEqual(result.exit_code, 0)
		# print(result.output)
		self.assertEqual(result.output, ANS_HLP)

	def test_cli_show_file(self):
		lib_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../phoebe')
		if lib_path not in sys.path:
			sys.path.append(lib_path)
		import phoebe.cli

		runner = CliRunner()
		result = runner.invoke(phoebe.cli.cli, ['--showfile'])
		self.assertEqual(result.exit_code, 2)
		result = runner.invoke(phoebe.cli.cli, ['--showfile', 'tests/samples/cli1.yml'])
		self.assertEqual(result.exit_code, 0)
		# print(result.output)
		self.assertEqual(result.output, ANS_FILE)


def main():
	unittest.main()


if __name__ == '__main__':
	main()

# end.
