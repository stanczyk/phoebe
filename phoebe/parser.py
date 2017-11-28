#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
**parser.py**
phoebe implementation

in the module:
* *class* **Parser**

Copyright 2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl
"""
# pylint: disable=relative-import, missing-docstring
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

	def parse(self):
		"""
		main function of phoebe.
		"""
		yam = Yml()
		try:
			self.content_yaml = yam.load(self.file_handler)
		except yaml.YAMLError as exc:
			print Err().value_to_name(Err.ERR_YAML) + ": " + str(exc)
			# print(exc)
			return Err.ERR_YAML
		print '== WCZYTANY PLIK: =========='
		print yam.show(self.content_yaml)

		print '== POSZCZEGÓLNE ELEMENTY1 =='
		print 'input:'
		print yam.get_value(self.content_yaml, 'input')
		print 'prod-unit:'
		print yam.get_value(self.content_yaml, 'prod-unit')
		print 'output:'
		print yam.get_value(self.content_yaml, 'output')

		print '== POSZCZEGÓLNE ELEMENTY2 =='
		print 'input:'
		my_dic = yam.get_value(self.content_yaml, 'input')
		for i in range(0, yam.get_len(my_dic)):
			key = yam.get_key(my_dic[i])
			print '  ' + key
			my_internal_dic = yam.get_value(my_dic[i], key)
			print '    op-time: ' + yam.get_value(my_internal_dic, 'op-time', '0')
			print '    connect: ' + yam.get_value(my_internal_dic, 'connect', 'no')
			print '    tr-time: ' + yam.get_value(my_internal_dic, 'tr-time', '0')
		print 'prod-unit:'
		my_dic = yam.get_value(self.content_yaml, 'prod-unit', None)
		for i in range(0, yam.get_len(my_dic)):
			key = yam.get_key(my_dic[i])
			print '  ' + key
			my_internal_dic = yam.get_value(my_dic[i], key)
			print '    op-time: ' + yam.get_value(my_internal_dic, 'op-time', '0')
			print '    connect: ' + yam.get_value(my_internal_dic, 'connect', 'no')
			print '    tr-time: ' + yam.get_value(my_internal_dic, 'tr-time', '0')
		print 'output:'
		my_dic = yam.get_value(self.content_yaml, 'output', None)
		for i in range(0, yam.get_len(my_dic)):
			key = yam.get_key(my_dic[i])
			print '  ' + key
			my_internal_dic = yam.get_value(my_dic[i], key)
			print '    op-time: ' + yam.get_value(my_internal_dic, 'op-time', '0')
			print '    connect: ' + yam.get_value(my_internal_dic, 'connect', 'no')
			print '    tr-time: ' + yam.get_value(my_internal_dic, 'tr-time', '0')

		print '== KONIEC =================='
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
