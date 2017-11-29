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


class Parser(object):
	"""Parser class"""
	def __init__(self):
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
			my_dic = self.yaml.get_value(self.content_yaml, i)
			if i == 'input':
				vec = self.u
			if i == 'prod-unit':
				vec = tmp
			if i == 'output':
				vec = self.y
			for j in range(0, self.yaml.get_len(my_dic)):
				vec.append(self.yaml.get_key(my_dic[j]))
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
			my_dic = self.yaml.get_value(self.content_yaml, i)
			for j in range(0, self.yaml.get_len(my_dic)):
				name = self.yaml.get_key(my_dic[j])
				self.mapping[name] = j

	def create_matrix(self, matrix, v1, v2):
		for _ in range(0, self.yaml.get_len(v1)):
			tmp = []
			for __ in range(0, self.yaml.get_len(v2)):
				tmp.append('e')
			matrix.append(tmp)

	def fill_matrix_B0(self, my_dic):
		for i in range(0, self.yaml.get_len(my_dic)):
			key = self.yaml.get_key(my_dic[i])
			int_dic = self.yaml.get_value(my_dic[i], key)
			op_time, connect, tr_time = self.get_details(int_dic)
			if connect:
				j = self.mapping[connect]
				tmp = ''
				if tr_time:
					tmp += tr_time
				if op_time:
					tmp += op_time
				self.B0[i][j] = tmp

	def fill_matrix_A0(self, my_dic):
		for i in range(0, self.yaml.get_len(my_dic)):
			key = self.yaml.get_key(my_dic[i])
			int_dic = self.yaml.get_value(my_dic[i], key)
			op_time, connect, tr_time = self.get_details(int_dic)
			if connect and connect[0] != 'y':
				j = self.mapping[connect]
				tmp = ''
				if tr_time:
					tmp += tr_time
				if op_time:
					tmp += op_time
				self.A0[j][i] = tmp

	def fill_matrix_A1(self, my_dic):
		for i in range(0, self.yaml.get_len(my_dic)):
			key = self.yaml.get_key(my_dic[i])
			int_dic = self.yaml.get_value(my_dic[i], key)
			op_time, _, _ = self.get_details(int_dic)
			if op_time:
				j = self.mapping[key]
				tmp = ''
				if op_time:
					tmp += op_time
				self.A1[j][i] = tmp

	def fill_matrix_C(self, my_dic):
		for i in range(0, self.yaml.get_len(my_dic)):
			key = self.yaml.get_key(my_dic[i])
			int_dic = self.yaml.get_value(my_dic[i], key)
			op_time, connect, tr_time = self.get_details(int_dic)
			if connect and connect[0] == 'y':
				j = self.mapping[connect]
				tmp = ''
				if tr_time:
					tmp += tr_time
				if op_time:
					tmp += op_time
				self.C[j][i] = tmp

	def matrix_preparation(self):
		self.create_matrix(self.B0, self.x, self.u)
		self.fill_matrix_B0(self.yaml.get_value(self.content_yaml, 'input'))
		prod_unit = self.yaml.get_value(self.content_yaml, 'prod-unit')
		self.create_matrix(self.A0, self.x, self.x)
		self.fill_matrix_A0(prod_unit)
		self.create_matrix(self.A1, self.x, self.x)
		self.fill_matrix_A1(prod_unit)
		self.create_matrix(self.C, self.y, self.x)
		self.fill_matrix_C(prod_unit)

	def show_matrices(self):
		print '== MATRICES ================'
		for i in [self.A0, self.A1, self.B0, self.C]:
			print i

	def parse(self):
		"""
		main function of phoebe.
		"""
		if self.read_file():
			return Err.ERR_IO
		if self.args['--file']:
			self.show_file_content()
		if self.args['--details-1']:
			self.show_read_details_1()
		if self.args['--details-2']:
			self.show_read_details_2()
		self.prepare_vectors()
		if self.args['--vectors']:
			self.show_vectors()
		self.prepare_mapping()
		self.matrix_preparation()
		self.show_matrices()

		return Err.NOOP

	def main_cli(self):
		self.set_up_argv()
		err = self.set_up_file_handler()
		if not err:
			# parse file
			err = self.parse()
			if err:
				return err
			# clean up
			self.tear_down_cli()
		return err

	def tear_down_cli(self):
		if self.file_name:
			self.file_handler.close()

	@staticmethod
	def get_err_description(error_code):
		return Err().value_to_name(error_code)

	@staticmethod
	def get_version():
		return Inf().VER + '\n' + Inf().WRITTEN

	def epilog(self, err):
		pass

	def main(self):
		err = self.main_cli()
		self.epilog(err)
		sys.exit(err)


if __name__ == '__main__':
	Parser().main()

# eof.
