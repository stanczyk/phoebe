#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
**info.py**
phoebe implementation: constant, statics and global variables

in the module:

* *class* **Info**

Copyright 2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl
"""
import time


class Inf(object):
	"""Static info generated by/for battleship"""
	# pylint: disable=too-few-public-methods

	def __init__(self):
		pass

	# used by setup
	AUTHOR = 'Jaroslaw Stanczyk'
	AUTHOR_EMAIL = 'jaroslaw.stanczyk@upwr.edu.pl'
	NAME = 'phoebe'
	DESC = NAME + ' - automatic max-plus description generator'
	LICENSE = 'GNU Affero General Public License v3 or later (AGPLv3+)'
	URL = 'http://gen.up.wroc.pl/stanczyk/'
	# 'https://github.com/stanczyk/phoebe'
	VERSION = '0.2'

	# used by phoebe
	VER = '' + \
		NAME + \
		'  v.' + \
		VERSION
	WRITTEN = '' + \
		'author: ' + AUTHOR + '\n' + \
		'e-mail: ' + AUTHOR_EMAIL + '\n' + \
		'copyright: (c) 2017 ' + AUTHOR

	DOC = '' + \
		'Usage:' + \
		'\t' + NAME + ' [--file] ' + \
		'[--details1] ' + \
		'[--details2] ' + \
		'[--details3] ' + \
		'[--vectors] ' + \
		'[--latex | --no-desc] ' + \
		'<desc_file>\n' + \
		'\t' + NAME + ' -h | --help\n' + \
		'\t' + NAME + ' -v | --version\n' + \
		'\nOptions:\n' + \
		'\t--file\t\tshow information from desc_file\n' + \
		'\t--details1\tshow parsed information (1) from desc_file\n' + \
		'\t--details2\tshow parsed information (2) from desc_file\n' + \
		'\t--details3\tshow mapping and parsed matrices\n' + \
		'\t--vectors\tshow vectors: u(k), x(k) and y(k)\n' + \
		'\t--latex\t\tgenerate description for latex, default is matlab description\n' + \
		'\t--no-desc\tno description generated\n' + \
		'\t-h, --help\tshows this help message and exit\n' + \
		'\t-v, --version\tshow version information and exit'

	def get_version(self):
		return self.VER + '\n' + self.WRITTEN

	@staticmethod
	def get_time():
		return time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime())


def self_test():
	"""self tests"""
	print 'Inf.VER:'
	print Inf.VER + '\n'
	print 'Inf.DOC:'
	print Inf.DOC


if __name__ == '__main__':
	self_test()

# eof.
