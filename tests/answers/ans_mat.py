# -*- coding: utf-8 -*-
"""
	**answers.ans_mat.py**

	Copyright (c) 2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
"""

MAT_HEADER = '\
%\n\
% nazwa-pliku.m\n\
% (max, +) system description\n\
% automatically generated by phoebe ver.1.0 on 2019-09-06 15:48:05 \n\
% Copyright (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>\n\
%\n'

MAT_PREFACE = '\
\n\
clear\n'

MAT_END = '\
\n\
% eof\n\
\n'

MAT_EQ1 = '\
disp(\'x(k+1) = \');\n\
disp(\'y(k) = \');\n'

MAT_EQ2 = '\
disp(\'x(k+1) = A0x(k+1) + B0u(k)\');\n\
disp(\'y(k) = Cx(k) + Du(k)\');\n'

MAT_EQ3 = '\
disp(\'x(k+1) = A0x(k+1) + A1x(k) + A4x(k-3) + B0u(k)\');\n\
disp(\'y(k) = Cx(k) + Du(k)\');\n'

MAT_VEC3 = '\n\
disp(\'u(k) = [ ]\');\n\
disp(\'x(k) = [ ]\');\n\
disp(\'y(k) = [ ]\');\n'

MAT_VEC4 = '\n\
disp(\'u(k) = [ u1(k); ]\');\n\
disp(\'x(k) = [ x1(k); x2(k); ]\');\n\
disp(\'y(k) = [ y1(k); y2(k); y3(k); ]\');\n'

MAT_INI1 = '\n\
disp(\'initial vectors:\');\n\
\n\
disp(\'times:\');\n'

MAT_INI2 = '\n\
disp(\'initial vectors:\');\n\
U  = mp_ones(1, 1)\n\
X0 = mp_zeros(1, 1)\n\
\n\
disp(\'times:\');\n\
t01 = 0\n'

MAT_ADDS = '\
disp(\'finally:\');\n\
As = mp_star(A0)\n\
A = mp_multi(As, A1)\n\
B = mp_multi(As, B0)\n\
\n\
disp(\'state vector and output:\');\n\
% k - number of iterations\n\
k = 12;\n\
\n\
X(:, 1) = mp_add(mp_multi(A, X0), mp_multi(B, U));\n\
Y(:, 1) = mp_multi(C, X(:, 1));\n\
for i = 2:k\n\
    X(:, i) = mp_add(mp_multi(A, X(:, i - 1)), mp_multi(B, U));\n\
    Y(:, i) = mp_multi(C, X(:, i));\n\
end\n\
X\n\
Y\n'

MAT_MAT1 = '\
% matrix A\n\
A = mp_zeros(1, 1);\n\
   A(1, 1) = a;\n\
   A\n\
\n'

MAT_MAT2 = '\
% matrix A\n\
A = mp_zeros(3, 3);\n\
   A(1, 3) = d3;\n\
   A(2, 1) = mp_multi(d1, d12);\n\
   A(3, 2) = mp_multi(d2, d22);\n\
   A\n\
\n'

MAT_MAT3 = '\
% matrix A3\n\
A3 = mp_zeros(2, 3);\n\
   A3(2, 1) = d1;\n\
   A3(2, 2) = mp_multi(mp_multi(d21, d22), d23);\n\
   A3\n\
\n'

# end.
