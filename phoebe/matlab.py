#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
**matlab.py**
phoebe implementation

in the module:
* *class* **Matlab**

Copyright 2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl
"""
# pylint: disable=invalid-name
import inf
from yml import Yml


class Mat(object):
	"""Mat class"""
	def __init__(self):
		self.yam = Yml()

	@staticmethod
	def begin():
		info = inf.Inf()
		print '%'
		print '% (max, +) system description'
		print '% (c) 2017 {0}, e-mail: {1}'.format(info.AUTHOR, info.AUTHOR_EMAIL)
		print '%'
		print '% automatically generated by {0} on {1}'.format(info.VER, info.get_time())
		print '%'
		print

	@staticmethod
	def equation():
		print 'clear\n' + \
			'disp(\' \');\n' + \
			'disp(\'x(k) = A0x(k) + A1x(k-1) + B0u(k)\');\n' + \
			'disp(\'y(k) =  Cx(k)\');\n' + \
			'disp(\'---------------------------------\');\n'

	@staticmethod
	def clean_value(value):
		ans = ''
		for i in range(0, len(value)):
			if value[i] not in ['{', '}', '_', ',']:
				ans += value[i]
		return ans

	def values(self, values):
		if values:
			for key in sorted(values):
				print '%s = %s' % (self.clean_value(key), values[key])
			print

	@staticmethod
	def vector(name, vector):
		print 'disp(\'{0}(k) = ['.format(name),
		for i in range(0, len(vector)):
			print '{0}(k);'.format(vector[i]),
		print ']\');'

	def get_matrix_value(self, tab):
		if not tab:
			return '-'
		if tab == '-':
			return tab
		odp = ''
		tmp = ''
		for i in range(0, len(tab)):
			if len(tab) > 1 and i > 0:
				odp = 'mp_multi({0}, '.format(tmp)
			tmp = str(self.clean_value(tab[i]))
			odp += tmp
			if len(tab) > 1 and i > 0:
				odp += ')'
			tmp = odp
		return tmp

	def matrix(self, name, idx_name, matrix):
		print '% matrix {0}{1}'.format(name, idx_name)
		w1, w2 = self.yam.get_matrix_size(matrix)
		print '{0}{1} = mp_zeros({2}, {3});'.format(name, idx_name, w1, w2)
		for i in range(0, w1):
			for j in range(0, w2):
				if matrix[i][j] != '-':
					print '   {0}{1}({2}, {3}) = {4};'.format(name, idx_name, i+1, j+1, self.get_matrix_value(matrix[i][j]))
		print

	@staticmethod
	def input_vec(vec):
		print 'disp(\'---------------------------------\');\n'
		print 'disp(\'initial vectors:\');\n'
		print 'disp(\'\');\n'
		print 'U  = mp_ones({0}, {1})'.format(len(vec), 1)

	@staticmethod
	def start_vec(vec):
		print 'X0 = mp_zeros({0}, {1})'.format(len(vec), 1)
		print

	@staticmethod
	def adds():
		print '' + \
			'A0\n' + \
			'A1\n' + \
			'B0\n' + \
			'C\n' + \
			'\n' + \
			'As = mp_star(A0)\n' + \
			'A = mp_multi(As, A1)\n' + \
			'B = mp_multi(As, B0)\n' + \
			'\n' + \
			'% number of iterations\n' + \
			'k = 12;\n' + \
			'X(:, 1) = mp_add(mp_multi(A, X0), mp_multi(B, U));\n' + \
			'Y(1) = mp_multi(C, X(:, 1));\n' + \
			'for i = 2:k\n' + \
			'    X(:, i) = mp_add(mp_multi(A, X(:, i - 1)), mp_multi(B, U));\n' + \
			'    Y(i) = mp_multi(C, X(:, i));\n' + \
			'end\n' + \
			'X\n' + \
			'Y\n'


	@staticmethod
	def end():
		print '% eof\n'

# eof.
