%
% desc01_3.m
% (max, +) system description
% automatically generated by phoebe ver.1.0 on 2019-10-13 16:46:20 
% Copyright (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
%

clear
disp('x(k+1) = A0x(k+1) + A1x(k) + B1u(k)');
disp('y(k) = Cx(k) + Cx(k0) + Cx(k-2) + Cx(k-5) + Cx(k-9) + Cx(k-14)');

disp('u(k) = [ u_1(k); u_2(k); u_3(k); u_4(k); u_5(k); u_6(k); ]');
disp('x(k) = [ x_1(k); x_2(k); x_3(k); x_4(k); x_5(k); x_6(k); x_7(k); ]');
disp('y(k) = [ y_1(k); y_2(k); y_3(k); y_4(k); y_5(k); y_6(k); ]');

disp('initial vectors:');
U  = mp_ones(6, 1)
X0 = mp_zeros(7, 1)

disp('times:');
d1 = 1
d2 = 5
d3 = 3
d4 = 2
d5 = 3
d6 = 4
d7 = 3

disp('matrices:');
% matrix A0
A0 = mp_zeros(7, 7);
   A0(2, 1) = d1;
   A0(4, 1) = d1;
   A0(4, 3) = d3;
   A0(5, 2) = d2;
   A0(5, 4) = d4;
   A0(6, 3) = d3;
   A0(7, 4) = d4;
   A0(7, 6) = d6;
   A0

% matrix A1
A1 = mp_zeros(7, 7);
   A1(1, 1) = d1;
   A1(1, 2) = d2;
   A1(1, 7) = d7;
   A1(2, 2) = d2;
   A1(2, 5) = d5;
   A1(3, 3) = d3;
   A1(3, 5) = d5;
   A1(3, 6) = d6;
   A1(4, 4) = d4;
   A1(5, 5) = d5;
   A1(6, 6) = d6;
   A1(6, 7) = d7;
   A1(7, 7) = d7;
   A1

% matrix B1
B1 = mp_zeros(7, 6);
   B1(1, 1) = 0;
   B1(1, 5) = 0;
   B1(2, 6) = 0;
   B1(3, 2) = 0;
   B1(3, 4) = 0;
   B1(6, 3) = 0;
   B1

% matrix C
C = mp_zeros(6, 7);
   C(1, 2) = d2;
   C(2, 5) = d5;
   C(3, 7) = d7;
   C(4, 6) = d6;
   C(5, 7) = d7;
   C(6, 5) = d5;
   C

disp('finally:');
As = mp_star(A0)
A = mp_multi(As, A1)
B = mp_multi(As, B1)

disp('state vector and output:');
% k - number of iterations
k = 12;

X(:, 1) = mp_add(mp_multi(A, X0), mp_multi(B, U));
Y(:, 1) = mp_multi(C, X(:, 1));
for i = 2:k
    X(:, i) = mp_add(mp_multi(A, X(:, i - 1)), mp_multi(B, U));
    Y(:, i) = mp_multi(C, X(:, i));
end
X
Y

% eof

