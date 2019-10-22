#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
**lat.py**
phoebe implementation

in the module:
* *class* **Lat**

Copyright (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
"""
import numbers
from builtins import staticmethod, str, enumerate, range, len, IndexError, sorted

import inf
from yml import Yml
from err import Err


class Lat:
	"""Lat class"""
	def __init__(self):
		self.yam = Yml()
		self.info = inf.Inf()
		self.time = None

	def header(self, filename):
		self.time = self.info.get_time()
		print('%')
		print('% {0}.tex'.format(filename))
		print('% (max, +) system description')
		print('% automatically generated by {0} ver.{1} on {2}'.format(self.info.NAME, self.info.VERSION, self.time))
		print('% Copyright (c) 2017-2019 {0} <{1}>'.format(self.info.AUTHOR, self.info.AUTHOR_EMAIL))
		print('%')
		return Err.NOOP

	def preface(self):
		print()
		print('\\documentclass[11pt, a4paper, fleqn]{article}')
		print()
		print('\\usepackage{amsmath}')
		print('\\usepackage{currfile}')
		print('\\usepackage{graphicx}')
		print()
		print('\\begin{document}')
		print()
		print('\\noindent')
		print('\\textbf{(max, +) description of} \\texttt{\\currfilebase} \\\\')
		print('automatically generated by {0} ver.{1} on {2}'.format(self.info.NAME, self.info.VERSION, self.time))
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
				if len(mat):
					mat = mat + ' \\oplus '
				index = index - i
				tmp = ''
				if index > 0:
					tmp = '+{0}'.format(index)
				elif index < 0:
					tmp = '{0}'.format(index+1)
				if iter is None:
					mat = mat + '\\mathbf{' + name + vec + '}'
				else:
					mat = mat + '\\mathbf{' + name + '}_{' + str(i) + '}\\mathbf{' + vec + '}'
				mat = mat + '(k{0})'.format(tmp)
		return mat

	def equation(self, mat_A, mat_B, mat_C, mat_D):
		print()
		print('\\begin{align}\\begin{split}')
		print('\\mathbf{x}(k+1) & \\, = \\; ', end='')
		mat = self.do_matrices(mat_A, 'A', 'x', 1)
		if len(mat):
			print(mat, end='')
			mat1 = self.do_matrices(mat_B, 'B', 'u', 1)
			if len(mat1):
				print(' \\oplus', mat1, end='')
		print('\\\\')
		if len(mat):
			print('& \\, = \\; \\mathbf{Ax}(k)', end='')
			if len(mat1):
				print(' \\oplus \\mathbf{Bu}(k)', end='')
			print('\\\\')
		print('\\mathbf{y}(k) & \\, = \\; ', end='')
		mat = self.do_matrices(mat_C, 'C', 'x', None)
		if len(mat):
			print(mat, end='')
		mat = self.do_matrices(mat_D, 'D', 'u', None)
		if len(mat):
			print(' \\oplus', mat, end='')
		print('\n\\end{split}\\end{align}')
		return Err.NOOP

	@staticmethod
	def vector(name, vector):
		if not name:
			return Err.ERR_NO_NAME
		print('% vector {0}(k)'.format(name))
		print('\\begin{equation*}')
		print('\\mathbf{%s}(k) = ' % name)
		print('\\left[\\begin{array}{*{20}c}')
		if vector:
			for i, _ in enumerate(vector):
				print('  {0}(k) \\\\'.format(vector[i]))
		else:
			print('\\\\')
		print('\\end{array}\\right]')
		print('\\end{equation*}')
		return Err.NOOP

	@staticmethod
	def get_matrix_value(tab):
		if tab is None:
			return '-'
		if isinstance(tab, numbers.Number):
			return str(tab)
		odp = ''
		for i, _ in enumerate(tab):
			if str(tab[i]) is not '-':
				odp += str(tab[i])
		if odp == '':
			return '-'
		return odp

	@staticmethod
	def matrix_desc():
		print('\\\\')
		print('\\\\')
		print('matrices:')
		return Err.NOOP

	def matrix(self, name, idx_name, matrix):
		if not name:
			return Err.ERR_NO_NAME
		if not idx_name:
			idx_name = ''
		else:
			tmp = '_{' + idx_name + '}'
			idx_name = tmp
		if self.yam.empty_matrix(matrix):
			return Err.ERR_NO_MATRIX
		try:
			lan = len(matrix[1])
		except IndexError:
			lan = len(matrix[0])
		str = 'c' * lan
		print('% matrix {0}{1}'.format(name, idx_name))
		if lan > 20:
			print('\\scalebox{.6}{')
		print('\\begin{equation*}')
		print('\\mathbf{%s}%s = ' % (name, idx_name))
		print('\\left[\\begin{array}{', str, '}')
		for i, _ in enumerate(matrix):
			for j in range(0, len(matrix[i])):
				if j > 0:
					print('\t&', end='')
				if matrix[i][j] == '-':
					print('\\varepsilon', end='')
				else:
					print(self.get_matrix_value(matrix[i][j]), end='')
			print('\\\\')
		print('\\end{array}\\right]')
		print('\\end{equation*}\n')
		if lan > 20:
			print('}')
		return Err.NOOP

	@staticmethod
	def time_values(values):
		if values:
			first = True
			print('\\noindent\\\\')
			print('times:\\\\')
			for key in sorted(values):
				if first:
					print('$%s = %s$' % (key, values[key]), end='')
					first = False
				else:
					print(', $%s = %s$' % (key, values[key]), end='')
			print('.', end='')
			return Err.NOOP
		return Err.ERR_NO_DATA

	@staticmethod
	def end():
		print()
		print('\\end{document}')
		print()
		print('% eof')
		print()
		return Err.NOOP

	def inits(self, vec_u, vec_x, values):
		self.time_values(values)
		return Err.NOOP

	def vectors(self, vec_u, vec_x, vec_y):
		print()
		self.vector('u', vec_u)
		self.vector('x', vec_x)
		self.vector('y', vec_y)
		return Err.NOOP

	@staticmethod
	def adds(matA, matB, matC, matD, vecX):
		return Err.NOOP

# eof.
