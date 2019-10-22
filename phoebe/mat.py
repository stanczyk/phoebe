#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
**mat.py**
phoebe implementation

in the module:
* *class* **Mat**

Copyright (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
"""
# pylint: disable=invalid-name
import numbers
from builtins import range, len, staticmethod, enumerate, sorted, str, isinstance, object

import inf
from yml import Yml
from err import Err


class Mat(object):
	"""Mat class"""
	def __init__(self):
		self.yam = Yml()

	@staticmethod
	def header(filename):
		info = inf.Inf()
		print('%')
		print('% {0}.m'.format(filename))
		print('% (max, +) system description')
		print('% automatically generated by {0} ver.{1} on {2}'.format(info.NAME, info.VERSION, info.get_time()))
		print('% Copyright (c) 2017-2019 {0} <{1}>'.format(info.AUTHOR, info.AUTHOR_EMAIL))
		print('%')
		return Err.NOOP

	@staticmethod
	def preface():
		print()
		print('clear')
		return Err.NOOP

	def do_matrices(self, matrix, name, vec, iter):
		if iter:
			index = iter
		else:
			index = 0
		mat = ''
		if not matrix:
			return mat
		if self.yam.empty_matrix(matrix):
			return mat
		for i in range(0, len(matrix)):
			if not self.yam.empty_matrix(matrix[i]):
				if matrix[i]:
					if len(mat):
						mat = mat + ' + '
					index = index - i
					tmp = ''
					if index > 0:
						tmp = '+{0}'.format(index)
					elif index < 0:
						tmp = '{0}'.format(index+1)
					if iter is None:
						mat = mat + '{0}{1}(k{2})'.format(name, vec, tmp)
					else:
						mat = mat + '{0}{1}{2}(k{3})'.format(name, i, vec, tmp)
		return mat

	def equation(self, mat_A, mat_B, mat_C, mat_D):
		print('disp(\'x(k+1) = ', end='')
		mat = self.do_matrices(mat_A, 'A', 'x', 1)
		if len(mat):
			print(mat, end='')
			mat1 = self.do_matrices(mat_B, 'B', 'u', 1)
			if len(mat1):
				print(' +', mat1, end='')
		print('\');')
		if len(mat):
			print('disp(\'       = Ax(k)', end='')
			if len(mat1):
				print(' + Bx(k)', end='')
			print('\');')
		print('disp(\'y(k)   = ', end='')
		mat = self.do_matrices(mat_C, 'C', 'x', None)
		if len(mat):
			print(mat, end='')
		mat = self.do_matrices(mat_D, 'D', 'u', None)
		if len(mat):
			print(' +', mat, end='')
		print('\');')
		return Err.NOOP

	# czy nie powinno być:
	# 	dla '-' 					0 \varepsilon albo ''???
	# TODO clean_value() sprawdzić - czy działanie jest napewno OK
	@staticmethod
	def clean_value(value):
		ans = ''
		if not value:
			return ans
		if isinstance(value, numbers.Number):
			return value
		for i, _ in enumerate(value):
			if value[i] not in ['{', '}', '_', ',']:
				ans += value[i]
		return ans

	def time_values(self, values):
		if values:
			for key in sorted(values):
				print('%s = %s' % (self.clean_value(key), values[key]))
			return Err.NOOP
		return Err.ERR_NO_DATA

	@staticmethod
	def vector(name, vector):
		if not name:
			return Err.ERR_NO_NAME
		print('disp(\'{0}(k) = ['.format(name), end='')
		if vector:
			for i, _ in enumerate(vector):
				print(' {0}(k);'.format(vector[i]), end='')
		print(' ]\');')
		return Err.NOOP

	# czy nie powinno być:
	# 	dla '-' -> \varepsilon
	# 	dla ['d_1', 'd_2', 'd_3'] -> mp_multi(d1, d2, d3) albo mp_multi(mp_multi(d1, d2), d3)
	# a co dla [], albo None ???
	# patrz też tests/test_mat.py:test_get_matrix_value
	# TODO get_matrix_value() do poprawy
	def get_matrix_value(self, tab):
		if tab is None:
			return ''
		odp = ''
		if isinstance(tab, str):
			tmp = str(self.clean_value(tab))
			if tmp == '-':
				return ''
			return tmp
		if isinstance(tab, numbers.Number):
			return str(tab)
		for i, _ in enumerate(tab):
			tmp = str(self.clean_value(tab[i]))
			if tmp == '-':
				tmp = ''
			if tmp:
				if odp:
					tmp2 = 'mp_multi({0}, {1})'.format(odp, tmp)
					odp = tmp2
				else:
					odp = tmp
		return odp

	@staticmethod
	def matrix_desc():
		print('\ndisp(\'matrices:\');')
		return Err.NOOP

	def matrix(self, name, idx_name, mat, dl=None):
		if not name:
			return Err.ERR_NO_NAME
		if not idx_name:
			idx_name = ''
		if self.yam.empty_matrix(mat):
			return Err.ERR_NO_MATRIX
		print('% matrix {0}{1}'.format(name, idx_name))
		w1, w2 = self.yam.get_matrix_size(mat)
		if not dl:
			dl = w2
		print('{0}{1} = mp_zeros({2}, {3});'.format(name, idx_name, w1, dl))
		for i in range(0, w1):
			for j in range(0, w2):
				if mat[i][j] != '-':
					print('   {0}{1}({2}, {3}) = {4};'.format(
						name, idx_name, i + 1, j + 1, self.get_matrix_value(mat[i][j])
					))
		print('   {0}{1}'.format(name, idx_name))
		print()
		return Err.NOOP

	@staticmethod
	def input_vec(vec):
		if not vec:
			return Err.ERR_NO_VECTOR
		print('U  = mp_ones({0}, 1)'.format(len(vec)))
		return Err.NOOP

	@staticmethod
	def start_vec(vec):
		if not vec:
			return Err.ERR_NO_VECTOR
		print('X0 = mp_zeros({0}, {1})'.format(len(vec), 1))
		return Err.NOOP

	def adds(self, matA, matB, matC, matD, vecX):
		print('' + \
			'disp(\'finally:\');\n' + \
			'As  = mp_star(A0)')
		licz_wmacA = len(matA)
		licz_wier = len(matA[0])
		self.print_matAB(licz_wmacA, licz_wier, matA, 'A')

		licz_wmac = len(matB)
		self.print_matAB(licz_wmac, licz_wier, matB, 'B')

		licz, licz_wmac = self.yam.get_matrix_size(matC)
		if (licz_wmacA - 1) * licz_wier > licz_wmac:
			print()
			self.matrix('C', '', matC, (licz_wmacA - 1) * licz_wier)

		if (licz_wmacA - 1) * licz_wier > len(vecX):
			print('% modification of init vector')
			print('X0 = mp_zeros({0}, 1)'.format((licz_wmacA - 1) * licz_wier))
			print()

		print('' + \
			'disp(\'state vector and output:\');\n' + \
			'% k - number of iterations\n' + \
			'k = 12;\n\n' + \
			'X(:, 1) = mp_add(mp_multi(A, X0), mp_multi(B, U));\n' + \
			'Y(:, 1) = mp_multi(C, X(:, 1));\n' + \
			'for i = 2:k\n' + \
			'    X(:, i) = mp_add(mp_multi(A, X(:, i - 1)), mp_multi(B, U));\n' + \
			'    Y(:, i) = mp_multi(C, X(:, i));\n' + \
			'end\n' + \
			'X\n' + \
			'Y')
		return Err.NOOP

	@staticmethod
	def end():
		print()
		print('% eof')
		print()
		return Err.NOOP

	def inits(self, vec_u, vec_x, values):
		print('\ndisp(\'initial vectors:\');')
		self.input_vec(vec_u)
		self.start_vec(vec_x)
		print('\ndisp(\'times:\');')
		self.time_values(values)
		return Err.NOOP

	def vectors(self, vec_u, vec_x, vec_y):
		print()
		self.vector('u', vec_u)
		self.vector('x', vec_x)
		self.vector('y', vec_y)
		return Err.NOOP

	def print_matAB(self, dl, sz, matirces, first_letter):
		print('\n% matrix ' + first_letter)
		for i in range(1, dl):
			if not self.yam.empty_matrix(matirces[i]):
				print(first_letter + 's' + str(i) + ' = mp_multi(As, ' + first_letter + str(i) + ');')
		tmp = '      '
		print(first_letter + '   = [')
		print(tmp, end='')
		for i in range(1, dl):
			if not self.yam.empty_matrix(matirces[i]):
				print(' ' + first_letter + 's' + str(i), end='')
		print(';')
		for i in range(1, sz):
			print(tmp, end='')
			for j in range(1, dl):
				if first_letter == 'A':
					if i == j:
						print(' mp_eye(size(As1))', end='')
					else:
						print(' mp_zeros(size(As1))', end='')
				else:
					print(' mp_zeros(size(' + first_letter + 's1))', end='')
			print(';')
		print(tmp + ']')
		return Err.NOOP

# eof.
