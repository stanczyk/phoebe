#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
**worker.py**
phoebe implementation

in the module:
* *class* **Worker**

Copyright 2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl
"""
import sys
from err import Err
from inf import Inf
from parser import Parser


class Worker(object):
	"""Worker class"""
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

	def show_vectors(self):
		print '== VECTORS ================='
		self.print_vector('u(k)', self.u)
		self.print_vector('x(k)', self.x)
		self.print_vector('y(k)', self.y)

	@staticmethod
	def print_vector(name, vector):
		print name + ' = [',
		for i in range(0, len(vector)):
			print vector[i],
		print ']\'' if len(vector) > 1 else ']'

	def prepare_mapping(self):
		for i in ['input', 'prod-unit', 'output']:
			my_dic = self.parser.yaml.get_value(self.parser.content_yaml, i)
			for j in range(0, self.parser.yaml.get_len(my_dic)):
				name = self.parser.yaml.get_key(my_dic[j])
				self.mapping[name] = j

	def create_matrix(self, matrix, v1, v2):
		for _ in range(0, self.parser.yaml.get_len(v1)):
			tmp = []
			for __ in range(0, self.parser.yaml.get_len(v2)):
				tmp.append('e')
			matrix.append(tmp)

	def fill_matrix(self, matrix, my_dic):
		for i in range(0, self.parser.yaml.get_len(my_dic)):
			key = self.parser.yaml.get_key(my_dic[i])
			int_dic = self.parser.yaml.get_value(my_dic[i], key)
			op_time, connect, tr_time = self.parser.get_details(int_dic)
			tmp = ''
			if op_time:
				tmp += op_time
			if matrix in ['A0', 'B0']:
				if connect and connect[0] != 'y':
					j = self.mapping[connect]
					if tr_time:
						tmp += tr_time
					if matrix == 'A0':
						self.A0[j][i] = tmp
					if matrix == 'B0':
						self.B0[j][i] = tmp
			if matrix in ['A1']:
				if op_time:
					j = self.mapping[key]
					self.A1[j][i] = tmp
			if matrix in ['C']:
				if connect and connect[0] == 'y':
					j = self.mapping[connect]
					if tr_time:
						tmp += tr_time
					self.C[j][i] = tmp

	def matrix_preparation(self):
		self.create_matrix(self.B0, self.x, self.u)
		self.fill_matrix('B0', self.parser.yaml.get_value(self.parser.content_yaml, 'input'))
		prod_unit = self.parser.yaml.get_value(self.parser.content_yaml, 'prod-unit')
		self.create_matrix(self.A0, self.x, self.x)
		self.fill_matrix('A0', prod_unit)
		self.create_matrix(self.A1, self.x, self.x)
		self.fill_matrix('A1', prod_unit)
		self.create_matrix(self.C, self.y, self.x)
		self.fill_matrix('C', prod_unit)

	def show_matrices(self):
		print '== MATRICES ================'
		for i in [self.A0, self.A1, self.B0, self.C]:
			print i

	def main_work(self):
		self.prepare_vectors()
		if self.parser.args['--vectors']:
			self.show_vectors()
		self.prepare_mapping()
		print self.mapping
		self.matrix_preparation()
		self.show_matrices()
		return Err.NOOP

	def main(self):
		self.parser = Parser()
		self.parser.main()
		sys.exit(self.main_work())


if __name__ == '__main__':
	Worker().main()

# eof.
