#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	**yml.py**
	module is a simple wrapper of yaml package

	in the module:
	* *class* **Yml**

	Copyright 2013--2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl
"""
# pylint: disable=bad-continuation, redefined-outer-name
import yaml
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
		if not isinstance(my_dict, dict):
			return -1
		return len(my_dict)


DATA = {
	# input definition
	'input':
	[
		{
			# input u_1
			'u_1':
				{
					'op-time': 't_u_1',
					# the time after which the item is delivered to the input, default: 0 (available immediately)
					# there is no need to define this value if it is equal to the default

					'connect': 'M_1',
					# to which system item (processing unit or output) the input is connected

					'tr-time': 't_{0,1}'
					# transport time from input to system item
				}
		}
	],
	# prod-unit definition
	'prod-unit':
	[
		{
			# production unit M_1
			'M_1':
			{
				'op-time': 'd_1',
				# operation time on M_1

				'connect': 'M_2',
				# to which system item (processing unit or output) this processing unit is connected

				'tr-time': 't_{1,2}'
				# transport time from input to system item
			}
		},
		{
			'M_2':
			{
				'op-time': 'd_2',
				'connect': 'M_3',
				'tr-time': 't_{2,3}'
			}
		},
		{
			'M_3':
			{
				'op-time': 'd_3',
				'connect': 'y',
				'tr-time': 't_{3,4}'
			}
		}
	],
	# output definition
	'output':
	[
		'y'
	]
}


def self_test():
	"""self tests"""
	yaml = Yml()
	print yaml.dump(DATA)
	# import sys
	# yaml = YAML()
	# yaml.dump(data, sys.stdout)
	my_dic = yaml.get_value(DATA, 'prod-unit', None)
	print my_dic
	print len(my_dic)
	print my_dic[1]
	print yaml.get_key(my_dic[1], None)


if __name__ == '__main__':
	self_test()

# end.
