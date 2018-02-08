=======
repo:
	phoebe
version:
	v0.8

Copyright (c) 2017-2018 Jarosław Stańczyk <j.stanczyk@hotmail.com>

=================================
moje wypociny dot. generatora opisu systemów w algebrze (max, +)

	splitting a subfolder out into a new repository
	- https://help.github.com/articles/splitting-a-subfolder-out-into-a-new-repository/

2018.02.08 DONE v0.7
2018.01.06 DONE v0.6

2017.12.28
	- użycie liczbowych czasów operacji i transportu (jak w desc2_3.yml)

2017.12.09
	- modelowanie pojemności buforów
	- modelowanie pętli zwrotnych (z podaniem taktu, w którym mają powrócić)

2017.12.09 DONE v0.5
	- modelowanie pętli zwrotnych (w następnym takcie)

2017.12.08 DONE v0.4
	- połączenie z więcej niż jednym elementem

2017.12.06 DONE v0.3
	- modelowanie braku buforów (i pojemności buforów za pomocą pojedynczych maszyn)

2017.12.05 DONE v0.2
	- transport time = 0 by default (jeśli połączone)

2017.11.29 DONE
	- zakładamy, że wszystkie czasy (tr- i op-) są zmiennymi typu str! (obliczenia wykonane zostana w matlabie po wygenerowaniu!)

2017.11.27 DONE
	- uruchamianie poszczególnych testów z kat.~/prj/prv/up/max/src/09/phoebe:
		py.test tests/test_inf.py

2017.11.22 DONE
	- automatyczne modelowanie linii produkcyjnej bazującej na opisie yaml
		sudo apt-get install yamllint
		yamllint opis.yaml

# eof.