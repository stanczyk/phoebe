# -*- coding: utf-8 -*-
"""
	**answers.ans_pre.py**

	Copyright (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
"""
# flake8: noqa
# pylama: ignore=E101

ANS_FILE = '\
== INPUT FILE ==============\n\
file_name: tests/samples/pre2.yml\n\
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

PRE_IMP1 = {
	'input': [{'u_1': {'connect': 'M_1', 'tr-time': 't_{0,1}'}}, {'u_2': {'connect': 'M_2', 'tr-time': 't_{0,2}'}}],
	'prod-unit': [{'M_1': {'connect': 'M_3', 'op-time': 'd_1', 'tr-time': 't_{1,3}'}},
				  {'M_2': {'connect': 'M_3', 'op-time': 'd_2', 'tr-time': 't_{2,3}'}},
				  {'M_3': {'connect': 'y', 'op-time': 'd_3', 'tr-time': 't_{3,4}'}}],
	'output': [{'y': {}}],
	'values': {'t_{0,1}': 2, 't_{0,2}': 0, 't_{1,3}': 1, 't_{2,3}': 0, 't_{3,4}': 0, 'd_1': 5, 'd_2': 6, 'd_3': 3}
}

PRE_ANS1 = ['x_1', 'x_2', 'x_3']

PRE_VEC1 = '\
== VECTORS =================\n\
u(k) = []\n\
x(k) = []\n\
y(k) = []\n\
\n'

PRE_VEC2 = '\
== VECTORS =================\n\
u(k) = [ u_1(k) u_2(k) ]\'\n\
x(k) = [ x_1(k) x_2(k) x_3(k) ]\'\n\
y(k) = [ y_1(k) ]\'\n\
\n'

# end.
