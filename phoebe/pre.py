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

# eof.
