# -*- coding: utf-8 -*-
"""
	**answers.ans_cli.py**

	Copyright (c) 2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
"""
# flake8: noqa
# pylama: ignore=E101

ANS_HLP = '\
Usage: cli [OPTIONS] FILENAME COMMAND [ARGS]...\n\
\n\
  The max-plus algebraic state space model generator. Version 1.0. Copyright:\n\
  (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>\n\
\n\
Options:\n\
  --showfile  Display yaml information from FILENAME.\n\
  --det1      Show parsing information (1).\n\
  --det2      Show parsing information (2).\n\
  --det3      Show mapping and parsed matrices.\n\
  --matrices  Show max-plus model matrices.\n\
  --vectors   Show vectors: u(k), x(k) and y(k)\n\
  -h, --help  Show this message and exit.\n\
\n\
Commands:\n\
  latex   Generate latex description.\n\
  matlab  Generate max-plus matlab model.\n\
'

ANS_FILE = '\
== INPUT FILE ==============\n\
file_name: tests/samples/cli1.yml\n\
input:\n\
- u_1:\n\
    connect: M_1\n\
    tr-time: t_{0,1}\n\
- u_2:\n\
    connect: M_2\n\
    tr-time: t_{0,2}\n\
output:\n\
- y: {}\n\
prod-unit:\n\
- M_1:\n\
    connect: M_3\n\
    op-time: d_1\n\
    tr-time: t_{1,3}\n\
- M_2:\n\
    connect: M_3\n\
    op-time: d_2\n\
    tr-time: t_{2,3}\n\
- M_3:\n\
    connect: y\n\
    op-time: d_3\n\
    tr-time: t_{3,4}\n\
values:\n\
  d_1: 5\n\
  d_2: 6\n\
  d_3: 3\n\
  t_{0,1}: 2\n\
  t_{0,2}: 0\n\
  t_{1,3}: 1\n\
  t_{2,3}: 0\n\
  t_{3,4}: 0\n\
\n\
'

# end.
