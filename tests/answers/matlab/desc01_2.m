%
% desc01_2.m
% (max, +) system description
% automatically generated by phoebe ver.1.0 on 2019-10-13 16:46:20 
% Copyright (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
%

clear
disp('x(k+1) = A0x(k+1) + A1x(k) + B0u(k)');
disp('y(k) = Cx(k)');

disp('u(k) = [ u_1(k); u_2(k); ]');
disp('x(k) = [ x_1(k); x_2(k); x_3(k); ]');
disp('y(k) = [ y_1(k); ]');

disp('initial vectors:');
U  = mp_ones(2, 1)
X0 = mp_zeros(3, 1)

disp('times:');
d1 = 5
d2 = 6
d3 = 3
t01 = 2
t02 = 0
t13 = 1
t23 = 0
t34 = 0

disp('matrices:');
% matrix A0
A0 = mp_zeros(3, 3);
   A0(3, 1) = mp_multi(d1, t13);
   A0(3, 2) = mp_multi(d2, t23);
   A0

% matrix A1
A1 = mp_zeros(3, 3);
   A1(1, 1) = d1;
   A1(1, 3) = mp_multi(mp_multi(t01, d3), t34);
   A1(2, 2) = d2;
   A1(2, 3) = mp_multi(mp_multi(t02, d3), t34);
   A1(3, 3) = d3;
   A1

% matrix B0
B0 = mp_zeros(3, 2);
   B0(1, 1) = t01;
   B0(2, 2) = t02;
   B0

% matrix C
C = mp_zeros(1, 3);
   C(1, 3) = mp_multi(d3, t34);
   C

disp('finally:');
As = mp_star(A0)
A = mp_multi(As, A1)
B = mp_multi(As, B0)

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
