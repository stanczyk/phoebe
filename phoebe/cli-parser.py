#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
**cli_parser.py**
phoebe implementation

Copyright (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
"""

import click
"""
import os
import sys

from err import Err
from parser import Parser
from latex import Lat
from matlab import Mat

@click.command()
@click.option('-v', '--version', is_flag=True, help='Displays version information and exit.')
@click.option('--file', is_flag=True, help='Show information from FILENAME.')
@click.option('--dont', is_flag=True, help='State space model is not generated.')
@click.argument('filename')
def get_cmdline_params(version, file, dont, filename):
	
	The max-plus algebraic state space model generator.\n
	Copyright: (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
	
	if version:
		click.echo("We are in the verbose mode.")
	print("filename ", filename)
	print("file ", file)
	print("gen ", dont)
"""


@click.group()
def cli1():
	pass


@cli1.command()
@click.option('-v', '--version', is_flag=True, help='Displays version information and exit.')
def cmd1(version):
	if version:
		click.echo("We are in the verbose mode.")


@click.group()
def cli2():
	pass


@cli2.command()
@click.option('--file', is_flag=True, help='Show information from FILENAME.')
@click.option('--dont', is_flag=True, help='State space model is not generated.')
@click.argument('filename')
def cmd2(file, dont, filename):
	"""
	The max-plus algebraic state space model generator.\n
	Copyright: (c) 2017 - 2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
	"""
	print("filename ", filename)
	print("file ", file)
	print("gen ", dont)


cli = click.CommandCollection(sources=[cli1, cli2])


def main():
	cli()
	# proces = Worker()
	# get_cmdline_params()
	# proces.init_parser()
	# proces.parser.main()
	# sys.exit(proces.main_work())


if __name__ == '__main__':
	main()

# eof.
