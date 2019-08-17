#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
**phoebe**
phoebe launcher (and wrapper)

Copyright (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
"""
import os
import sys
import importlib


def set_path():
	LIB_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../phoebe')
	if LIB_PATH not in sys.path:
		sys.path.append(LIB_PATH)


def start():
	lib = importlib.import_module('cli-parser')
	lib.main()


if __name__ == '__main__':
	set_path()
	start()

# eof.
