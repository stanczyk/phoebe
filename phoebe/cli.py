#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
**cli.py**
phoebe implementation: command line interface

Copyright (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
"""
# pylint: disable=import-error

import click
import sys
from pre import Preparer
from err import Err


@click.group(context_settings={'help_option_names': ['-h', '--help']}, invoke_without_command=True)
@click.option('--showfile', is_flag=True, help='Display yaml information from FILENAME.')
@click.option('--det1', is_flag=True, help='Show parsing information (1).')
@click.option('--det2', is_flag=True, help='Show parsing information (2).')
@click.option('--det3', is_flag=True, help='Show mapping and parsed matrices.')
@click.option('--matrices', is_flag=True, help='Show max-plus model matrices.')
@click.option('--vectors', is_flag=True, help='Show vectors: u(k), x(k) and y(k)')
@click.argument('filename')
@click.pass_context
def cli(ctx, showfile, det1, det2, det3, matrices, vectors, filename):
	"""
	The max-plus algebraic state space model generator. Version 1.0.
	Copyright: (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
	"""
	ctx.obj = Preparer()
	ans = ctx.obj.set_file_handler(filename)
	if ans != Err().NOOP:
		print('Input file error (' + str(ans) + '): ' + Err().value_to_name(ans), file=sys.stderr)
		return ans
	ans = ctx.obj.read_file()
	if ans != Err().NOOP:
		print('Input file content error (' + str(ans) + '): ' + Err().value_to_name(ans), file=sys.stderr)
		return ans
	if showfile:
		ctx.obj.show_file_content(filename)
	if det1:
		# TODO
		pass
	if det2:
		# TODO
		pass
	if det3:
		# TODO
		pass
	if matrices:
		# TODO
		pass
	if vectors:
		ctx.obj.prepare_vectors()
		ctx.obj.show_vectors()
	# default action
	# if not ctx.invoked_subcommand:
	# 	print('main stuff')


@click.command()
@click.pass_obj
def latex(lat):
	"""Generate latex description."""
	# TODO
	print('hej hopla i generuję opis dla latexa')


@click.command()
@click.pass_obj
def matlab(mat):
	"""Generate max-plus matlab model."""
	# TODO
	print('hej hopla i generuję model dla matlaba')


@click.command()
@click.pass_context
def help(ctx):
	# pylint: disable=missing-docstring, redefined-builtin
	print(ctx.parent.get_help())


cli.add_command(latex)
cli.add_command(matlab)


def main():
	# pylint: disable=missing-docstring, no-value-for-parameter
	cli()


if __name__ == '__main__':
	main()

# eof.
