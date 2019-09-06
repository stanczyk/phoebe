# -*- coding: utf-8 -*-
"""
	**answers.ans_mat.py**

	Copyright (c) 2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
"""

MAT_BEGIN = '\
%\n\
% nazwa-pliku.m\n\
% (max, +) system description\n\
% automatically generated by phoebe ver.1.0 on 2019-09-06 15:48:05 \n\
% Copyright (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>\n\
%\n\n'

MAT_EQUEST1 = '\
clear\n\
\n\
disp(\'x(k+1) = A0x(k+1) + A1x(k) + A3x(k-2) + B1u(k)\');\n\
disp(\'y(k) = C1x(k) + D1u(k)\');\n\
disp(\'---------------------------------\');\n'

# end.