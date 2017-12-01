#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
**latex.py**
phoebe implementation

in the module:
* *class* **Latex**

Copyright 2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl
"""


class Lat(object):
	"""Lat class"""
	# pylint: disable=missing-docstring
	def __init__(self):
		pass

	@staticmethod
	def begin():
		print '%\n' + \
			'% (max, +) system description in latex\n' + \
			'% (c) 2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl\n' + \
			'%\n' + \
			'\\documentclass[11pt, a4paper]{article}\n' + \
			'\\usepackage{amsmath}\n' + \
			'\\begin{document}\n'

	@staticmethod
	def vector(name, vector):
		print '% vector {0}(k)'.format(name)
		print '\\begin{equation*}'
		print '\\mathbf{%s}(k) = ' % name
		print '\\left[\\begin{array}{*{20}c}'
		for i in range(0, len(vector)):
			print '  {0}(k) \\\\'.format(vector[i])
		print '\\end{array}\\right]'
		print '\\end{equation*}\n'

	@staticmethod
	def matrix(name, idx_name, matrix):
		print '% matrix {0}{1}'.format(name, idx_name)
		print '\\begin{equation*}'
		print '\\mathbf{%s}%s = ' % (name, idx_name)
		print '\\left[\\begin{array}{*{20}c}'
		for i in range(0, len(matrix)):
			for j in range(0, len(matrix[i])):
				if j > 0:
					print '\t&',
				if matrix[i][j] == '-':
					print '\\varepsilon',
				else:
					print matrix[i][j],
			print '\\\\'
		print '\\end{array}\\right]'
		print '\\end{equation*}\n'

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

	@staticmethod
	def end():
		print '\\end{document}\n' + \
			'% eof\n'

# eof.
