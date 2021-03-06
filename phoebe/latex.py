#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
**latex.py**
phoebe implementation

in the module:
* *class* **Latex**

Copyright (c) 2017-2018 Jarosław Stańczyk <jaroslaw.stanczyk@upwr.edu.pl>
"""
import inf
from err import Err


class Lat(object):
	"""Lat class"""
	def __init__(self):
		pass

	@staticmethod
	def begin(filename):
		info = inf.Inf()
		time = info.get_time()
		print '%'
		print '% {0}.tex'.format(filename)
		print '% (max, +) system description'
		print '% Copyright (c) 2017-2018 {0} <{1}>'.format(info.AUTHOR, info.AUTHOR_EMAIL)
		print '%'
		print '% automatically generated by {0} on {1}'.format(info.VER, time)
		print '%'
		print '\\documentclass[11pt, a4paper, fleqn]{article}'
		print
		print '\\usepackage{amsmath}'
		print '\\usepackage{currfile}'
		print '\\usepackage{graphicx}'
		print
		print '\\begin{document}'
		print '\\noindent'
		print '\\textbf{(max, +) description} \\texttt{\\currfilebase} \\\\'
		print 'automatically generated by {0} on {1}'.format(info.VER, time)
		print
		return Err.NOOP

	@staticmethod
	def equation():
		print '\\begin{align}\\begin{split}\n' + \
			'% x(k) = A0x(k) + A1x(k-1) + B0u(k)\n' + \
			'\\mathbf{x}(k) & \\, = \\; ' + \
			'\\mathbf{A}_0\\mathbf{x}(k) \\oplus ' + \
			'\\mathbf{A}_1\\mathbf{x}(k-1) \\oplus ' + \
			'\\mathbf{B}_0\\mathbf{u}(k)\\\\\n' + \
			'% y(k) = Cx(k)\n' + \
			'\\mathbf{y}(k) & \\, = \\; \\mathbf{Cx}(k) \\\\\n' + \
			'\\end{split}\\end{align}\n'
		return Err.NOOP

	@staticmethod
	def vector(name, vector):
		print '% vector {0}(k)'.format(name)
		print '\\begin{equation*}'
		print '\\mathbf{%s}(k) = ' % name
		print '\\left[\\begin{array}{*{20}c}'
		for i, _ in enumerate(vector):
			print '  {0}(k) \\\\'.format(vector[i])
		print '\\end{array}\\right]'
		print '\\end{equation*}\n'
		return Err.NOOP

	@staticmethod
	def get_matrix_value(tab):
		if not tab:
			return '-'
		if tab == '-':
			return tab
		odp = ''
		for i, _ in enumerate(tab):
			odp += str(tab[i])
		return odp

	@staticmethod
	def matrix_desc():
		return Err.NOOP

	def matrix(self, name, idx_name, matrix):
		try:
			lan = len(matrix[1])
		except IndexError:
			lan = len(matrix[0])
		str = 'c' * lan
		print '% matrix {0}_{1}'.format(name, idx_name)
		if lan > 20:
			print '\\scalebox{.6}{'
		print '\\begin{equation*}'
		print '\\mathbf{%s}_%s = ' % (name, idx_name)
		print '\\left[\\begin{array}{', str, '}'
		for i, _ in enumerate(matrix):
			for j in range(0, len(matrix[i])):
				if j > 0:
					print '\t&',
				if matrix[i][j] == '-':
					print '\\varepsilon',
				else:
					print self.get_matrix_value(matrix[i][j]),
			print '\\\\'
		print '\\end{array}\\right]'
		print '\\end{equation*}'
		if lan > 20:
			print '}'
		print '\n'
		return Err.NOOP

	@staticmethod
	def values(values):
		if values:
			print '\\noindent\\\\'
			for key in sorted(values):
				print '$%s = %s$,' % (key, values[key])
			print
		return Err.NOOP

	@staticmethod
	def end():
		print '\\end{document}\n' + \
			'% eof\n'
		return Err.NOOP

# eof.
