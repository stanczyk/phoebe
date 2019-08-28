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
		vec = []
		tmp = []
		for i in ['input', 'prod-unit', 'output']:
			my_dic = self.yml.get_value(self.content_yaml, i)
			# print(my_dic)
			if i == 'input':
				vec = self.vector_u
			if i == 'prod-unit':
				vec = tmp
			if i == 'output':
				vec = self.vector_y
			for j in range(0, self.yml.get_len(my_dic)):
				vec.append(self.yml.get_key(my_dic[j]))
		for i in range(0, len(tmp)):
			self.vector_x.append('x_{' + str(i + 1) + '}')
		return Err.NOOP

	def show_vectors(self):
		print('== VECTORS =================')
		self.print_vector('u(k)', self.vector_u)
		self.print_vector('x(k)', self.vector_x)
		self.print_vector('y(k)', self.vector_y)
		return Err.NOOP

	@staticmethod
	def print_vector(name, vector):
		print(name + ' = [', end='')
		for _, j in enumerate(vector):
			print(' {0}(k)'.format(j), end = '')
		print(' ]\'' if len(vector) > 1 else ']')
		return Err.NOOP

# eof.
