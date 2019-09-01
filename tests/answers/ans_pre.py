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
	'input': [
		{'u_1': {'connect': 'M_1', 'tr-time': 't_{0,1}'}},
		{'u_2': {'connect': 'M_2', 'tr-time': 't_{0,2}'}}],
	'prod-unit': [
		{'M_1': {'connect': 'M_3', 'op-time': 'd_1', 'tr-time': 't_{1,3}'}},
		{'M_2': {'connect': 'M_3', 'op-time': 'd_2', 'tr-time': 't_{2,3}'}},
		{'M_3': {'connect': 'y', 'op-time': 'd_3', 'tr-time': 't_{3,4}'}}],
	'output': [
		{'y': {}}],
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

PRE_CONTENT1 = {'output': [{'y_1': {}}]}

PRE_CONTENT2 = {
	'input': [
		{'u_1': {'connect': {'M_1': {'tr-time': 't_{0,1}', 'buffers': '-'}}, 'op-time': '0'}},
		{'u_2': {'connect': {'M_2': {'tr-time': 't_{0,2}', 'buffers': '-'}}, 'op-time': '0'}}],
	'prod-unit': [
		{'M_1': {'connect': {'M_3': {'tr-time': 't_{1,3}', 'buffers': '-'}}, 'op-time': 'd_1'}},
		{'M_2': {'connect': {'M_3': {'tr-time': 't_{2,3}', 'buffers': '-'}}, 'op-time': 'd_2'}},
		{'M_3': {'connect': {'y': {'tr-time': 't_{3,4}', 'buffers': '-'}}, 'op-time': 'd_3'}}],
	'output': [
		{'y': {}}],
	'values': {'t_{0,1}': 2, 't_{0,2}': 0, 't_{1,3}': 1, 't_{2,3}': 0, 't_{3,4}': 0, 'd_1': 5, 'd_2': 6, 'd_3': 3}}

PRE_DET1_1 = '\
== DETAILS 1 ===============\n\
input: None\n\
prod-unit: None\n\
output: [{\'y_1\': {}}]\n\
values: None\n\
\n'

PRE_DET1_2 = '\
== DETAILS 1 ===============\n\
input: [\
{\'u_1\': {\'connect\': {\'M_1\': {\'tr-time\': \'t_{0,1}\', \'buffers\': \'-\'}}, \'op-time\': \'0\'}}, \
{\'u_2\': {\'connect\': {\'M_2\': {\'tr-time\': \'t_{0,2}\', \'buffers\': \'-\'}}, \'op-time\': \'0\'}}]\n\
prod-unit: [\
{\'M_1\': {\'connect\': {\'M_3\': {\'tr-time\': \'t_{1,3}\', \'buffers\': \'-\'}}, \'op-time\': \'d_1\'}}, \
{\'M_2\': {\'connect\': {\'M_3\': {\'tr-time\': \'t_{2,3}\', \'buffers\': \'-\'}}, \'op-time\': \'d_2\'}}, \
{\'M_3\': {\'connect\': {\'y\': {\'tr-time\': \'t_{3,4}\', \'buffers\': \'-\'}}, \'op-time\': \'d_3\'}}]\n\
output: [\
{\'y\': {}}]\n\
values: \
{\'t_{0,1}\': 2, \'t_{0,2}\': 0, \'t_{1,3}\': 1, \'t_{2,3}\': 0, \'t_{3,4}\': 0, \'d_1\': 5, \'d_2\': 6, \'d_3\': 3}\n\
\n'

PRE_DET2_1 = '\
== DETAILS 2 ===============\n\
input: \n\
prod-unit: \n\
output: \n\
  y_1\n\
    op-time: -\n\
    connect: -\n\
\n'

PRE_DET2_2 = '\
== DETAILS 2 ===============\n\
input: \n\
  u_1\n\
    op-time: 0\n\
    connect:\n\
      M_1\n\
        tr-time: t_{0,1}\n\
        buffers: -\n\
  u_2\n\
    op-time: 0\n\
    connect:\n\
      M_2\n\
        tr-time: t_{0,2}\n\
        buffers: -\n\
prod-unit: \n\
  M_1\n\
    op-time: d_1\n\
    connect:\n\
      M_3\n\
        tr-time: t_{1,3}\n\
        buffers: -\n\
  M_2\n\
    op-time: d_2\n\
    connect:\n\
      M_3\n\
        tr-time: t_{2,3}\n\
        buffers: -\n\
  M_3\n\
    op-time: d_3\n\
    connect:\n\
      y\n\
        tr-time: t_{3,4}\n\
        buffers: -\n\
output: \n\
  y\n\
    op-time: -\n\
    connect: -\n\
values:\n\
  d_1: 5\n\
  d_2: 6\n\
  d_3: 3\n\
  t_{0,1}: 2\n\
  t_{0,2}: 0\n\
  t_{1,3}: 1\n\
  t_{2,3}: 0\n\
  t_{3,4}: 0\n\
\n'

PRE_MAT1 = '\
== MATRICES ================\n\
A0 = []\n\
A1 = []\n\
C  = []\n\
C  = []\n\
\n'

PRE_MATA = [
	[['-', '-', '-'], ['-', '-', '-'], [['d_1', 't_{1,3}'], ['d_2', 't_{2,3}'], '-']],
	[[['d_1'], '-', '-'], ['-', ['d_2'], '-'], ['-', '-', ['d_3']]]]
PRE_MATB = [[['t_{0,1}'], '-'], ['-', ['t_{0,2}']], ['-', '-']]
PRE_MATC = [['-', '-', ['d_3', 't_{3,4}']]]

PRE_MAT2 = '\
== MATRICES ================\n\
A0 = [\n\
[\'-\', \'-\', \'-\']\n\
[\'-\', \'-\', \'-\']\n\
[[\'d_1\', \'t_{1,3}\'], [\'d_2\', \'t_{2,3}\'], \'-\']\n\
]\n\
A1 = [\n\
[[\'d_1\'], \'-\', \'-\']\n\
[\'-\', [\'d_2\'], \'-\']\n\
[\'-\', \'-\', [\'d_3\']]\n\
]\n\
B0 = [\n\
[[\'t_{0,1}\'], \'-\']\n\
[\'-\', [\'t_{0,2}\']]\n\
[\'-\', \'-\']\n\
]\n\
C  = [\n\
[\'-\', \'-\', [\'d_3\', \'t_{3,4}\']]\n\
]\n\
\n'

PRE_MATB2 = '\
[\n\
[[\'t_{0,1}\'], \'-\']\n\
[\'-\', [\'t_{0,2}\']]\n\
[\'-\', \'-\']\n\
]\n'

PRE_MAP1 = {'y_1': 0, 'u_1': 0, 'u_2': 1, 'M_1': 0, 'M_2': 1, 'M_3': 2, 'y': 0}
PRE_MAP2 = {'t_{0,1}': 2, 't_{0,2}': 0, 't_{1,3}': 1, 't_{2,3}': 0, 't_{3,4}': 0, 'd_1': 5, 'd_2': 6, 'd_3': 3}
PRE_DICM = [
	{'M_1': {'connect': {'M_3': {'tr-time': 't_{1,3}', 'buffers': '-'}}, 'op-time': 'd_1'}},
	{'M_2': {'connect': {'M_3': {'tr-time': 't_{2,3}', 'buffers': '-'}}, 'op-time': 'd_2'}},
	{'M_3': {'connect': {'y': {'tr-time': 't_{3,4}', 'buffers': '-'}}, 'op-time': 'd_3'}}]

PRE_A01 = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
PRE_A02 = [['-', '-', '-'], ['-', '-', '-'], [['d_1', 't_{1,3}'], ['d_2', 't_{2,3}'], '-']]
# end.
