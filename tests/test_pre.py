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
from tests.answers.ans_pre import ANS_FILE, PRE_IMP1, PRE_ANS1, PRE_VEC1, PRE_VEC2, PRE_CONTENT1, PRE_CONTENT2, \
	PRE_DET1_1, PRE_DET1_2, PRE_DET2_1, PRE_DET2_2, PRE_MAT1, PRE_MATA, PRE_MATB, PRE_MATC, PRE_MATD, PRE_MAT2, \
	PRE_MATB2, PRE_MAP1, PRE_MAP2, PRE_DICM, PRE_DICM2, PRE_A01, PRE_A02, PRE_A03, PRE_DET31, PRE_DET32

# pylint: disable=missing-docstring
lib_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../phoebe')
if lib_path not in sys.path:
	sys.path.append(lib_path)
import phoebe.pre
from phoebe.err import Err


class TestPre(unittest.TestCase):
	""" class for testing *Generator* """
	def setUp(self):
		self.pre = phoebe.pre.Preparer()

	def tearDown(self):
		pass

	def test_set_file_handler(self):
		# no filename
		self.assertEqual(self.pre.set_file_handler(None), Err.ERR_NO_INPUT_FILE)
		self.assertEqual(self.pre.set_file_handler(''), Err.ERR_NO_INPUT_FILE)
		# wrong filename
		self.assertEqual(self.pre.set_file_handler(' '), Err.ERR_NO_FILE)
		self.assertEqual(self.pre.set_file_handler('./tests/samples/not_existing_file'), Err.ERR_NO_FILE)
		# no rights to read file
		os.chmod('./tests/samples/pre1.yml', 0o006)
		self.assertEqual(self.pre.set_file_handler('./tests/samples/pre1.yml'), Err.ERR_NO_PERMISSION)
		# normal file
		os.chmod('./tests/samples/pre1.yml', 0o666)
		self.assertEqual(self.pre.set_file_handler('./tests/samples/pre1.yml'), Err.NOOP)

	def test_read_file(self):
		# normal file
		self.pre.set_file_handler('tests/samples/pre2.yml')
		self.assertEqual(self.pre.read_file(), Err.NOOP)
		# wrong yaml file
		self.pre.set_file_handler('tests/samples/pre3.yml')
		self.assertEqual(self.pre.read_file(), Err.ERR_YAML)

	def test_show_file_content(self):
		self.pre.set_file_handler('tests/samples/pre2.yml')
		self.pre.read_file()
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.pre.show_file_content()
			self.assertEqual(mock_stdout.getvalue(), ANS_FILE)

	def test_prepare_vectors(self):
		self.assertEqual(self.pre.prepare_vectors(), Err.NOOP)

	def test_prepare_vector(self):
		selector = 'prod-unit'
		vector = []
		name = 'x_'
		self.pre.content_yaml = None
		self.assertEqual(self.pre.prepare_vector(selector, vector, name), Err.NOOP)
		self.assertEqual(vector, [])
		self.pre.content_yaml = PRE_IMP1
		self.assertEqual(self.pre.prepare_vector(selector, vector, name), Err.NOOP)
		self.assertEqual(vector, PRE_ANS1)

	def test_show_vectors(self):
		self.pre.content_yaml = None
		self.pre.prepare_vectors()
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.pre.show_vectors()
			self.assertEqual(mock_stdout.getvalue(), PRE_VEC1)
		self.pre.content_yaml = PRE_IMP1
		self.pre.prepare_vectors()
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.pre.show_vectors()
			self.assertEqual(mock_stdout.getvalue(), PRE_VEC2)

	def test_print_vector(self):
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.pre.print_vector('x(k)', [])
			self.assertEqual(mock_stdout.getvalue(), 'x(k) = []\n')
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.pre.print_vector('x(k)', ['x_1', 'x_2', 'x_3'])
			self.assertEqual(mock_stdout.getvalue(), 'x(k) = [ x_1(k) x_2(k) x_3(k) ]\'\n')

	def test_add_defaults(self):
		self.pre.content_yaml = PRE_IMP1
		self.pre.add_defaults()
		self.assertEqual(self.pre.content_yaml, PRE_CONTENT2)
		self.pre.content_yaml = PRE_CONTENT1
		self.pre.add_defaults()
		self.assertEqual(self.pre.content_yaml, PRE_CONTENT1)

	def test_get_det1(self):
		op_time, connect = self.pre.get_det1({})
		self.assertIsNone(op_time)
		self.assertIsNone(connect)
		dic = {'connect': 'y', 'op-time': 'd_3', 'tr-time': 't_{3,4}'}
		op_time, connect = self.pre.get_det1(dic)
		self.assertEqual(op_time, 'd_3')
		self.assertEqual(connect, 'y')
		dic = {'connect': {'M_3': {'tr-time': 't_{1,3}', 'buffers': '-'}}, 'op-time': 'd_1'}
		op_time, connect = self.pre.get_det1(dic)
		self.assertEqual(op_time, 'd_1')
		self.assertEqual(connect, {'M_3': {'tr-time': 't_{1,3}', 'buffers': '-'}})

	def test_get_det2(self):
		tr_time, buffers = self.pre.get_det2({})
		self.assertIsNone(tr_time)
		self.assertIsNone(buffers)
		tr_time, buffers = self.pre.get_det2({'tr-time': 't_{0,1}', 'buffers': '-'})
		self.assertEqual(tr_time, 't_{0,1}')
		self.assertEqual(buffers, '-')

	def test_show_det1(self):
		self.pre.content_yaml = PRE_CONTENT1
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.pre.show_det1()
			self.assertEqual(mock_stdout.getvalue(), PRE_DET1_1)
		self.pre.content_yaml = PRE_CONTENT2
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.pre.show_det1()
			self.assertEqual(mock_stdout.getvalue(), PRE_DET1_2)

	def test_show_det2(self):
		self.pre.content_yaml = PRE_CONTENT1
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.pre.show_det2()
			self.assertEqual(mock_stdout.getvalue(), PRE_DET2_1)
		self.pre.content_yaml = PRE_CONTENT2
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.pre.show_det2()
			self.assertEqual(mock_stdout.getvalue(), PRE_DET2_2)

	def test_show_matrices(self):
		self.pre.A = [[], []]
		self.pre.B = [[]]
		self.pre.C = []
		self.pre.D = None
		# print(self.pre.show_matrices())
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.pre.show_matrices()
			self.assertEqual(mock_stdout.getvalue(), PRE_MAT1)
		self.pre.A = PRE_MATA
		self.pre.B = PRE_MATB
		self.pre.C = PRE_MATC
		self.pre.D = PRE_MATD
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.pre.show_matrices()
			self.assertEqual(mock_stdout.getvalue(), PRE_MAT2)

	def test_prn_matrix(self):
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.pre.prn_matrix([])
			self.assertEqual(mock_stdout.getvalue(), '[]\n')
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.pre.prn_matrix(PRE_MATB[0])
			self.assertEqual(mock_stdout.getvalue(), PRE_MATB2)

	def test_prepare_mapping(self):
		self.pre.content_yaml = PRE_CONTENT1
		self.pre.prepare_mapping()
		self.assertEqual(self.pre.mapping, {'y_1': 0})
		self.assertEqual(self.pre.values, None)
		self.pre.content_yaml = PRE_CONTENT2
		self.pre.prepare_mapping()
		self.assertEqual(self.pre.mapping, PRE_MAP1)
		self.assertEqual(self.pre.values, PRE_MAP2)

	def test_matrix_preparation(self):
		self.pre.content_yaml = PRE_CONTENT1
		self.pre.matrix_preparation()
		self.assertEqual(self.pre.A, [[], []])
		self.assertEqual(self.pre.B, [[]])
		self.assertEqual(self.pre.C, [])
		self.assertEqual(self.pre.D, [])
		self.pre.content_yaml = PRE_CONTENT2
		self.pre.vector_u = ['u_1', 'u_2']
		self.pre.vector_x = ['x_1', 'x_2', 'x_3']
		self.pre.vector_y = ['y_1']
		self.pre.mapping = PRE_MAP1
		self.pre.matrix_preparation()
		self.assertEqual(self.pre.A, PRE_MATA)
		self.assertEqual(self.pre.B, PRE_MATB)
		self.assertEqual(self.pre.C, PRE_MATC)

	def test_create_matrix(self):
		self.assertEqual(self.pre.create_matrix([], [], []), [])
		vector_u = ['u_1', 'u_2']
		vector_x = ['x_1', 'x_2', 'x_3']
		self.assertEqual(self.pre.create_matrix([], vector_u, vector_x), [['-', '-', '-'], ['-', '-', '-']])

	def test_fill_matrix(self):
		matrix = []
		dic = {}
		self.assertEqual(self.pre.fill_matrix(matrix, dic), [])
		matrix = PRE_A01
		dic = PRE_DICM
		self.pre.A[0] = matrix
		self.pre.mapping = PRE_MAP1
		self.assertEqual(self.pre.fill_matrix(matrix, dic), PRE_A02)

	def test_fill_(self):
		self.pre.A[0] = PRE_A01
		iteration = 0
		con = {'M_3': {'tr-time': 't_{1,3}', 'buffers': '-'}}
		val = ['d_1']
		self.pre.mapping = PRE_MAP1
		self.assertEqual(self.pre.fill_(self.pre.A[0], iteration, con, val), PRE_A03)
		self.pre.A[0] = PRE_A03
		iteration = 1
		con = {'M_3': {'tr-time': 't_{2,3}', 'buffers': '-'}}
		val = ['d_2']
		self.assertEqual(self.pre.fill_(self.pre.A[0], iteration, con, val), PRE_A02)

	def test_optimize_matrix(self):
		self.assertEqual(self.pre.optimize_matrix([]), [])
		self.assertEqual(
			self.pre.optimize_matrix([[['0', 't_{0,1}'], '-'], ['-', ['0', 't_{0,2}']], ['-', '-']]),
			[[['t_{0,1}'], '-'], ['-', ['t_{0,2}']], ['-', '-']])

	def test_rm_repeated_zeros(self):
		self.assertEqual(self.pre.rm_repeated_zeros([]), [])
		self.assertEqual(self.pre.rm_repeated_zeros([[], []]), [[], []])
		self.assertEqual(self.pre.rm_repeated_zeros(
			[
				[['0', '0', '0']]
			]),
			[
				[['0']]
			])
		self.assertEqual(self.pre.rm_repeated_zeros(
			[
				[['0', '0', '0'], '-']
			]),
			[
				[['0'], '-']
			])
		self.assertEqual(self.pre.rm_repeated_zeros(
			[
				[['d_1'], '-', ['0', '0', '0', 't_{0,1}', 'd_3', 't_{3,4}']],
				['-', ['d_2'], ['t_{0,2}', 'd_3', 't_{3,4}', '0', '0', '0']],
				['-', '-', ['d_3']]]),
			[
				[['d_1'], '-', ['0', 't_{0,1}', 'd_3', 't_{3,4}']],
				['-', ['d_2'], ['t_{0,2}', 'd_3', 't_{3,4}', '0']],
				['-', '-', ['d_3']]
			])

	def test_rm_redundant_zeros(self):
		self.assertEqual(self.pre.rm_redundant_zeros([]), [])
		self.assertEqual(self.pre.rm_redundant_zeros([[], []]), [[], []])
		self.assertEqual(self.pre.rm_redundant_zeros(
			[
				[['d_1', '0']]
			]),
			[
				[['d_1']]
			])
		self.assertEqual(self.pre.rm_redundant_zeros(
			[
				[['0', 'd_1', '0']]
			]),
			[
				[['d_1', '0']]
			])
		self.assertEqual(self.pre.rm_redundant_zeros(
			[
				[['0', 'd_1'], '-']
			]),
			[
				[['d_1'], '-']
			])
		self.assertEqual(self.pre.rm_redundant_zeros(
			[
				[['d_1'], '-', ['0', 't_{0,1}', 'd_3', 't_{3,4}']],
				['-', ['d_2'], ['t_{0,2}', 'd_3', 't_{3,4}', '0']],
				['-', '-', ['d_3']]]),
			[
				[['d_1'], '-', ['t_{0,1}', 'd_3', 't_{3,4}']],
				['-', ['d_2'], ['t_{0,2}', 'd_3', 't_{3,4}']],
				['-', '-', ['d_3']]
			])

	def test_add_feedback_x(self):
		matrix = [
			[['d_1'], '-', '-'],
			['-', ['d_2'], '-'],
			['-', '-', ['d_3']]]
		system = [
			{'M_1': {'connect': {'M_3': {'tr-time': 't_{1,3}', 'buffers': '-'}}, 'op-time': 'd_1'}},
			{'M_2': {'connect': {'M_3': {'tr-time': 't_{2,3}', 'buffers': '-'}}, 'op-time': 'd_2'}},
			{'M_3': {'connect': {'y': {'tr-time': 't_{3,4}', 'buffers': '-'}}, 'op-time': 'd_3'}}]
		output = [
			{'y': {}}]
		self.assertEqual(self.pre.add_feedback_x(matrix, system, output), matrix)
		matrix = [
			[['d_1'], '-', '-', '-', '-', '-', '-'],
			['-', ['d_2'], '-', '-', '-', '-', '-'],
			['-', '-', ['d_3'], '-', '-', '-', '-'],
			['-', '-', '-', ['d_4'], '-', '-', '-'],
			['-', '-', '-', '-', ['d_5'], '-', '-'],
			['-', '-', '-', '-', '-', ['d_6'], '-'],
			['-', '-', '-', '-', '-', '-', ['d_7']]]
		system = [
			{'X_1': {'op-time': 'd_1', 'connect':
				{'X_2': {'tr-time': '0', 'buffers': '-'}, 'X_4': {'tr-time': '0', 'buffers': '-'}}}},
			{'X_2': {'op-time': 'd_2', 'connect':
				{'y_1': {'tr-time': '0', 'buffers': '-'}, 'X_5': {'tr-time': '0', 'buffers': '-'}}}},
			{'X_3': {'op-time': 'd_3', 'connect':
				{'X_4': {'tr-time': '0', 'buffers': '-'}, 'X_6': {'tr-time': '0', 'buffers': '-'}}}},
			{'X_4': {'op-time': 'd_4', 'connect':
				{'X_5': {'tr-time': '0', 'buffers': '-'}, 'X_7': {'tr-time': '0', 'buffers': '-'}}}},
			{'X_5': {'op-time': 'd_5', 'connect':
				{'y_2': {'tr-time': '0', 'buffers': '-'}, 'y_6': {'tr-time': '0', 'buffers': '-'}}}},
			{'X_6': {'op-time': 'd_6', 'connect':
				{'X_7': {'tr-time': '0', 'buffers': '-'}, 'y_4': {'tr-time': '0', 'buffers': '-'}}}},
			{'X_7': {'op-time': 'd_7', 'connect':
				{'y_3': {'tr-time': '0', 'buffers': '-'}, 'y_5': {'tr-time': '0', 'buffers': '-'}}}}]
		output = [
			{'y_1': {'connect': {'X_1': {'tr-time': '0', 'buffers': '-'}}, 'op-time': '0'}},
			{'y_2': {'connect': {'X_3': {'tr-time': '0', 'buffers': '-'}}, 'op-time': '0'}},
			{'y_3': {'connect': {'X_6': {'tr-time': '0', 'buffers': '-'}}, 'op-time': '0'}},
			{'y_4': {'connect': {'X_3': {'tr-time': '0', 'buffers': '-'}}, 'op-time': '0'}},
			{'y_5': {'connect': {'X_1': {'tr-time': '0', 'buffers': '-'}}, 'op-time': '0'}},
			{'y_6': {'connect': {'X_2': {'tr-time': '0', 'buffers': '-'}}, 'op-time': '0'}}]
		result = [
			[['d_1'], ['0', 'd_2'], '-', '-', '-', '-', ['0', 'd_7']],
			['-', ['d_2'], '-', '-', ['0', 'd_5'], '-', '-'],
			['-', '-', ['d_3'], '-', ['0', 'd_5'], ['0', 'd_6'], '-'],
			['-', '-', '-', ['d_4'], '-', '-', '-'],
			['-', '-', '-', '-', ['d_5'], '-', '-'],
			['-', '-', '-', '-', '-', ['d_6'], ['0', 'd_7']],
			['-', '-', '-', '-', '-', '-', ['d_7']]]
		self.pre.mapping = {
			'u_1': 0, 'u_2': 1, 'u_3': 2, 'u_4': 3, 'u_5': 4, 'u_6': 5,
			'X_1': 0, 'X_2': 1, 'X_3': 2, 'X_4': 3, 'X_5': 4, 'X_6': 5, 'X_7': 6,
			'y_1': 0, 'y_2': 1, 'y_3': 2, 'y_4': 3, 'y_5': 4, 'y_6': 5}
		self.assertEqual(self.pre.add_feedback_x(matrix, system, output), result)

	def test_add_feedback_u(self):
			matrix = [
				[['d_1'], '-', '-'],
				['-', ['d_2'], '-'],
				['-', '-', ['d_3']]]
			result = [
				[['d_1'], '-', ['0', '0', '0', 't_{0,1}', 'd_3', 't_{3,4}']],
				['-', ['d_2'], ['0', '0', '0', 't_{0,2}', 'd_3', 't_{3,4}']],
				['-', '-', ['d_3']]]
			input = [
				{'u_1': {'connect': {'M_1': {'tr-time': 't_{0,1}', 'buffers': '-'}}, 'op-time': '0'}},
				{'u_2': {'connect': {'M_2': {'tr-time': 't_{0,2}', 'buffers': '-'}}, 'op-time': '0'}}]
			output = [
				{'y': {'op-time': '0', 'connect': {
					'u_1': {'tr-time': '0', 'buffers': '-'},
					'u_2': {'tr-time': '0', 'buffers': '-'}}}}]
			system = [
				{'M_1': {'connect': {'M_3': {'tr-time': 't_{1,3}', 'buffers': '-'}}, 'op-time': 'd_1'}},
				{'M_2': {'connect': {'M_3': {'tr-time': 't_{2,3}', 'buffers': '-'}}, 'op-time': 'd_2'}},
				{'M_3': {'connect': {'y': {'tr-time': 't_{3,4}', 'buffers': '-'}}, 'op-time': 'd_3'}}]
			self.pre.mapping = {'u_1': 0, 'u_2': 1, 'M_1': 0, 'M_2': 1, 'M_3': 2, 'y': 0}
			self.assertEqual(self.pre.add_feedback_u(matrix, input, system, output), result)
			matrix = [
				[['d_1'], '-', '-', '-', '-', '-', '-'],
				['-', ['d_2'], '-', '-', '-', '-', '-'],
				['-', '-', ['d_3'], '-', '-', '-', '-'],
				['-', '-', '-', ['d_4'], '-', '-', '-'],
				['-', '-', '-', '-', ['d_5'], '-', '-'],
				['-', '-', '-', '-', '-', ['d_6'], '-'],
				['-', '-', '-', '-', '-', '-', ['d_7']]]
			result = [
				[['d_1'], ['0', '0', '0', '0', 'd_2'], '-', '-', '-', '-', '-'],
				['-', ['d_2'], '-', '-', '-', '-', '-'],
				['-', '-', ['d_3'], '-', ['0', '0', '0', '0', 'd_5'], '-', '-'],
				['-', '-', '-', ['d_4'], '-', '-', '-'],
				['-', '-', '-', '-', ['d_5'], '-', '-'],
				['-', '-', '-', '-', '-', ['d_6'], ['0', '0', '0', '0', 'd_7']],
				['-', '-', '-', '-', '-', '-', ['d_7']]]
			input = [
				{'u_1': {'connect': {'X_1': {'tr-time': '0', 'buffers': '-'}}, 'op-time': '0'}},
				{'u_2': {'connect': {'X_3': {'tr-time': '0', 'buffers': '-'}}, 'op-time': '0'}},
				{'u_3': {'connect': {'X_6': {'tr-time': '0', 'buffers': '-'}}, 'op-time': '0'}},
				{'u_4': {'connect': {'X_3': {'tr-time': '0', 'buffers': '-'}}, 'op-time': '0'}},
				{'u_5': {'connect': {'X_1': {'tr-time': '0', 'buffers': '-'}}, 'op-time': '0'}},
				{'u_6': {'connect': {'X_2': {'tr-time': '0', 'buffers': '-'}}, 'op-time': '0'}}]
			output = [
				{'y_1': {'connect': {'u_1': {'tr-time': '0', 'buffers': '-'}}, 'op-time': '0'}},
				{'y_2': {'connect': {'u_2': {'tr-time': '0', 'buffers': '-'}}, 'op-time': '0'}},
				{'y_3': {'connect': {'u_3': {'tr-time': '0', 'buffers': '-'}}, 'op-time': '0'}},
				{'y_4': {}},
				{'y_5': {}},
				{'y_6': {}}]
			system = [
				{'X_1': {'op-time': 'd_1', 'connect': {'X_2': {'tr-time': '0', 'buffers': '-'}, 'X_4': {'tr-time': '0', 'buffers': '-'}}}},
				{'X_2': {'op-time': 'd_2', 'connect': {'y_1': {'tr-time': '0', 'buffers': '-'}, 'X_5': {'tr-time': '0', 'buffers': '-'}}}},
				{'X_3': {'op-time': 'd_3', 'connect': {'X_4': {'tr-time': '0', 'buffers': '-'}, 'X_6': {'tr-time': '0', 'buffers': '-'}}}},
				{'X_4': {'op-time': 'd_4', 'connect': {'X_5': {'tr-time': '0', 'buffers': '-'}, 'X_7': {'tr-time': '0', 'buffers': '-'}}}},
				{'X_5': {'op-time': 'd_5', 'connect': {'y_2': {'tr-time': '0', 'buffers': '-'}, 'y_6': {'tr-time': '0', 'buffers': '-'}}}},
				{'X_6': {'op-time': 'd_6', 'connect': {'X_7': {'tr-time': '0', 'buffers': '-'}, 'y_4': {'tr-time': '0', 'buffers': '-'}}}},
				{'X_7': {'op-time': 'd_7', 'connect': {'y_3': {'tr-time': '0', 'buffers': '-'}, 'y_5': {'tr-time': '0', 'buffers': '-'}}}}]
			self.pre.mapping = {
				'u_1': 0, 'u_2': 1, 'u_3': 2, 'u_4': 3, 'u_5': 4, 'u_6': 5,
				'X_1': 0, 'X_2': 1, 'X_3': 2, 'X_4': 3, 'X_5': 4, 'X_6': 5, 'X_7': 6,
				'y_1': 0, 'y_2': 1, 'y_3': 2, 'y_4': 3, 'y_5': 4, 'y_6': 5}
			self.assertEqual(self.pre.add_feedback_u(matrix, input, system, output), result)

	def test_get_det3(self):
		pred, how = self.pre.get_det3(PRE_DICM, 'y')
		self.assertEqual(pred, 'M_3')
		self.assertEqual(how, ['d_3', 't_{3,4}'])
		pred, how = self.pre.get_det3(PRE_DICM, 'M_3')
		self.assertEqual(pred, 'M_1')
		self.assertEqual(how, ['d_1', 't_{1,3}'])
		# to nadaje się do poprawy, w poniższym przykładzie powinno raczej zwrócić:
		# pred = ['X_2', 'X_4']
		# how = [['d_2'], ['d_4']]
		pred, how = self.pre.get_det3(PRE_DICM2, 'X_5')
		self.assertEqual(pred, 'X_2')
		self.assertEqual(how, ['d_2'])

	def test_show_det3(self):
		self.pre.mapping = {}
		self.pre.values = {}
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.pre.show_det3()
			self.assertEqual(mock_stdout.getvalue(), PRE_DET31)
		self.pre.mapping = PRE_MAP1
		self.pre.values = PRE_MAP2
		self.pre.show_det3()
		with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.pre.show_det3()
			self.assertEqual(mock_stdout.getvalue(), PRE_DET32)

	def test_get_x_value(self):
		key = 'y'
		system = PRE_DICM
		out1, out2, out3 = self.pre.get_x_value(key, system)
		self.assertEqual(out1, 'M_3')
		self.assertEqual(out3, 'd_3')
		self.assertEqual(out2, 2)
		key = 'y_3'
		system = PRE_DICM2
		out1, out2, out3 = self.pre.get_x_value(key, system)
		self.assertEqual(out1, 'X_7')
		self.assertEqual(out3, 'd_7')
		self.assertEqual(out2, 6)

	def test_generatable(self):
		self.pre.vector_u = None
		self.pre.vector_y = None
		self.pre.vector_x = None
		self.assertEqual(self.pre.generatable(), Err.ERR_NO_INPUT)
		self.pre.vector_u = ['u1']
		self.assertEqual(self.pre.generatable(), Err.ERR_NO_OUTPUT)
		self.pre.vector_y = ['y1']
		self.assertEqual(self.pre.generatable(), Err.ERR_NO_STATE_VECT)
		self.pre.vector_x = ['x1']
		self.assertEqual(self.pre.generatable(), Err.NOOP)

	@unittest.skip("not implemented yet")
	def test_matrices_desc(self):
		pass

	@unittest.skip("not implemented yet")
	def test_description(self):
		pass


def main():
	unittest.main()


if __name__ == '__main__':
	main()

# end.
