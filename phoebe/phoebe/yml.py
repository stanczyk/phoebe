#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	**yml.py**
	module is a simple wrapper of yaml package

	in the module:
	* *class* **Yml**

	Copyright 2013--2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl
"""
# pylint: disable=redefined-outer-name, invalid-name
import yaml
from yml_data import DANE
# from ruamel.yaml import YAML


class Yml(object):
	"""
	class to read, parse and store data
	from config file and/or command line interface
	"""
	def __init__(self):
		pass

	@staticmethod
	def load(stream):
		"""
		simple wrapper to use always the safety yaml load function.

		:param stream: stream of data to load
		"""
		return yaml.safe_load(stream)

	@staticmethod
	def dump(data, **kwargs):
		"""
		Simple wrapper to use the safety yaml dump function.

		:param data: data to yaml dump
		:param kwargs: some kwargs dict
		"""
		return yaml.safe_dump(data, **kwargs)

	def show(self, data):
		"""
		show data

		:param data: data to show
		"""
		return self.dump(data)

	@staticmethod
	def get_value(my_dict, key, default=None):
		"""
		smart access to a dictionary with key.
		if the key is not in the dictionary it returns default value.

		:param dict my_dict: dictionary to parse
		:param key: key to find appropriate data
		:param default: default return value
		"""
		if not my_dict:
			return default
		if not key:
			return default
		try:
			return my_dict[key]
		except KeyError:
			return default

	@staticmethod
	def get_key(my_dict, default=None):
		"""
		:param my_dict:
		:param default:
		:return:
		"""
		if not my_dict:
			return default
		try:
			for key, _ in my_dict.iteritems():
				return key
		except AttributeError:
			return default

	@staticmethod
	def get_len(my_dict):
		"""
		:param my_dict:
		:return:
		"""
		if not my_dict:
			return -1
		# if not isinstance(my_dict, dict):
		# if type(my_dict) is dict:
		return len(my_dict)

	@staticmethod
	def get_matrix_size(matrix):
		if not matrix:
			return None, None
		w1 = len(matrix)
		tmp = matrix[0]
		w2 = len(tmp)
		return w1, w2


def self_test():
	"""self tests"""
	yaml = Yml()
	print yaml.dump(DANE)


if __name__ == '__main__':
	self_test()

# end.
