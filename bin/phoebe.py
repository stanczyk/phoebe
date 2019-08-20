#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
**phoebe**
phoebe launcher (and wrapper)

Copyright (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
"""
# pylint: disable=missing-docstring

import os
import sys
import importlib


def set_path():
	lib_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../phoebe')
	if lib_path not in sys.path:
		sys.path.append(lib_path)


def start():
	lib = importlib.import_module('cli')
	lib.main()


if __name__ == '__main__':
	set_path()
	start()

# eof.
