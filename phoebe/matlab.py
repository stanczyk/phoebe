#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
**matlab.py**
phoebe implementation

in the module:
* *class* **Matlab**

Copyright (c) 2017-2018 Jarosław Stańczyk <jaroslaw.stanczyk@upwr.edu.pl>
"""
# pylint: disable=invalid-name
import inf
from yml import Yml
from err import Err


class Mat(object):
	"""Mat class"""
	def __init__(self):
		self.yam = Yml()

	@staticmethod
	def begin(filename):
		info = inf.Inf()
		print '%'
		print '% {0}.m'.format(filename)
		print '% (max, +) system description'
		print '% Copyright (c) 2017-2018 {0} <{1}>'.format(info.AUTHOR, info.AUTHOR_EMAIL)
		print '%'
		print '% automatically generated by {0} on {1}'.format(info.VER, info.get_time())
		print '%'
		print
		return Err.NOOP

	@staticmethod
	def equation():
		print 'clear\n' + \
			'disp(\'\');\n' + \
			'disp(\'x(k) = A0x(k) + A1x(k-1) + B0u(k)\');\n' + \
			'disp(\'y(k) =  Cx(k)\');\n' + \
			'disp(\'---------------------------------\');'
		return Err.NOOP

	@staticmethod
	def clean_value(value):
		ans = ''
		for i, _ in enumerate(value):
			if value[i] not in ['{', '}', '_', ',']:
				ans += value[i]
		return ans

	def values(self, values):
		if values:
			print 'disp(\'times:\');'
			for key in sorted(values):
				print '%s = %s' % (self.clean_value(key), values[key])
			print
		return Err.NOOP

	@staticmethod
	def vector(name, vector):
		print 'disp(\'{0}(k) = ['.format(name),
		for i, _ in enumerate(vector):
			print '{0}(k);'.format(vector[i]),
		print ']\');'
		return Err.NOOP

	def get_matrix_value(self, tab):
		if not tab:
			return '0'
		if tab == '-':
			return tab
		odp = ''
		tmp = ''
		for i, _ in enumerate(tab):
			if len(tab) > 1 and i > 0:
				odp = 'mp_multi({0}, '.format(tmp)
			tmp = str(self.clean_value(tab[i]))
			odp += tmp
			if len(tab) > 1 and i > 0:
				odp += ')'
		return odp

	@staticmethod
	def matrix_desc():
		print 'disp(\'matrices:\');'
		return Err.NOOP

	def matrix(self, name, idx_name, matrix):
		print '% matrix {0}{1}'.format(name, idx_name)
		w1, w2 = self.yam.get_matrix_size(matrix)
		print '{0}{1} = mp_zeros({2}, {3});'.format(name, idx_name, w1, w2)
		for i in range(0, w1):
			for j in range(0, w2):
				if matrix[i][j] != '-':
					print '   {0}{1}({2}, {3}) = {4};'.format(
						name, idx_name, i + 1, j + 1, self.get_matrix_value(matrix[i][j])
					)
		print '   {0}{1}'.format(name, idx_name)
		print
		return Err.NOOP

	@staticmethod
	def input_vec(vec):
		print 'disp(\'---------------------------------\');\n'
		print 'disp(\'initial vectors:\');'
		print 'U  = mp_ones({0}, {1})'.format(len(vec), 1)
		return Err.NOOP

	@staticmethod
	def start_vec(vec):
		print 'X0 = mp_zeros({0}, {1})'.format(len(vec), 1)
		print
		return Err.NOOP

	@staticmethod
	def adds():
		print '' + \
			'disp(\'model:\');\n' + \
			'As = mp_star(A0)\n' + \
			'A = mp_multi(As, A1)\n' + \
			'B = mp_multi(As, B0)\n' + \
			'\n' + \
			'disp(\'state vector and output:\');\n' + \
			'% number of iterations\n' + \
			'k = 12;\n' + \
			'X(:, 1) = mp_add(mp_multi(A, X0), mp_multi(B, U));\n' + \
			'Y(:, 1) = mp_multi(C, X(:, 1));\n' + \
			'for i = 2:k\n' + \
			'    X(:, i) = mp_add(mp_multi(A, X(:, i - 1)), mp_multi(B, U));\n' + \
			'    Y(:, i) = mp_multi(C, X(:, i));\n' + \
			'end\n' + \
			'X\n' + \
			'Y\n'
		return Err.NOOP

	@staticmethod
	def end():
		print '% eof\n'
		return Err.NOOP

# eof.
