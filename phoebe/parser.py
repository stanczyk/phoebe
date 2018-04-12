#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
**parser.py**
phoebe implementation

in the module:
* *class* **Parser**

Copyright (c) 2017-2018 Jarosław Stańczyk <jaroslaw.stanczyk@upwr.edu.pl>
"""
import sys
import docopt  # https://pypi.python.org/pypi/docopt/
import yaml
from err import Err
from inf import Inf
from yml import Yml


class Parser(object):
	"""Parser class"""
	# pylint: disable=too-many-branches, too-many-nested-blocks
	def __init__(self):
		self.args = None
		self.file_name = None
		self.file_handler = None
		self.content_yaml = None
		self.yml = None

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
		self.yml = Yml()
		try:
			self.content_yaml = self.yml.load(self.file_handler)
		except yaml.YAMLError as exc:
			print >> sys.stderr, Err().value_to_name(Err.ERR_YAML) + ': ' + str(exc)
			return Err.ERR_YAML
		return Err.NOOP

	def show_file_content(self):
		print 'file name: ', self.file_name
		print '== INPUT FILE =============='
		print self.yml.show(self.content_yaml)
		return Err.NOOP

	def add_defaults(self):  # noqa: C901
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

	def show_det1(self):
		print '== DETAILS 1 ==============='
		for i in ['input', 'prod-unit', 'output', 'values']:
			print i + ':',
			print self.yml.get_value(self.content_yaml, i)

		return Err.NOOP

	def get_det1(self, int_dic):
		op_time = self.yml.get_value(int_dic, 'op-time')
		connect = self.yml.get_value(int_dic, 'connect')
		return op_time, connect

	def get_det2(self, int_dic):
		tr_time = self.yml.get_value(int_dic, 'tr-time')
		buffers = self.yml.get_value(int_dic, 'buffers')
		return tr_time, buffers

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

	def show_det2(self):
		print '== DETAILS 2 ==============='
		for i in ['input', 'prod-unit', 'output']:
			print i + ':'
			dic1 = self.yml.get_value(self.content_yaml, i)
			for j in range(0, self.yml.get_len(dic1)):
				key = self.yml.get_key(dic1[j])
				print '  ' + key
				dic2 = self.yml.get_value(dic1[j], key)
				op_time, connect = self.get_det1(dic2)
				print '    op-time: ' + (op_time if op_time else '-')
				print '    connect:',
				if connect:
					print
					for key in connect:
						print '     ', key
						dic3 = connect[key]
						if dic3:
							tr_time, buffers = self.get_det2(dic3)
							print '        tr-time: ' + (tr_time if tr_time else '-')
							print '        buffers: ' + (buffers if buffers else '-')
				else:
					print '-'
		i = 'values'
		my_dic = self.yml.get_value(self.content_yaml, i)
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
		self.add_defaults()
		if self.args['--det1']:
			self.show_det1()
		if self.args['--det2']:
			self.show_det2()
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
