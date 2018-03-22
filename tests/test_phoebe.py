# -*- coding: utf-8 -*-
"""
	**test_parser.py**
	unit tests for *src/phoebe.py*

	in the module:
	* *class* **TestPhoebe**

	Copyright (c) 2017-2018 Jarosław Stańczyk <jaroslaw.stanczyk@upwr.edu.pl>
"""
import os
from StringIO import StringIO
import unittest
import mock
import phoebe.err
import phoebe.worker
from answers import ANS_F7_DET1, ANS_F7_DET3


class TestPhoebe(unittest.TestCase):
	""" class for testing *Phoebe main* """
	def setUp(self):
		self.work = phoebe.worker.Worker()
		self.args = {
			'--det1': False,
			'--det2': False,
			'--det3': False,
			'--file': False,
			'--help': False,
			'--vectors': False,
			'--version': False,
			'--latex': False,
			'--no-desc': False,
			'-h': False,
			'-v': False,
			'<desc_file>': None
		}

	def tearDown(self):
		pass

	@mock.patch('phoebe.parser.docopt.docopt')
	def test_phoebe_mat6(self, mock_docopt):
		args = self.args
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f6.yml'
		mock_docopt.return_value = args
		with self.assertRaises(SystemExit) as system_exit:
			self.work.main()
		self.assertEqual(system_exit.exception.code, phoebe.err.Err.NOOP)

	@mock.patch('phoebe.parser.docopt.docopt')
	def test_phoebe_lat6(self, mock_docopt):
		args = self.args
		args['--latex'] = True
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f6.yml'
		mock_docopt.return_value = args
		with self.assertRaises(SystemExit) as system_exit:
			self.work.main()
		self.assertEqual(system_exit.exception.code, phoebe.err.Err.NOOP)

	@mock.patch('phoebe.parser.docopt.docopt')
	def test_phoebe_f7_det1(self, mock_docopt):
		args = self.args
		args['--det1'] = True
		args['--no-desc'] = True
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f7.yml'
		mock_docopt.return_value = args
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			with self.assertRaises(SystemExit) as system_exit:
				self.work.main()
		self.assertEqual(system_exit.exception.code, phoebe.err.Err.NOOP)
		self.assertEqual(mock_stdout.getvalue(), ANS_F7_DET1)

	@mock.patch('phoebe.parser.docopt.docopt')
	def test_phoebe_f7_det3(self, mock_docopt):
		args = self.args
		args['--det3'] = True
		args['--no-desc'] = True
		args['<desc_file>'] = os.getcwd() + '/tests/samples/f7.yml'
		mock_docopt.return_value = args
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			with self.assertRaises(SystemExit) as system_exit:
				self.work.main()
		self.assertEqual(system_exit.exception.code, phoebe.err.Err.NOOP)
		self.assertEqual(mock_stdout.getvalue(), ANS_F7_DET3)


def main():
	unittest.main()


if __name__ == '__main__':
	main()

# end.
