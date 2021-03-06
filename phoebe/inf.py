#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
**info.py**
phoebe implementation: constant, statics and global variables

in the module:

* *class* **Info**

Copyright (c) 2017-2019 Jarosław Stańczyk <jaroslaw.stanczyk@upwr.edu.pl>
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
	VERSION = '0.9.1'

	# used by phoebe
	VER = '' + \
		NAME + \
		' v.' + \
		VERSION
	WRITTEN = '' + \
		'Author: ' + AUTHOR + ' <' + AUTHOR_EMAIL + '>\n' + \
		'Copyright: (c) 2017-2019 ' + AUTHOR

	DOC = '' + \
		'Usage:' + \
		'\t' + NAME + ' [--file] ' + \
		'[--det1] ' + \
		'[--det2] ' + \
		'[--det3] ' + \
		'[--matrices] ' + \
		'[--vectors] ' + \
		'[--latex | --no-desc] ' + \
		'<desc_file>\n' + \
		'\t' + NAME + ' -h | --help\n' + \
		'\t' + NAME + ' -v | --version\n' + \
		'\nOptions:\n' + \
		'  useful during debuging or learning:\n' + \
		'\t--file\t\tshows information from desc_file\n' + \
		'\t--det1\t\tshows parsed information (1) from desc_file\n' + \
		'\t--det2\t\tshows parsed information (2) from desc_file\n' + \
		'\t--det3\t\tshows mapping and parsed matrices\n' + \
		'\t--matrices\tshows max-plus matrices\n' + \
		'\t--vectors\tshows vectors: u(k), x(k) and y(k)\n' + \
		'\t--no-desc\tdescription not generated\n' + \
		'  in everyday use:\n' + \
		'\t--latex\t\tgenerate description for latex (by default matlab model is generated)\n' + \
		'\t-h, --help\tdisplays this help message and exit\n' + \
		'\t-v, --version\tdisplays version information and exit'

	def get_version(self):
		return self.VER + '\n\n' + self.WRITTEN + '\n'

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
