#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
**err.py**
error messages and values

in the module:
* *class* **Err**

Copyright (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
"""

# one more then last ERR
ERR_MAX_NUMBER = 10


class Err(object):
	"""Errors code and description"""
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
		ERR_NO_DATA,  # lack or not enough input data
		ERR_NO_INPUT,
		ERR_NO_OUTPUT,
		ERR_NO_STATE_VECT
	] = range(ERR_MAX_NUMBER)

	def value_to_name(self, value):
		"""
		based on given class, changes the value to the defined name in dictionary

		:param value: value to convert
		:return: name of the value as a string
		"""
		for name, val in self.__class__.__dict__.items():
			if val == value:
				return name
		raise ValueError('Unknown value: %r' % value)

	def get_err_description(self, error_code):
		return self.value_to_name(error_code)

	def self_test(self):
		"""self test for Err class"""
		for i in range(ERR_MAX_NUMBER):
			print('%d: %s' % (i, self.value_to_name(i)))


if __name__ == '__main__':
	err = Err()
	err.self_test()

# eof.
