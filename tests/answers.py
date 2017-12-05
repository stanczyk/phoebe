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
phoebe  v.0.3\n\
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
phoebe  v.0.3\n\
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
input: [\
{\'u\': {\'op-time\': \'0\', \'tr-time\': \'t_{0,1}\', \'connect\': \'M_1\', \'buffers\': \'-\'}}]\n\
prod-unit: [\
{\'M_1\': {\'op-time\': \'d_1\', \'tr-time\': \'t_{1,2}\', \'connect\': \'M_2\', \'buffers\': \'-\'}}, \
{\'M_2\': {\'op-time\': \'d_2\', \'tr-time\': \'t_{2,3}\', \'connect\': \'M_3\', \'buffers\': \'-\'}}, \
{\'M_3\': {\'op-time\': \'d_3\', \'tr-time\': \'t_{3,4}\', \'connect\': \'y\', \'buffers\': \'-\'}}]\n\
output: [\
{\'y\': {}}]\n\
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
    op-time: -\n\
    connect: -\n\
    tr-time: -\n\
    buffers: -\n'

ANS_DET2 = '\
== DETAILS 2 ===============\n\
input:\n\
  u\n\
    op-time: 0\n\
    connect: M_1\n\
    tr-time: t_{0,1}\n\
    buffers: -\n\
prod-unit:\n\
  M_1\n\
    op-time: d_1\n\
    connect: M_2\n\
    tr-time: t_{1,2}\n\
    buffers: -\n\
  M_2\n\
    op-time: d_2\n\
    connect: M_3\n\
    tr-time: t_{2,3}\n\
    buffers: -\n\
  M_3\n\
    op-time: d_3\n\
    connect: y\n\
    tr-time: t_{3,4}\n\
    buffers: -\n\
output:\n\
  y\n\
    op-time: -\n\
    connect: -\n\
    tr-time: -\n\
    buffers: -\n\
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

DESC_BEGIN = '\
%\n\
% (max, +) system description\n\
% (c) 2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl\n\
%\n\
% automatically generated by phoebe  v.0.3 on 2017-12-04 08:30:33 CET\n\
%\n'

ANS_MAT = '\
{0}\
\n\
clear\n\
disp(\'\');\n\
disp(\'x(k) = A0x(k) + A1x(k-1) + B0u(k)\');\n\
disp(\'y(k) =  Cx(k)\');\n\
disp(\'---------------------------------\');\n\
disp(\'u(k) = [ u(k); ]\');\n\
disp(\'x(k) = [ x_1(k); x_2(k); x_3(k); ]\');\n\
disp(\'y(k) = [ y(k); ]\');\n\
disp(\'---------------------------------\');\n\
disp(\'initial vectors:\');\n\
disp(\'\');\n\
\n\
U  = mp_ones(1, 1)\n\
X0 = mp_zeros(3, 1)\n\
\n\
{1}\
% matrix A0\n\
A0 = mp_zeros(3, 3);\n\
   A0(2, 1) = mp_multi(d1, t12);\n\
   A0(3, 2) = mp_multi(d2, t23);\n\
\n\
% matrix A1\n\
A1 = mp_zeros(3, 3);\n\
   A1(1, 1) = d1;\n\
   A1(2, 2) = d2;\n\
   A1(3, 3) = d3;\n\
\n\
% matrix B0\n\
B0 = mp_zeros(3, 1);\n\
   B0(1, 1) = t01;\n\
\n\
% matrix C\n\
C = mp_zeros(1, 3);\n\
   C(1, 3) = mp_multi(d3, t34);\n\
\n\
A0\n\
A1\n\
B0\n\
C\n\
\n\
As = mp_star(A0)\n\
A = mp_multi(As, A1)\n\
B = mp_multi(As, B0)\n\
\n\
% number of iterations\n\
k = 12;\n\
X(:, 1) = mp_add(mp_multi(A, X0), mp_multi(B, U));\n\
Y(1) = mp_multi(C, X(:, 1));\n\
for i = 2:k\n\
    X(:, i) = mp_add(mp_multi(A, X(:, i - 1)), mp_multi(B, U));\n\
    Y(i) = mp_multi(C, X(:, i));\n\
end\n\
X\n\
Y\n\
\n\
% eof\n\
\n'

ANS_MAT4 = ANS_MAT.format(DESC_BEGIN, '')
ANS_MAT5 = ANS_MAT.format(DESC_BEGIN, '\
d1 = 3\n\
d2 = 2\n\
d3 = 6\n\
t01 = 1\n\
t12 = 2\n\
t23 = 0\n\
t34 = 1\n\
\n')

ANS_LAT = '\
\\documentclass[11pt, a4paper, fleqn]{article}\n\
\\usepackage{amsmath}\n\
\\begin{document}\n\
\\section{(max, +) description}\n\
\n\
\\begin{align}\\begin{split}\n\
% x(k) = A0x(k) + A1x(k-1) + B0u(k)\n\
\\mathbf{x}(k) & \\, = \\; \
\\mathbf{A}_0\\mathbf{x}(k) \\oplus \\mathbf{A}_1\\mathbf{x}(k-1) \\oplus \\mathbf{B}_0\\mathbf{u}(k)\\\\\n\
% y(k) = Cx(k)\n\\mathbf{y}(k) & \\, = \\; \\mathbf{Cx}(k) \\\\\n\
\\end{split}\\end{align}\n\
\n\
% vector u(k)\n\
\\begin{equation*}\n\
\\mathbf{u}(k) = \n\
\\left[\\begin{array}{*{20}c}\n\
  u(k) \\\\\n\
\\end{array}\\right]\n\
\\end{equation*}\n\
\n\
% vector x(k)\n\
\\begin{equation*}\n\
\\mathbf{x}(k) = \n\
\\left[\\begin{array}{*{20}c}\n\
  x_1(k) \\\\\n\
  x_2(k) \\\\\n\
  x_3(k) \\\\\n\
\\end{array}\\right]\n\
\\end{equation*}\n\
\n\
% vector y(k)\n\
\\begin{equation*}\n\
\\mathbf{y}(k) = \n\
\\left[\\begin{array}{*{20}c}\n\
  y(k) \\\\\n\
\\end{array}\\right]\n\
\\end{equation*}\n\
\n\
% matrix A_0\n\
\\begin{equation*}\n\
\\mathbf{A}_0 = \n\
\\left[\\begin{array}{*{20}c}\n\
\\varepsilon \t& \\varepsilon \t& \\varepsilon \\\\\n\
d_1t_{1,2} \t& \\varepsilon \t& \\varepsilon \\\\\n\
\\varepsilon \t& d_2t_{2,3} \t& \\varepsilon \\\\\n\
\\end{array}\\right]\n\
\\end{equation*}\n\
\n\
% matrix A_1\n\
\\begin{equation*}\n\
\\mathbf{A}_1 = \n\
\\left[\\begin{array}{*{20}c}\n\
d_1 \t& \\varepsilon \t& \\varepsilon \\\\\n\
\\varepsilon \t& d_2 \t& \\varepsilon \\\\\n\
\\varepsilon \t& \\varepsilon \t& d_3 \\\\\n\
\\end{array}\\right]\n\
\\end{equation*}\n\
\n\
% matrix B_0\n\
\\begin{equation*}\n\
\\mathbf{B}_0 = \n\
\\left[\\begin{array}{*{20}c}\n\
t_{0,1} \\\\\n\
\\varepsilon \\\\\n\
\\varepsilon \\\\\n\
\\end{array}\\right]\n\
\\end{equation*}\n\
\n\
% matrix C_{}\n\
\\begin{equation*}\n\
\\mathbf{C}_{} = \n\
\\left[\\begin{array}{*{20}c}\n\
\\varepsilon \t& \\varepsilon \t& d_3t_{3,4} \\\\\n\
\\end{array}\\right]\n\
\\end{equation*}\n\
\n'

LAT_END = '\
\\end{document}\n\
% eof\n\
\n'

ANS_LAT4 = DESC_BEGIN + ANS_LAT + LAT_END
ANS_LAT5 = DESC_BEGIN + ANS_LAT + '\
\\noindent\\\\\n\
$d_1 = 3$\\\\\n\
$d_2 = 2$\\\\\n\
$d_3 = 6$\\\\\n\
$t_{0,1} = 1$\\\\\n\
$t_{1,2} = 2$\\\\\n\
$t_{2,3} = 0$\\\\\n\
$t_{3,4} = 1$\\\\\n\
\n' + LAT_END

# end.
