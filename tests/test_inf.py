# -*- coding: utf-8 -*-
"""
	**test_inf.py**
	unit tests for *src/inf.py*

	in the module:
	* *class* **TestInf**

	Copyright (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
"""
# pylint: disable=missing-docstring

import unittest
from io import StringIO
from freezegun import freeze_time  # https://github.com/spulec/freezegun
import mock

import phoebe.inf
from tests.answers.ans_inf import INF_ANS, INF_COPY, INF_DESC, INF_VERS


class TestInf(unittest.TestCase):
	""" class for testing *Inf* """

	def setUp(self):
		self.inf = phoebe.inf.Inf()

	def tearDown(self):
		pass

	def test_get_description(self):
		# print(self.inf.get_description())
		self.assertEqual(self.inf.get_description(), INF_DESC)

	def test_get_copyright(self):
		print(self.inf.get_copyright())
		self.assertEqual(self.inf.get_copyright(), INF_COPY)

	def test_get_version(self):
		# print(self.inf.get_version())
		self.assertEqual(self.inf.get_version(), INF_VERS)

	@freeze_time("2017-12-03 19:55:02")
	def test_self_test(self):
		phoebe.inf.self_test()
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			phoebe.inf.self_test()
			self.assertEqual(mock_stdout.getvalue(), INF_ANS)

	# coś jest tu nie tak ze strefami czasowmi
	@freeze_time("2017-12-03 19:55:02")
	def test_get_time(self):
		self.assertEqual(self.inf.get_time(), '2017-12-03 20:55:02 ')


def main():
	unittest.main()


if __name__ == '__main__':
	main()

# end.
