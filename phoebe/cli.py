#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
**cli-parser.py**
phoebe implementation

Copyright (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
"""

import click


@click.group(context_settings={'help_option_names': ['-h', '--help']})
# @click.option('--file', is_flag=True, help='Show information from FILENAME.')
# @click.option('--dont', is_flag=True, help='State space model is not generated.')
# @click.argument('filename')
# def get_cmdline_params(version, file, dont, filename):
# 	"""
# 	The max-plus algebraic state space model generator.\n
# 	Copyright: (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
# 	"""
# 	if version:
# 		click.echo("We are in the verbose mode.")
# 	print("filename ", filename)
# 	print("file ", file)
# 	print("gen ", dont)


def cli():
	"""My very cool command-line tool"""
	pass


@click.command()
def dosomething():
	"""Do Something."""
	dosomething()


cli.add_command(dosomething)


@click.command()
@click.pass_context
def help(ctx):
	print(ctx.parent.get_help())


def main():
	cli()


if __name__ == '__main__':
	main()

# eof.
