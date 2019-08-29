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

import sys
import yaml
from err import Err
from yml import Yml


class Preparer:
	"""Preparer class"""
	# pylint: disable=missing-docstring

	def __init__(self):
		self.file_handler = None
		self.content_yaml = None
		self.yml = Yml()
		self.vector_u = []
		self.vector_x = []
		self.vector_y = []
		self.A = [[], []] 	# [A0, A1]
		self.B = [] 		# [B0]
		self.C = [] 		# [C]

	def set_file_handler(self, filename):
		if not filename:
			return Err.ERR_NO_INPUT_FILE
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

	def show_file_content(self, file_name):
		print('== INPUT FILE ==============')
		print('file_name:', file_name)
		print(self.yml.show(self.content_yaml))
		return Err.NOOP

	def prepare_vectors(self):
		for i in ['input', 'prod-unit', 'output']:
			self.prepare_vector(i)
		return Err.NOOP

	def prepare_vector(self, select):
		vec1 = []
		vec2 = []
		tmp = ''
		my_dic = self.yml.get_value(self.content_yaml, select)
		# print(my_dic)
		for i in range(0, self.yml.get_len(my_dic)):
			vec1.append(self.yml.get_key(my_dic[i]))
		# print(vec)
		if select == 'input':
			vec2 = self.vector_u
			tmp = 'u_'
		if select == 'prod-unit':
			vec2 = self.vector_x
			tmp = 'x_'
		if select == 'output':
			vec2 = self.vector_y
			tmp = 'y_'
		for i in range(0, len(vec1)):
			if len(vec1) < 10:
				vec2.append(tmp + str(i + 1))
			else:
				vec2.append(tmp + '{' + str(i + 1) + '}')
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
				print('    op-time: ' + (op_time if op_time else '-'))
				print('    connect:', end='')
				if connect:
					print()
					for key in connect:
						print('     ', key)
						dic3 = connect[key]
						if dic3:
							tr_time, buffers = self.get_det2(dic3)
							print('        tr-time: ' + (tr_time if tr_time else '-'))
							print('        buffers: ' + (buffers if buffers else '-'))
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
		for i in [self.A, self.B, self.C]:
			if i == self.A:
				for j in range(0, len(self.A)):
					name = 'A' + str(j) + ' = '
					print(name, end='')
					self.prn_matrix(j)
			else:
				if i == self.B:
					name = 'B0 = '
				if i == self.C:
					name = 'C  = '
				print(name, end='')
				self.prn_matrix(i)
		return Err.NOOP

	@staticmethod
	def prn_matrix(matrix):
		if matrix:
			# print('[')
			for _, j in enumerate(matrix):
				print(j)
			# print(']')
		else:
			print('[]')

# eof.
