#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	**yml.py**
	module is a simple wrapper of yaml package

	in the module:

	* *class* **Yml**

	Copyright 2013--2016 Jarek Stanczyk, e-mail: j.stanczyk@hotmail.com
"""
# import yaml
# pip install ruamel.yaml
from ruamel.yaml import YAML


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


#data = {
#	input:
#	[
#		{
#			u: {
#			connect: 1,
#			tr-time: 2,
#			}
#		},
#	]
#}

data = {1: {1: [{1: 1, 2: 2}, {1: 1, 2: 2}], 2: 2}, 2: 42}

# yaml_str = """\
# first_name: Art
# occupation: Architect  # This is an occupation comment
# about: Art Vandelay is a fictional character that George invents...
# """


def self_test():
	"""self tests"""
	import sys

	yaml = YAML()
	# data = yaml.load(yaml_str)
	# data.insert(1, 'last name', 'Vandelay', comment="new key")
	yaml.dump(data, sys.stdout)

	# yml.explicit_start = True
	# yml.dump(data, sys.stdout)
	# yml.indent(sequence=4, offset=2)


if __name__ == '__main__':
	self_test()

# end.
