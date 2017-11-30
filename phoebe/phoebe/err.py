#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
**err.py**
error messages and values

in the module:
* *class* **Err**

Copyright 2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl
"""
# one more then last ERR
ERR_MAX_NUMBER = 6


class Err(object):
	"""Errors code and description"""
	# pylint: disable=bad-continuation, too-few-public-methods, missing-docstring

	def __init__(self):
		pass

	# error codes:
	[
		NOOP,  # means NO ERROR
		ERR_NO_INPUT_FILE,  # lack file_name
		ERR_NO_FILE,  # no file with given file_name
		ERR_NO_PERMISSION,  # no permission to read file
		ERR_IO,  # IOError
		ERR_YAML,  # error in yaml file
	] = range(ERR_MAX_NUMBER)

	def value_to_name(self, value):
		"""
		based on given class, changes the value to the defined name in dictionary

		:param value: value to convert
		:return: name of the value as a string
		"""
		for name, val in self.__class__.__dict__.iteritems():
			if val == value:
				return name
		raise ValueError('Unknown value: %r' % value)

	# def name_to_value(self, name):
	# 	"""
	# 	based on given class, returns the value of a defined name

	# 	:param class_name: class in which value exists
	# 	:param name: name to convert to value
	# 	:return: value associated with name
	# 	"""
	# 	for nam, val in self.__dict__.iteritems():
	# 		if nam == name:
	# 			return val
	# 	raise ValueError('Unknown name: %r' % name)

	def get_err_description(self, error_code):
		return self.value_to_name(error_code)


def self_test():
	"""self test for Err class"""

	err = Err()
	for i in range(ERR_MAX_NUMBER):
		print '%d: %s' % (i, err.value_to_name(i))


if __name__ == '__main__':
	self_test()

# eof.
