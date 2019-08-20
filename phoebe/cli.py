#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
**cli.py**
phoebe implementation: command line interface

Copyright (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
"""
# pylint: disable=import-error

import click
from pre import Preparer
from err import Err


@click.group(context_settings={'help_option_names': ['-h', '--help']}, invoke_without_command=True)
@click.option('--showfile', is_flag=True, help='Show information from FILENAME.')
# @click.option('--dont', is_flag=True, help='State space model is not generated.')
@click.argument('filename')
@click.pass_context
def cli(ctx, showfile, filename):
	"""
	The max-plus algebraic state space model generator. Version 1.0.
	Copyright: (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
	"""
	ctx.obj = Preparer()
	if ctx.obj.set_file_handler(filename) == Err().NOOP:
		ctx.obj.read_file(ctx.obj.file_handler)
		ctx.obj.close_file()
	if showfile:
		ctx.obj.show_file_content(filename)


@click.command()
@click.pass_obj
def dosomething(prep):
	"""Do Something."""
	print('hej hopla')
	prep.tada()


cli.add_command(dosomething)


@click.command()
@click.pass_context
def help(ctx):
	# pylint: disable=missing-docstring, redefined-builtin
	print(ctx.parent.get_help())


def main():
	# pylint: disable=missing-docstring, no-value-for-parameter
	cli()


if __name__ == '__main__':
	main()

# eof.
