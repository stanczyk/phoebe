#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
**info.py**
phoebe implementation: constant, statics and global variables

in the module:

* *class* **Info**

Copyright (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
"""
import time


class Inf(object):
	"""Static info generated by/for phoebe"""
	def __init__(self):
		pass

	# used by setup
	AUTHOR = u'Jarosław Stańczyk'
	AUTHOR_EMAIL = 'j.stanczyk@hotmail.com'
	NAME = 'phoebe'
	DESC = 'The max-plus algebraic state space model generator.'
	LICENSE = 'GNU Affero General Public License v3 or later (AGPLv3+)'
	# URL = 'http://gen.up.wroc.pl/stanczyk/'
	# 'https://github.com/stanczyk/phoebe'
	VERSION = '1.0'

	# used by phoebe
	VER = 'Version ' + VERSION
	WRITTEN = '' + \
		'Author: ' + AUTHOR + ' <' + AUTHOR_EMAIL + '>\n' + \
		'Copyright: (c) 2017-2019 ' + AUTHOR

	# DOC = '' + \
	# 	'Usage:' + \
	# 	'\t' + NAME + ' [--file] ' + \
	# 	'[--det1] ' + \
	# 	'[--det2] ' + \
	# 	'[--det3] ' + \
	# 	'[--matrices] ' + \
	# 	'[--vectors] ' + \
	# 	'[--latex | --no-desc] ' + \
	# 	'<desc_file>\n' + \
	# 	'\t' + NAME + ' -h | --help\n' + \
	# 	'\t' + NAME + ' -v | --version\n' + \
	# 	'\nOptions:\n' + \
	# 	'  useful during debuging or learning:\n' + \
	# 	'\t--file\t\tshows information from desc_file\n' + \
	# 	'\t--det1\t\tshows parsed information (1) from desc_file\n' + \
	# 	'\t--det2\t\tshows parsed information (2) from desc_file\n' + \
	# 	'\t--det3\t\tshows mapping and parsed matrices\n' + \
	# 	'\t--matrices\tshows max-plus matrices\n' + \
	# 	'\t--vectors\tshows vectors: u(k), x(k) and y(k)\n' + \
	# 	'\t--no-desc\tdescription not generated\n' + \
	# 	'  in everyday use:\n' + \
	# 	'\t--latex\t\tgenerate description for latex (by default matlab model is generated)\n' + \
	# 	'\t-h, --help\tdisplays this help message and exit\n' + \
	# 	'\t-v, --version\tdisplays version information and exit'

	def get_description(self):
		return self.DESC

	def get_copyright(self):
		return self.WRITTEN

	def get_version(self):
		return self.VER

	@staticmethod
	def get_time():
		return time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime())


def self_test():
	"""self tests"""
	print('Inf.VER:', Inf.VER)

	inf = Inf()
	print('Inf.VER: ' + inf.VER)
	print()
	print(inf.get_description() + ' ' + inf.get_version())
	print(inf.get_copyright())
	print()
	print(inf.get_time())


if __name__ == '__main__':
	self_test()

# eof.
