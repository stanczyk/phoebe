#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
**parser.py**
phoebe implementation

in the module:
* *class* **Parser**

Copyright 2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl
"""
# pylint: disable=relative-import
import sys
import docopt  # https://pypi.python.org/pypi/docopt/
import yaml
from err import Err
from inf import Inf
from yml import Yml


class Parser(object):
	"""Parser class"""
	# pylint: disable=missing-docstring, invalid-name, too-many-instance-attributes
	def __init__(self):
		self.args = None
		self.file_name = None
		self.file_handler = None
		self.content_yaml = None
		self.yaml = None
		self.u = []
		self.x = []
		self.y = []
		self.A0 = []
		self.A1 = []
		self.B0 = []
		self.C = []

	def set_up_argv(self):
		# parse command line options
		self.args = docopt.docopt(Inf.DOC, version=self.get_version())
		# print self.args
		if self.args['-v']:
			print self.get_version()
			exit(Err.NOOP)
		self.file_name = self.args['<desc_file>']

	def set_up_file_handler(self):
		if not self.file_name:
			return Err.ERR_NO_INPUT_FILE
		# you read from ordinary file
		return self.get_file_handler()

	def get_file_handler(self):
		try:
			self.file_handler = open(self.file_name, 'r')
		except IOError as ioe:
			if ioe.errno == 2:
				return Err.ERR_NO_FILE
			if ioe.errno == 13:
				return Err.ERR_NO_PERMISSION
			return Err.ERR_IO
		return Err.NOOP

	def read_file(self):
		self.yaml = Yml()
		try:
			self.content_yaml = self.yaml.load(self.file_handler)
		except yaml.YAMLError as exc:
			print >> sys.stderr, Err().value_to_name(Err.ERR_YAML) + ": " + str(exc)
			return Err.ERR_YAML
		return Err.NOOP

	def show_file_content(self):
		print '== INPUT FILE =============='
		print self.yaml.show(self.content_yaml)

	def data_preparation(self):
		for i in ['input', 'prod-unit', 'output']:
			idx = 0
			print i,
			my_dic = self.yaml.get_value(self.content_yaml, i)
			for j in range(0, self.yaml.get_len(my_dic)):
				key = self.yaml.get_key(my_dic[j])
				print key
				my_internal_dic = self.yaml.get_value(my_dic[j], key)
				print my_internal_dic
				my_internal_dic['vec_id'] = idx
				idx += 1
				print my_internal_dic

	def show_read_details_1(self):
		print '== READ DETAILS 1 =========='
		for i in ['input', 'prod-unit', 'output']:
			print i + ':',
			print self.yaml.get_value(self.content_yaml, i)

	def show_read_details_2(self):
		print '== READ DETAILS 2 =========='
		for i in ['input', 'prod-unit', 'output']:
			print i + ':'
			my_dic = self.yaml.get_value(self.content_yaml, i)
			for j in range(0, self.yaml.get_len(my_dic)):
				key = self.yaml.get_key(my_dic[j])
				print '  ' + key
				my_internal_dic = self.yaml.get_value(my_dic[j], key)
				print '    op-time: ' + self.yaml.get_value(my_internal_dic, 'op-time', '0')
				print '    connect: ' + self.yaml.get_value(my_internal_dic, 'connect', 'no')
				print '    tr-time: ' + self.yaml.get_value(my_internal_dic, 'tr-time', '0')

	def prepare_vectors(self):
		vec = []
		tmp = []
		for i in ['input', 'prod-unit', 'output']:
			my_dic = self.yaml.get_value(self.content_yaml, i)
			for j in range(0, self.yaml.get_len(my_dic)):
				if i == 'input':
					vec = self.u
				if i == 'prod-unit':
					vec = tmp
				if i == 'output':
					vec = self.y
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

	def matrix_description(self):
		pass

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

		self.data_preparation()
		self.matrix_description()
		self.show_matrices()

		return Err.NOOP

	def main_cli(self):
		self.set_up_argv()
		err = self.set_up_file_handler()
		if not err:
			# parse file
			err = self.parse()
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
