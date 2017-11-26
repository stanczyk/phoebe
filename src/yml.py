#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	**yml.py**
	module is a simple wrapper of yaml package

	in the module:

	* *class* **Yml**

	Copyright 2013--2016 Jarek Stanczyk, e-mail: j.stanczyk@hotmail.com
"""
import yaml


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


def self_test():
	"""self tests"""
	# TODO self_test not implemented yet
	pass


if __name__ == '__main__':
	self_test()

# end.
