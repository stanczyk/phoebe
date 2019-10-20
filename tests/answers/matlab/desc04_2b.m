%
% desc04_2b.m
% (max, +) system description
% automatically generated by phoebe ver.1.0 on 2019-10-13 16:46:20 
% Copyright (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
%

clear
disp('x(k+1) = A0x(k+1) + A1x(k) + A2x(k-1) + A3x(k-4) + B0u(k)');
disp('y(k) = Cx(k)');

disp('u(k) = [ u_1(k); ]');
disp('x(k) = [ x_1(k); x_2(k); x_3(k); ]');
disp('y(k) = [ y_1(k); ]');

disp('initial vectors:');
U  = mp_ones(1, 1)
X0 = mp_zeros(3, 1)

disp('times:');
b0 = 0
b1 = 1
b2 = 2
d1 = 3
d2 = 2
d3 = 6
t01 = 1
t12 = 2
t23 = 0
t34 = 1

disp('matrices:');
% matrix A0
A0 = mp_zeros(3, 3);
   A0(2, 1) = mp_multi(d1, t12);
   A0(3, 2) = mp_multi(d2, t23);
   A0

% matrix A1
A1 = mp_zeros(3, 3);
   A1(1, 1) = d1;
   A1(2, 2) = d2;
   A1(3, 1) = -t34;
   A1(3, 3) = d3;
   A1

% matrix A2
A2 = mp_zeros(3, 3);
   A2(1, 2) = -t12;
   A2

% matrix A3
A3 = mp_zeros(3, 3);
   A3(2, 3) = -t23;
   A3

% matrix B0
B0 = mp_zeros(3, 1);
   B0(1, 1) = t01;
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

