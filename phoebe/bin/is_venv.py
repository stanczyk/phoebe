#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	**./bin/is_venv**
	checks whether virtualenv is turned on

	Copyright 2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl
"""
# pylint: disable=no-member
import sys


def is_venv():
	"""
	checks whether virtualenv is turned on

	:return: 0 if virtual env is turned off
	:return: 1 otherwise
	"""
	return hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)


if __name__ == '__main__':
	sys.exit(is_venv())

# eof.
