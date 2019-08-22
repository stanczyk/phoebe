# -*- coding: utf-8 -*-
"""
	**answers.ans_yml.py**

	Copyright (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
"""
# flake8: noqa
# pylama: ignore=E101

YML_ANS = '\
input:\n\
- u_1:\n\
    connect: M_1\n\
    op-time: t_u_1\n\
    tr-time: t_{0,1}\n\
output:\n\
- y_1: {}\n\
prod-unit:\n\
- M_1:\n\
    connect: M_2\n\
    op-time: d_1\n\
    tr-time: t_{1,2}\n\
- M_2:\n\
    connect: M_3\n\
    op-time: d_2\n\
    tr-time: t_{2,3}\n\
- M_3:\n\
    connect: y_1\n\
    op-time: d_3\n\
    tr-time: t_{3,4}\n\
values:\n\
  d_1: 3\n\
  d_2: 2\n\
  d_3: 6\n\
  t_{0,1}: 1\n\
  t_{1,2}: 2\n\
  t_{2,3}: 0\n\
  t_{3,4}: 1\n\
\n'

# end.
