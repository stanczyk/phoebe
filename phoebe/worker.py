#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
**worker.py**
phoebe implementation

in the module:
* *class* **Worker**

Copyright (c) 2017-2018 Jarosław Stańczyk <jaroslaw.stanczyk@upwr.edu.pl>
"""
import sys
from err import Err
from parser import Parser
from latex import Lat
from matlab import Mat


class Worker(object):
	"""Worker class"""
	# pylint: disable=invalid-name
	# pylint: disable=too-many-instance-attributes
	# pylint: disable=too-many-nested-blocks
	# pylint: disable=too-many-public-methods
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

	def init_parser(self):
		self.parser = Parser()

	def prepare_vectors(self):
		vec = []
		tmp = []
		for i in ['input', 'prod-unit', 'output']:
			my_dic = self.parser.yml.get_value(self.parser.content_yaml, i)
			if i == 'input':
				vec = self.u
			if i == 'prod-unit':
				vec = tmp
			if i == 'output':
				vec = self.y
			for j in range(0, self.parser.yml.get_len(my_dic)):
				vec.append(self.parser.yml.get_key(my_dic[j]))
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
		for _, j in enumerate(vector):
			print '{0}(k)'.format(j),
		print ']\'' if len(vector) > 1 else ']'
		return Err.NOOP

	def prepare_mapping(self):
		for i in ['input', 'prod-unit', 'output']:
			my_dic = self.parser.yml.get_value(self.parser.content_yaml, i)
			for j in range(0, self.parser.yml.get_len(my_dic)):
				name = self.parser.yml.get_key(my_dic[j])
				self.mapping[name] = j
		i = 'values'
		my_dic = self.parser.yml.get_value(self.parser.content_yaml, i)
		if my_dic:
			self.values = my_dic
		return Err.NOOP

	@staticmethod
	def create_matrix(matrix, v1, v2):
		for _ in range(0, len(v1)):
			tmp = []
			for __ in range(0, len(v2)):
				tmp.append('-')
			matrix.append(tmp)
		return matrix

	def fill_(self, matrix, iteration, con, val):  # noqa: C901
		if con:
			for key in con:
				tr_time, buffers = self.parser.get_det2(con[key])
				j = self.mapping[key]
				if key[0] != 'y':
					if matrix in [self.A0, self.B0]:
						if tr_time:
							val.append(tr_time)
						matrix[j][iteration] = val
					if matrix in [self.A1]:
						if buffers == '0':
							if tr_time == '0':
								matrix[iteration][j] = ['0']
							else:
								matrix[iteration][j] = ['-' + tr_time]
				else:
					if matrix in [self.C]:
						if tr_time:
							val.append(tr_time)
						matrix[j][iteration] = val
		return matrix

	def fill_matrix(self, matrix, my_dic):
		for i in range(0, self.parser.yml.get_len(my_dic)):
			key = self.parser.yml.get_key(my_dic[i])
			op_time, connect = self.parser.get_det1(self.parser.yml.get_value(my_dic[i], key))
			tmp = []
			if op_time:
				tmp.append(op_time)
			self.fill_(matrix, i, connect, tmp)
			if matrix == self.A1:
				if op_time:
					j = self.mapping[key]
					matrix[j][i] = tmp
				self.fill_(matrix, i, connect, tmp)
		return matrix

	def add_feedback_x(self, matrix, system, output):
		for i in range(0, self.parser.yml.get_len(output)):
			key1 = self.parser.yml.get_key(output[i])
			op_time, connect = self.parser.get_det1(self.parser.yml.get_value(output[i], key1))
			if connect:
				for key in connect:
					if key[0].upper() != 'U':
						tmp = []
						if op_time:
							tmp.append(op_time)
						# tr_time, buffers = self.parser.get_det2(connect[key])
						j = self.mapping[key]
						# print key, '(', j, ',', key1, ')'
						_, idx, time = self.get_x_value(key1, system)
						# print key1, key, key2
						tmp.append(time)
						val = matrix[j][idx]
						if val != '-':
							tmp.append(val)
						matrix[j][idx] = tmp
		return matrix

	def add_feedback_u(self, matrix, we, sy, wy):  # noqa: C901
		# pylint: disable=too-many-locals
		for i in range(0, self.parser.yml.get_len(wy)):
			key1 = self.parser.yml.get_key(wy[i])
			key0, opt = self.parser.get_det3(sy, key1)
			op_time, con1 = self.parser.get_det1(self.parser.yml.get_value(wy[i], key1))
			if con1:
				for key2 in con1:
					if key2[0].upper() == 'U':
						tmp = []
						if op_time:
							tmp.append(op_time)
						tr_time, _ = self.parser.get_det2(con1[key2])
						if tr_time:
							tmp.append(tr_time)
						for j in range(0, self.parser.yml.get_len(we)):
							key3 = self.parser.yml.get_key(we[j])
							if key3 == key2:
								op_time, con2 = self.parser.get_det1(self.parser.yml.get_value(we[j], key2))
								if op_time:
									tmp.append(op_time)
								for key4 in con2:
									tr_time, _ = self.parser.get_det2(con2[key4])
									if tr_time:
										tmp.append(tr_time)
									idx1 = self.mapping[key4]
									tmp.append(opt)
									idx2 = self.mapping[key0]
									matrix[idx1][idx2] = tmp
		return matrix

	def get_x_value(self, key, my_dic):
		for i in range(0, self.parser.yml.get_len(my_dic)):
			key1 = self.parser.yml.get_key(my_dic[i])
			op_time, connect = self.parser.get_det1(self.parser.yml.get_value(my_dic[i], key1))
			if connect:
				for key2 in connect:
					if key2 == key:
						return key1, i, op_time
		return None, None, None

	def rm_repeated_zeros(self, matrix):
		""" 0, 0, 0 -> 0 """
		# pylint: disable=consider-using-enumerate
		w1, w2 = self.parser.yml.get_matrix_size(matrix)
		for i in range(0, w1):
			for j in range(0, w2):
				if matrix[i][j] != '-':
					tmp = matrix[i][j]
					for k in range(0, len(tmp)):
						if tmp[k] == '0' and tmp.count(tmp[k]) > 1:
							tmp[k] = None
					for k in range(0, tmp.count(None)):
						tmp.remove(None)
		return matrix

	def rm_redundant_zeros(self, matrix):
		""" 0, d_1 -> d1 """
		w1, w2 = self.parser.yml.get_matrix_size(matrix)
		for i in range(0, w1):
			for j in range(0, w2):
				if matrix[i][j] != '-':
					tmp = matrix[i][j]
					if len(tmp) > 1 and tmp.count('0'):
						tmp.remove('0')
		return matrix

	def optimize_matrix(self, matrix):
		if not matrix:
			return matrix
		self.rm_repeated_zeros(matrix)
		self.rm_redundant_zeros(matrix)
		return matrix

	def matrix_preparation(self):
		we = self.parser.yml.get_value(self.parser.content_yaml, 'input')
		sy = self.parser.yml.get_value(self.parser.content_yaml, 'prod-unit')
		wy = self.parser.yml.get_value(self.parser.content_yaml, 'output')
		# matrix B0
		self.create_matrix(self.B0, self.x, self.u)
		self.fill_matrix(self.B0, we)
		# matrix A0 and A1
		for i in [self.A0, self.A1]:
			self.create_matrix(i, self.x, self.x)
			self.fill_matrix(i, sy)
		# self.add_feedback()
		self.add_feedback_x(self.A1, sy, wy)
		self.add_feedback_u(self.A1, we, sy, wy)
		# self.add_feedback_y(self.A1, prod_unit)
		# matrix C
		self.create_matrix(self.C, self.y, self.x)
		self.fill_matrix(self.C, sy)
		# polishing
		for i in [self.A0, self.A1, self.B0, self.C]:
			self.optimize_matrix(i)
		return Err.NOOP

	def show_det3(self):
		print '== DETAILS 3 ==============='
		print 'mapping:'
		print self.mapping
		print self.values
		self.show_matrices()
		return Err.NOOP

	@staticmethod
	def prn_matrix(matrix):
		if matrix:
			print '['
			for _, j in enumerate(matrix):
				print j
			print ']'
		else:
			print '[]'

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
			self.prn_matrix(i)
		return Err.NOOP

	def desc_vector(self, obj):
		tmp = None
		for i in [self.u, self.x, self.y]:
			if i == self.u:
				tmp = 'u'
			if i == self.x:
				tmp = 'x'
			if i == self.y:
				tmp = 'y'
			obj.vector(tmp, i)
		return Err.NOOP

	def desc_matrix(self, obj):
		tmp1 = tmp2 = None
		obj.matrix_desc()
		for i in [self.A0, self.A1, self.B0, self.C]:
			if i == self.A0:
				tmp1 = 'A'
				tmp2 = '0'
			if i == self.A1:
				tmp1 = 'A'
				tmp2 = '1'
			if i == self.B0:
				tmp1 = 'B'
				tmp2 = '0'
			if i == self.C:
				tmp1 = 'C'
				tmp2 = ''
				if obj.__class__.__name__ == 'Lat':
					tmp2 = '{}'
			obj.matrix(tmp1, tmp2, i)
		return Err.NOOP

	def description(self, obj):
		obj.begin()
		obj.equation()
		self. desc_vector(obj)
		if obj.__class__.__name__ == 'Mat':
			obj.input_vec(self.u)
			obj.start_vec(self.x)
			obj.values(self.values)
		self.desc_matrix(obj)
		if obj.__class__.__name__ == 'Lat':
			obj.values(self.values)
		if obj.__class__.__name__ == 'Mat':
			obj.adds()
		obj.end()
		return Err.NOOP

	def generatable(self):
		""" return Err.NOOP if it is possible to generate a description """
		if not self.u:
			return Err.ERR_NO_INPUT
		if not self.y:
			return Err.ERR_NO_OUTPUT
		if not self.x:
			return Err.ERR_NO_STATE_VECT
		return Err.NOOP

	def main_work(self):
		self.prepare_vectors()
		if self.parser.args['--vectors']:
			self.show_vectors()
		self.prepare_mapping()
		self.matrix_preparation()
		if self.parser.args['--det3']:
			self.show_det3()
		if self.parser.args['--no-desc']:
			return Err.NOOP
		ans = self.generatable()
		if ans:
			print >> sys.stderr, Err().value_to_name(ans) + ': not enough data to generate description'
			return Err.ERR_NO_DATA
		if self.parser.args['--latex']:
			des = Lat()
		else:
			des = Mat()
		self.description(des)
		return Err.NOOP

	def main(self):
		self.init_parser()
		self.parser.main()
		sys.exit(self.main_work())


if __name__ == '__main__':
	Worker().main()

# eof.
