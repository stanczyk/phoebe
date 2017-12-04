#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
**parser.py**
phoebe implementation

in the module:
* *class* **Parser**

Copyright 2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl
"""
import sys
import docopt  # https://pypi.python.org/pypi/docopt/
import yaml
from err import Err
from inf import Inf
from yml import Yml


class Parser(object):
	"""Parser class"""
	def __init__(self):
		self.args = None
		self.file_name = None
		self.file_handler = None
		self.content_yaml = None
		self.yaml = None

	def set_up_argv(self):
		self.args = docopt.docopt(Inf().DOC, version=Inf().get_version())
		if self.args['-v']:
			print Inf().get_version()
			exit(Err.NOOP)
		self.file_name = self.args['<desc_file>']
		return Err.NOOP

	def set_up_file_handler(self):
		if not self.file_name:
			return Err.ERR_NO_INPUT_FILE
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
			print >> sys.stderr, Err().value_to_name(Err.ERR_YAML) + ': ' + str(exc)
			return Err.ERR_YAML
		return Err.NOOP

	def show_file_content(self):
		print '== INPUT FILE =============='
		print self.yaml.show(self.content_yaml)
		return Err.NOOP

	def show_details1(self):
		print '== DETAILS 1 ==============='
		for i in ['input', 'prod-unit', 'output', 'values']:
			print i + ':',
			print self.yaml.get_value(self.content_yaml, i)
		return Err.NOOP

	def get_details(self, int_dic):
		op_time = self.yaml.get_value(int_dic, 'op-time')
		connect = self.yaml.get_value(int_dic, 'connect')
		tr_time = self.yaml.get_value(int_dic, 'tr-time')
		return op_time, connect, tr_time

	def show_details2(self):
		print '== DETAILS 2 ==============='
		for i in ['input', 'prod-unit', 'output']:
			print i + ':'
			my_dic = self.yaml.get_value(self.content_yaml, i)
			for j in range(0, self.yaml.get_len(my_dic)):
				key = self.yaml.get_key(my_dic[j])
				print '  ' + key
				my_internal_dic = self.yaml.get_value(my_dic[j], key)
				op_time, connect, tr_time = self.get_details(my_internal_dic)
				print '    op-time: ' + (op_time if op_time else '--')
				print '    connect: ' + (connect if connect else '--')
				print '    tr-time: ' + (tr_time if tr_time else '--')
		i = 'values'
		my_dic = self.yaml.get_value(self.content_yaml, i)
		if my_dic:
			print i + ':'
			for key in sorted(my_dic):
				print '  %s: %s' % (key, my_dic[key])
		return Err.NOOP

	def parse(self):
		if self.read_file():
			return Err.ERR_IO
		if self.args['--file']:
			self.show_file_content()
		if self.args['--details1']:
			self.show_details1()
		if self.args['--details2']:
			self.show_details2()
		return Err.NOOP

	def main_cli(self):
		self.set_up_argv()
		err = self.set_up_file_handler()
		if not err:
			err = self.parse()
			self.tear_down_cli()
		return err

	def tear_down_cli(self):
		if self.file_name:
			self.file_handler.close()
		return Err.NOOP

	def main(self):
		err = self.main_cli()
		if err:
			sys.exit(err)
		return Err.NOOP


if __name__ == '__main__':
	Parser().main()

# eof.
