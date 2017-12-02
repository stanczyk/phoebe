#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
**worker.py**
phoebe implementation

in the module:
* *class* **Worker**

Copyright 2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl
"""
# pylama: ignore=C901
# pylint: disable=relative-import
import sys
from err import Err
from parser import Parser
from latex import Lat


class Worker(object):
	"""Worker class"""
	# pylint: disable=invalid-name, missing-docstring, too-many-instance-attributes
	def __init__(self):
		self.parser = None
		self.u = []
		self.x = []
		self.y = []
		self.A0 = []
		self.A1 = []
		self.B0 = []
		self.C = []
		self.mapping = {}
		self.values = None

	def prepare_vectors(self):
		vec = []
		tmp = []
		for i in ['input', 'prod-unit', 'output']:
			my_dic = self.parser.yaml.get_value(self.parser.content_yaml, i)
			if i == 'input':
				vec = self.u
			if i == 'prod-unit':
				vec = tmp
			if i == 'output':
				vec = self.y
			for j in range(0, self.parser.yaml.get_len(my_dic)):
				vec.append(self.parser.yaml.get_key(my_dic[j]))
		for i in range(0, len(tmp)):
			self.x.append('x_' + str(i + 1))
		return Err.NOOP

	def show_vectors(self):
		print '== VECTORS ================='
		self.print_vector('u(k)', self.u)
		self.print_vector('x(k)', self.x)
		self.print_vector('y(k)', self.y)
		return Err.NOOP

	@staticmethod
	def print_vector(name, vector):
		print name + ' = [',
		for i in range(0, len(vector)):
			print '{0}(k)'.format(vector[i]),
		print ']\'' if len(vector) > 1 else ']'
		return Err.NOOP

	def prepare_mapping(self):
		for i in ['input', 'prod-unit', 'output']:
			my_dic = self.parser.yaml.get_value(self.parser.content_yaml, i)
			for j in range(0, self.parser.yaml.get_len(my_dic)):
				name = self.parser.yaml.get_key(my_dic[j])
				self.mapping[name] = j
		i = 'values'
		my_dic = self.parser.yaml.get_value(self.parser.content_yaml, i)
		if my_dic:
			self.values = my_dic
		return Err.NOOP

	def create_matrix(self, matrix, v1, v2):
		for _ in range(0, self.parser.yaml.get_len(v1)):
			tmp = []
			for __ in range(0, self.parser.yaml.get_len(v2)):
				tmp.append('-')
			matrix.append(tmp)
		return Err.NOOP

	def fill_matrix(self, matrix, my_dic):
		for i in range(0, self.parser.yaml.get_len(my_dic)):
			key = self.parser.yaml.get_key(my_dic[i])
			op_time, connect, tr_time = self.parser.get_details(self.parser.yaml.get_value(my_dic[i], key))
			tmp = ''
			if op_time:
				tmp += op_time
			if matrix in [self.A0, self.B0]:
				if connect and connect[0] != 'y':
					if tr_time:
						tmp += tr_time
					j = self.mapping[connect]
					matrix[j][i] = tmp
			if matrix in [self.A1]:
				if op_time:
					j = self.mapping[key]
					matrix[j][i] = tmp
			if matrix in [self.C]:
				if connect and connect[0] == 'y':
					if tr_time:
						tmp += tr_time
					j = self.mapping[connect]
					matrix[j][i] = tmp
		return Err.NOOP

	def matrix_preparation(self):
		self.create_matrix(self.B0, self.x, self.u)
		self.fill_matrix(self.B0, self.parser.yaml.get_value(self.parser.content_yaml, 'input'))
		prod_unit = self.parser.yaml.get_value(self.parser.content_yaml, 'prod-unit')
		self.create_matrix(self.A0, self.x, self.x)
		self.fill_matrix(self.A0, prod_unit)
		self.create_matrix(self.A1, self.x, self.x)
		self.fill_matrix(self.A1, prod_unit)
		self.create_matrix(self.C, self.y, self.x)
		self.fill_matrix(self.C, prod_unit)
		return Err.NOOP

	def show_details3(self):
		print '== DETAILS 3 ==============='
		print 'mapping:'
		print self.mapping
		print self.values
		self.show_matrices()

	def show_matrices(self):
		print '== MATRICES ================'
		for i in [self.A0, self.A1, self.B0, self.C]:
			if i == self.A0:
				print 'A0 =',
			if i == self.A1:
				print 'A1 =',
			if i == self.B0:
				print 'B0 =',
			if i == self.C:
				print 'C  =',
			print i
		return Err.NOOP

	def latex(self):
		tmp = tmp1 = tmp2 = None
		lat = Lat()
		lat.begin()
		lat.equation()
		for i in [self.u, self.x, self.y]:
			if i == self.u:
				tmp = 'u'
			if i == self.x:
				tmp = 'x'
			if i == self.y:
				tmp = 'y'
			lat.vector(tmp, i)
		for i in [self.A0, self.A1, self.B0, self.C]:
			if i == self.A0:
				tmp1 = 'A'
				tmp2 = '_0'
			if i == self.A1:
				tmp1 = 'A'
				tmp2 = '_1'
			if i == self.B0:
				tmp1 = 'B'
				tmp2 = '_0'
			if i == self.C:
				tmp1 = 'C'
				tmp2 = ''
			lat.matrix(tmp1, tmp2, i)
		lat.values(self.values)
		lat.end()

	def matlab(self):
		pass

	def main_work(self):
		self.prepare_vectors()
		if self.parser.args['--vectors']:
			self.show_vectors()
		self.prepare_mapping()
		self.matrix_preparation()
		if self.parser.args['--details3']:
			self.show_details3()
		if self.parser.args['--latex']:
			self.latex()
		else:
			self.matlab()

		return Err.NOOP

	def main(self):
		self.parser = Parser()
		self.parser.main()
		sys.exit(self.main_work())


if __name__ == '__main__':
	Worker().main()

# eof.
