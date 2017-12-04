# -*- coding: utf-8 -*-

ERR_ANS = '\
0: NOOP\n\
1: ERR_NO_INPUT_FILE\n\
2: ERR_NO_FILE\n\
3: ERR_NO_PERMISSION\n\
4: ERR_IO\n\
5: ERR_YAML\n\
6: ERR_NO_DATA\n\
7: ERR_NO_INPUT\n\
8: ERR_NO_OUTPUT\n\
9: ERR_NO_STATE_VECT\n'

INF_ANS = '\
Inf.VER:\n\
phoebe  v.0.1\n\
\n\
Inf.DOC:\n\
Usage:\tphoebe [--file] [--details1] [--details2] [--details3] [--vectors] [--latex | --no-desc] <desc_file>\n\
\tphoebe -h | --help\n\
\tphoebe -v | --version\n\
\n\
Options:\n\
\t--file\t\tshow information from desc_file\n\
\t--details1\tshow parsed information (1) from desc_file\n\
\t--details2\tshow parsed information (2) from desc_file\n\
\t--details3\tshow mapping and parsed matrices\n\
\t--vectors\tshow vectors: u(k), x(k) and y(k)\n\
\t--latex\t\tgenerate description for latex, default is matlab description\n\
\t--no-desc\tno description generated\n\
\t-h, --help\tshows this help message and exit\n\
\t-v, --version\tshow version information and exit\n'

INF_VER = '\
phoebe  v.0.1\n\
author: Jaroslaw Stanczyk\n\
e-mail: jaroslaw.stanczyk@upwr.edu.pl\n\
copyright: (c) 2017 Jaroslaw Stanczyk'

YML_ANS = '\
input:\n\
- u_1: {connect: M_1, op-time: t_u_1, tr-time: \'t_{0,1}\'}\n\
output:\n\
- y_1: {}\n\
prod-unit:\n\
- M_1: {connect: M_2, op-time: d_1, tr-time: \'t_{1,2}\'}\n\
- M_2: {connect: M_3, op-time: d_2, tr-time: \'t_{2,3}\'}\n\
- M_3: {connect: y_1, op-time: d_3, tr-time: \'t_{3,4}\'}\n\
values: {d_1: 3, d_2: 2, d_3: 6, \'t_{0,1}\': 1, \'t_{1,2}\': 2, \'t_{2,3}\': 0, \'t_{3,4}\': 1}\n\
\n'

ANS_FILE = '\
== INPUT FILE ==============\n\
output:\n\
- y_1: {}\n\
\n'

ANS_DET1_2 = '\
== DETAILS 1 ===============\n\
input: None\n\
prod-unit: None\n\
output: [{\'y_1\': {}}]\n\
values: None\n'

ANS_DET = '\
== DETAILS 1 ===============\n\
input: [{\'u\': {\'tr-time\': \'t_{0,1}\', \'connect\': \'M_1\'}}]\n\
prod-unit: [\
{\'M_1\': {\'op-time\': \'d_1\', \'tr-time\': \'t_{1,2}\', \'connect\': \'M_2\'}}, \
{\'M_2\': {\'op-time\': \'d_2\', \'tr-time\': \'t_{2,3}\', \'connect\': \'M_3\'}}, \
{\'M_3\': {\'op-time\': \'d_3\', \'tr-time\': \'t_{3,4}\', \'connect\': \'y\'}}]\n\
output: [{\'y\': {}}]\n\
values: %(values)s\n'

ANS_VALU_5 = '\
{\'t_{1,2}\': 2, \'t_{2,3}\': 0, \'d_2\': 2, \'d_3\': 6, \'d_1\': 3, \'t_{0,1}\': 1, \'t_{3,4}\': 1}'

ANS_DET1_4 = ANS_DET % {'values': None}
ANS_DET1_5 = ANS_DET % {'values': ANS_VALU_5}

ANS_DET2_2 = '\
== DETAILS 2 ===============\n\
input:\n\
prod-unit:\n\
output:\n\
  y_1\n\
    op-time: --\n\
    connect: --\n\
    tr-time: --\n'

ANS_DET2 = '\
== DETAILS 2 ===============\n\
input:\n\
  u\n\
    op-time: --\n\
    connect: M_1\n\
    tr-time: t_{0,1}\n\
prod-unit:\n\
  M_1\n\
    op-time: d_1\n\
    connect: M_2\n\
    tr-time: t_{1,2}\n\
  M_2\n\
    op-time: d_2\n\
    connect: M_3\n\
    tr-time: t_{2,3}\n\
  M_3\n\
    op-time: d_3\n\
    connect: y\n\
    tr-time: t_{3,4}\n\
output:\n\
  y\n\
    op-time: --\n\
    connect: --\n\
    tr-time: --\n\
%(values)s'

ANS_DET2_4 = ANS_DET2 % {'values': ''}

ANS_DET2_5 = ANS_DET2 % {'values': '\
values:\n\
  d_1: 3\n\
  d_2: 2\n\
  d_3: 6\n\
  t_{0,1}: 1\n\
  t_{1,2}: 2\n\
  t_{2,3}: 0\n\
  t_{3,4}: 1\n'}

ANS_VEC2 = '\
== VECTORS =================\n\
u(k) = [ ]\n\
x(k) = [ ]\n\
y(k) = [ y_1(k) ]\n'

ANS_VEC4 = '\
== VECTORS =================\n\
u(k) = [ u(k) ]\n\
x(k) = [ x_1(k) x_2(k) x_3(k) ]\'\n\
y(k) = [ y(k) ]\n'

ANS_DET3_2 = '\
== DETAILS 3 ===============\n\
mapping:\n\
{\'y_1\': 0}\n\
None\n\
== MATRICES ================\n\
A0 = A1 = B0 = []\n\
A0 = A1 = B0 = []\n\
A0 = A1 = B0 = []\n\
C  = [[]]\n'

ANS_DET3 = '\
== DETAILS 3 ===============\n\
mapping:\n\
{\'M_3\': 2, \'M_2\': 1, \'M_1\': 0, \'u\': 0, \'y\': 0}\n\
%(values)s\n\
== MATRICES ================\n\
A0 = [[\'-\', \'-\', \'-\'], [[\'d_1\', \'t_{1,2}\'], \'-\', \'-\'], [\'-\', [\'d_2\', \'t_{2,3}\'], \'-\']]\n\
A1 = [[[\'d_1\'], \'-\', \'-\'], [\'-\', [\'d_2\'], \'-\'], [\'-\', \'-\', [\'d_3\']]]\n\
B0 = [[[\'t_{0,1}\']], [\'-\'], [\'-\']]\n\
C  = [[\'-\', \'-\', [\'d_3\', \'t_{3,4}\']]]\n'

ANS_DET3_4 = ANS_DET3 % {'values': None}
ANS_DET3_5 = ANS_DET3 % {'values': ANS_VALU_5}

# end.
