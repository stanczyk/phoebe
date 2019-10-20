#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
**pre.py**
phoebe implementation - preparation

in the module:
* *class* **Preparer**

Copyright (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
"""
# pylint: disable=import-error

import os
import sys
import numbers
from builtins import IOError, KeyError, str, range, len, enumerate, staticmethod, isinstance, sorted, int

import yaml
from err import Err
from yml import Yml


class Preparer:
	"""Preparer class"""
	# pylint: disable=missing-docstring

	def __init__(self):
		self.file_handler = None
		self.file_name = ''
		self.content_yaml = None
		self.yml = Yml()
		self.vector_u = []
		self.vector_x = []
		self.vector_y = []
		self.A = [[], []] 	# [[A0], [A1]]
		self.B = [[], []] 	# [[B0]]
		self.C = [] 		# [C]
		self.D = None 		# [D]
		self.mapping = {}
		self.values = None

	def set_file_handler(self, filename):
		if not filename:
			return Err.ERR_NO_INPUT_FILE
		self.file_name = filename
		try:
			self.file_handler = open(filename, 'r')
		except IOError as ioe:
			if ioe.errno == 2:
				return Err.ERR_NO_FILE
			if ioe.errno == 13:
				return Err.ERR_NO_PERMISSION
			return Err.ERR_IO
		return Err.NOOP

	def read_file(self):
		try:
			self.content_yaml = self.yml.load(self.file_handler)
		except yaml.YAMLError as err:
			print(Err().value_to_name(Err.ERR_YAML) + ': ' + str(err), file=sys.stderr)
			return Err.ERR_YAML
		self.file_handler.close()
		self.file_handler = None
		return Err.NOOP

	def show_file_content(self):
		print('== INPUT FILE ==============')
		print('file_name:', self.file_name)
		print(self.yml.show(self.content_yaml))
		return Err.NOOP

	def prepare(self):
		self.prepare_vectors()
		self.add_defaults()
		self.prepare_mapping()
		self.matrix_preparation()
		return Err.NOOP

	def prepare_vectors(self):
		vec = None
		name = None
		for i in ['input', 'prod-unit', 'output']:
			if i == 'input':
				vec = self.vector_u
				name = 'u_'
			if i == 'prod-unit':
				vec = self.vector_x
				name = 'x_'
			if i == 'output':
				vec = self.vector_y
				name = 'y_'
			self.prepare_vector(i, vec, name)
		return Err.NOOP

	def prepare_vector(self, select, vec, name):
		vec1 = []
		my_dic = self.yml.get_value(self.content_yaml, select)
		# print(my_dic)
		for i in range(0, self.yml.get_len(my_dic)):
			vec1.append(self.yml.get_key(my_dic[i]))
		# print(vec)
		for i in range(0, len(vec1)):
			if len(vec1) < 10:
				vec.append(name + str(i + 1))
			else:
				vec.append(name + '{' + str(i + 1) + '}')
		return Err.NOOP

	def show_vectors(self):
		print('== VECTORS =================')
		self.print_vector('u(k)', self.vector_u)
		self.print_vector('x(k)', self.vector_x)
		self.print_vector('y(k)', self.vector_y)
		print()
		return Err.NOOP

	@staticmethod
	def print_vector(name, vector):
		print(name + ' = [', end='')
		for _, j in enumerate(vector):
			print(' {0}(k)'.format(j), end='')
		print(' ]\'' if len(vector) > 0 else ']')
		return Err.NOOP

	def add_defaults(self):
		for i in ['input', 'prod-unit', 'output']:
			dic1 = self.yml.get_value(self.content_yaml, i)
			for j in range(0, self.yml.get_len(dic1)):
				key = self.yml.get_key(dic1[j])
				dic2 = self.yml.get_value(dic1[j], key)
				op_time, connect = self.get_det1(dic2)
				if not connect:
					continue
				if not op_time:
					dic2['op-time'] = '0'
				# if type(connect) is dict:
				if isinstance(connect, dict):
					for key in connect:
						dic3 = connect[key]
						if dic3:
							tr_time, buffers = self.get_det2(dic3)
							if not tr_time:
								dic3['tr-time'] = '0'
							if buffers is None:
								dic3['buffers'] = '-'
							elif buffers == 0:
								dic3['buffers'] = '0'
						else:
							connect[key] = {'tr-time': '0', 'buffers': '-'}
				else:
					tr_time, buffers = self.get_det2(dic2)
					if tr_time or tr_time == 0:
						del dic2['tr-time']
					if not tr_time:
						tr_time = '0'
					if buffers or buffers == 0:
						del dic2['buffers']
					if buffers is None:
						buffers = '-'
					elif buffers == 0:
						buffers = '0'
					dic2['connect'] = {connect: {'tr-time': tr_time, 'buffers': buffers}}
		return Err.NOOP

	def get_det1(self, int_dic):
		op_time = self.yml.get_value(int_dic, 'op-time')
		connect = self.yml.get_value(int_dic, 'connect')
		return op_time, connect

	def get_det2(self, int_dic):
		tr_time = self.yml.get_value(int_dic, 'tr-time')
		buffers = self.yml.get_value(int_dic, 'buffers')
		return tr_time, buffers

	def show_det1(self):
		print('== DETAILS 1 ===============')
		for i in ['input', 'prod-unit', 'output', 'values']:
			print(i + ': ', end='')
			print(self.yml.get_value(self.content_yaml, i))
		print()
		return Err.NOOP

	def show_det2(self):
		print('== DETAILS 2 ===============')
		for i in ['input', 'prod-unit', 'output']:
			print(i + ': ')
			dic1 = self.yml.get_value(self.content_yaml, i)
			for j in range(0, self.yml.get_len(dic1)):
				key = self.yml.get_key(dic1[j])
				print('  ' + key)
				dic2 = self.yml.get_value(dic1[j], key)
				op_time, connect = self.get_det1(dic2)
				print('    op-time: ' + (str(op_time) if op_time else '-'))
				print('    connect:', end='')
				if connect:
					print()
					for key in connect:
						print('     ', key)
						dic3 = connect[key]
						if dic3:
							tr_time, buffers = self.get_det2(dic3)
							print('        tr-time: ' + (str(tr_time) if tr_time else '-'))
							print('        buffers: ' + (str(buffers) if buffers else '-'))
				else:
					print(' -')
		i = 'values'
		my_dic = self.yml.get_value(self.content_yaml, i)
		if my_dic:
			print(i + ':')
			for key in sorted(my_dic):
				print('  %s: %s' % (key, my_dic[key]))
		print()
		return Err.NOOP

	def show_matrices(self):
		name = ''
		print('== MATRICES ================')
		for i in [self.A, self.B, self.C, self.D]:
			if i in [self.A, self.B]:
				for j in range(0, len(i)):
					if i == self.A:
						name = 'A' + str(j) + ' = '
					else:
						name = 'B' + str(j) + ' = '
					print(name, end='')
					self.prn_matrix(i[j])
			else:
				if i == self.C:
					name = 'C  = '
				if i == self.D:
					name = 'D  = '
				print(name, end='')
				self.prn_matrix(i)
		print()
		return Err.NOOP

	@staticmethod
	def prn_matrix(matrix):
		if matrix:
			print('[')
			for _, j in enumerate(matrix):
				print(j)
			print(']')
		else:
			print('[]')

	def prepare_mapping(self):
		for i in ['input', 'prod-unit', 'output']:
			my_dic = self.yml.get_value(self.content_yaml, i)
			for j in range(0, self.yml.get_len(my_dic)):
				name = self.yml.get_key(my_dic[j])
				self.mapping[name] = j
		i = 'values'
		my_dic = self.yml.get_value(self.content_yaml, i)
		if my_dic:
			self.values = my_dic
		return Err.NOOP

	def matrix_preparation(self):
		we = self.yml.get_value(self.content_yaml, 'input')
		sy = self.yml.get_value(self.content_yaml, 'prod-unit')
		wy = self.yml.get_value(self.content_yaml, 'output')

		# matrix A
		for i in range(0, len(self.A)):
			self.create_matrix(self.A[i], self.vector_x, self.vector_x)
			self.fill_matrix(self.A[i], sy)
		self.add_feedback_x(self.A[1], sy, wy)
		self.add_feedback_u(self.A[1], we, sy, wy)
		self.add_buffers(self.A, sy)

		# matrix B
		self.create_matrix(self.B[0], self.vector_x, self.vector_u)
		for i in range(1, len(self.B)):
			self.create_matrix(self.B[i], self.vector_x, self.vector_u)
			self.fill_matrix(self.B[i], we)

		# matrix C
		self.create_matrix(self.C, self.vector_y, self.vector_x)
		self.fill_matrix(self.C, sy)

		# matrix D
		if self.D is None:
			self.D = []
		self.create_matrix(self.D, self.vector_y, self.vector_u)
		# TODO tu jeszcze nie jest zrobione dla self.D
		# self.fill_matrix(self.D, we)

		# polishing
		for i in [self.A, self.B, self.C, self.D]:
			if i == self.A or i == self.B:
				for j in i: # range(0, len(self.A)):
					self.optimize_matrix(j)
			else:
				self.optimize_matrix(i)
		return Err.NOOP

	@staticmethod
	def create_matrix(matrix, v1, v2):
		for _ in range(0, len(v1)):
			tmp = []
			for __ in range(0, len(v2)):
				tmp.append('-')
			matrix.append(tmp)
		# self.prn_matrix(matrix)
		return matrix

	def fill_matrix(self, matrix, my_dic):
		for i in range(0, self.yml.get_len(my_dic)):
			key = self.yml.get_key(my_dic[i])
			op_time, connect = self.get_det1(self.yml.get_value(my_dic[i], key))
			tmp = []
			if op_time:
				tmp.append(op_time)
			self.fill_(matrix, i, connect, tmp)
			if matrix == self.A[1]:
				if op_time:
					j = self.mapping[key]
					matrix[j][i] = tmp
				self.fill_(matrix, i, connect, tmp)
		return matrix

	def fill_(self, matrix, iteration, con, val):  # noqa: C901
		if con:
			for key in con:
				tr_time, buffers = self.get_det2(con[key])
				j = self.mapping[key]
				if key[0] != 'y':
					if matrix in [self.A[0], self.B[1]]:
						cell = val[:]
						if tr_time:
							cell.append(str(tr_time))
						matrix[j][iteration] = cell
					#if matrix in [self.A[1]]:
					#	if buffers == '0':
					#		if tr_time == '0':
					#			matrix[iteration][j] = ['0']
					#		else:
					#			matrix[iteration][j] = ['-' + tr_time]
				else:
					if matrix in [self.C]:
						if tr_time:
							val.append(str(tr_time))
						matrix[j][iteration] = val
		return matrix

	def optimize_matrix(self, matrix):
		if not matrix:
			return matrix
		self.rm_repeated_zeros(matrix)
		self.rm_redundant_zeros(matrix)
		return matrix

	def rm_repeated_zeros(self, matrix):
		""" 0, 0, 0 -> 0 """
		# pylint: disable=consider-using-enumerate
		if not matrix:
			return matrix
		w1, w2 = self.yml.get_matrix_size(matrix)
		for i in range(0, w1):
			for j in range(0, w2):
				if matrix[i][j] != '-':
					tmp = matrix[i][j]
					# print(tmp)
					for k in range(0, len(tmp)):
						if tmp[k] == '0' and tmp.count(tmp[k]) > 1:
							tmp[k] = None
					for _ in range(0, tmp.count(None)):
						tmp.remove(None)
		return matrix

	def rm_redundant_zeros(self, matrix):
		""" 0, d_1 -> d1 """
		if not matrix:
			return matrix
		w1, w2 = self.yml.get_matrix_size(matrix)
		for i in range(0, w1):
			for j in range(0, w2):
				if matrix[i][j] != '-':
					tmp = matrix[i][j]
					if len(tmp) > 1 and tmp.count('0'):
						tmp.remove('0')
		return matrix

	def add_feedback_x(self, matrix, system, output):
		for i in range(0, self.yml.get_len(output)):
			key1 = self.yml.get_key(output[i])
			op_time, connect = self.get_det1(self.yml.get_value(output[i], key1))
			if connect:
				for key in connect:
					if key[0].upper() != 'U':
						tmp = []
						if op_time:
							tmp.append(op_time)
						# tr_time, buffers = self.get_det2(connect[key])
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
		for i in range(0, self.yml.get_len(wy)):
			key1 = self.yml.get_key(wy[i])
			# print 'key1:', key1
			# print sy
			key0, opt = self.get_det3(sy, key1)
			# print 'key0, opt:', key0, opt
			op_time, con1 = self.get_det1(self.yml.get_value(wy[i], key1))
			# print op_time, con1
			if con1:
				for key2 in con1:
					if key2[0].upper() == 'U':
						tmp = []
						if op_time:
							tmp.append(op_time)
						tr_time, _ = self.get_det2(con1[key2])
						if tr_time:
							tmp.append(tr_time)
						for j in range(0, self.yml.get_len(we)):
							key3 = self.yml.get_key(we[j])
							if key3 == key2:
								op_time, con2 = self.get_det1(self.yml.get_value(we[j], key2))
								if op_time:
									tmp.append(op_time)
								for key4 in con2:
									tr_time, _ = self.get_det2(con2[key4])
									if tr_time:
										tmp.append(tr_time)
									idx1 = self.mapping[key4]
									tmp.extend(opt)
									idx2 = self.mapping[key0]
									matrix[idx1][idx2] = tmp
		return matrix

	def get_det3(self, system, key):
		for i in range(0, self.yml.get_len(system)):
			key1 = self.yml.get_key(system[i])
			op_time, con1 = self.get_det1(self.yml.get_value(system[i], key1))
			# print op_time, con1, key
			if con1:
				tmp = []
				# print con1
				for key2 in con1:
					if key == key2:
						tmp.append(op_time)
						tr_time, _ = self.get_det2(self.yml.get_value(con1, key))
						if tr_time != '0':
							tmp.append(tr_time)
						return key1, tmp
		return None, None

	def show_det3(self):
		print('== DETAILS 3 ===============')
		print('mapping: ', end='')
		print(self.mapping)
		print('values: ', end='')
		print(self.values)
		print()
		return Err.NOOP

	def get_x_value(self, key, my_dic):
		for i in range(0, self.yml.get_len(my_dic)):
			key1 = self.yml.get_key(my_dic[i])
			op_time, connect = self.get_det1(self.yml.get_value(my_dic[i], key1))
			if connect:
				for key2 in connect:
					if key2 == key:
						return key1, i, op_time
		return None, None, None

	def generatable(self):
		""" return Err.NOOP if it is possible to generate a description """
		if not self.vector_u:
			return Err.ERR_NO_INPUT
		if not self.vector_y:
			return Err.ERR_NO_OUTPUT
		if not self.vector_x:
			return Err.ERR_NO_STATE_VECT
		return Err.NOOP

	def matrices_desc(self, obj):
		if not obj:
			return Err.ERR_NO_DATA
		obj.matrix_desc()
		for i in [self.A, self.B, self.C, self.D]:
			if i == self.A or i == self.B:
				if i == self.A:
					name = 'A'
				else:
					name = 'B'
				for j in range(0, len(i)):
					if i[j]:
						index = str(j)
						obj.matrix(name, index, i[j])
			if i == self.C or i == self.D:
				if i == self.C:
					name = 'C'
				else:
					name = 'D'
				index = ''
				if obj.__class__.__name__ == 'Lat':
					index = '{}'
				obj.matrix(name, index, i)
		return Err.NOOP

	def description(self, obj):
		if not obj:
			return Err.ERR_NO_DATA
		obj.header(os.path.splitext(os.path.basename(self.file_name))[0])
		obj.preface()
		obj.equation(self.A, self.B, self.C, self.D)
		obj.vectors(self.vector_u, self.vector_x, self.vector_y)
		obj.inits(self.vector_u, self.vector_x, self.values)
		self.matrices_desc(obj)
		obj.adds()
		obj.end()
		return Err.NOOP

	def add_buffers(self, matA, system):
		if not matA:
			return Err.ERR_NO_MATRIX
		if not system:
			return Err.ERR_NO_DATA
		for i in range(0, self.yml.get_len(system)):
			key1 = self.yml.get_key(system[i])
			_, connect = self.get_det1(self.yml.get_value(system[i], key1))
			if connect:
				for key2 in connect:
					tr_time, buffer = self.get_det2(connect[key2])
					if buffer and buffer != '-':
						# idx = numerical value of the buffer capacity
						#if isinstance(buffer, numbers.Number):
						#	idx = buffer
						if isinstance(buffer, str):
							try:
								idx = self.values[buffer]
							except KeyError:
								idx = int(buffer)
						else:
							idx = buffer
						# checking if an appropriate A matrix exists
						for j in range(len(matA)-1, idx+1):
							matA.append([])
						if not matA[idx+1]:
							self.create_matrix(matA[idx+1], self.vector_x, self.vector_x)
						cell = matA[idx+1][self.mapping[key1]][self.mapping[key2]]
						tmp = tr_time
						if tr_time != '0':
							tmp = '-' + str(tr_time)
						if cell == '-':
							cell = [tmp]
						else:
							cell.append(tmp)
						matA[idx + 1][self.mapping[key1]][self.mapping[key2]] = cell
		return Err.NOOP

# eof.
