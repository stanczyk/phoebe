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


class Preparer():
	"""Preparer class"""
	# pylint: disable=missing-docstring

	def __init__(self):
		self.file_handler = None
		self.content_yaml = None
		self.yml = Yml()

	def set_file_handler(self, filename):
		if not filename:
			return Err.ERR_NO_INPUT_FILE
		# print('filename:', filename)
		return self.get_file_handler(filename)

	def get_file_handler(self, filename):
		try:
			self.file_handler = open(filename, 'r')
		except IOError as ioe:
			if ioe.errno == 2:
				return Err.ERR_NO_FILE
			if ioe.errno == 13:
				return Err.ERR_NO_PERMISSION
			return Err.ERR_IO
		return Err.NOOP

	def read_file(self, file_handler):
		try:
			self.content_yaml = self.yml.load(file_handler)
		except yaml.YAMLError as exc:
			print(Err().value_to_name(Err.ERR_YAML) + ': ' + str(exc), file=sys.stderr)
			return Err.ERR_YAML
		return Err.NOOP

	def close_file(self):
		self.file_handler.close()
		self.file_handler = None

	def show_file_content(self, file_name):
		print('== INPUT FILE ==============')
		print('file_name:', file_name)
		print(self.yml.show(self.content_yaml))
		return Err.NOOP

# eof.
