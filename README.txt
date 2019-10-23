repo:
	prj/soft/phoebe
	sw_phoebe.git
	git@github.com:stanczyk/phoebe.git
version:
	v1.0

Copyright (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
=================================
The max-plus algebraic state space model generator

=================================
	projekt prowadzony w pythonie
		- https://docs.python-guide.org/
		- dokumentacja - sphinx with Read the Docs theme
			https://github.com/readthedocs/sphinx_rtd_theme

=================================
DO ZROBIENIA (plan):
	- DONE: testy jednostkowe (skończyć do konca w41 2019)
	- jeśli już będzie działać, tzn. będzie pełna funkcjonalność z v0.9
		- przygotować kilka wygenerowanych wyników, dla systemów opisanych już w moich publikacjach
		- sprawdzić je w matlabie
		- zapisać w testach
		- RELEASE versji 1.0
	- pomysły dla v1.1:
		- bufor pomiędzy wejściem a pierwszą maszyną
		- bufory wejściowe i wyjściowe (zamiast tylko wyjściowych -- ale to jeszcze sprawdzić)
		- przygotować opis systemu wraz z macierzą D i sprawdzić wygenerowany wynik -> zapisać do testów

WYKRYTE BŁĘDY I BRAKI
- 2019.10.14:
	DONE
	- specs/desc02_c.yml
	- nie działa generowanie modelu dla matlaba, jeśli warości podawane są bezpośrednio, a nie poprzez sekcję values
- 2019.10.14:
	DONE
	- brak modelowania buforów o skończonej pojemności
	- specs/desc04_2.yml
	- poprawić tests/answers/latex/desc04_2.tex i tests/answers/matlab/desc04_2.m
- 2019.10.17:
	- buffers - oznacza bufory wyjściowe
		na razie nie modeluję buforów pomiędzy wejściem a pierwszą maszyną, to chyba doda mi macierz B1?
	- (a powinno być, buf_in, buf_out) <-- pomysł do dorobienia
	- jak zachowuje się system z buf. wyjściowym, czasem transportu i buforem wejściowym?
- 2019.10.14:
	modelowanie przykładu z pracy 06/07 - rys.3 dla poszczególnych wariantów i konfiguracji (patrz tab.6)
	i dalej od 9?

=================================
zrobione przykłady:
	01:
		desc01_1  - ok - a simple production system (fig1 and fig2) described in 01/Ex.1.1
		desc01_2  - ok - modification of desc01_1 described in 01/Ex.1.2
		desc01_3  - ok - a multi production system (fig5 and fig6) described in 01/Ex.2.1
	02:
		desc02_a  - ko - a simple serial production line (figF23) described in 02/Ex.1.1 - without time values
		desc02_b  - ok - desc02_a with time values
		desc02_c  - ok - desc02_b with time values directly in system description
	03:
		desc03    - ok - a merging/assembly line (figF32) described in 03/Ex.1.1
	04:
		desc04_1  - ok - a simple production line without buffers (figF23) described in 04/Ex.1.1
		desc04_2  - ok - desc04_1 with finite buffers capacity 04/Ex.1.2 - the calculations do not take into account A2 and A3
		desc04_2b - ok - desc04_2 with buffers capacity given directly in the system description
		desc04_3  - ok - desc04_1 with buffers as additional OU - 04/Ex.1.3
	05:
		desc05_11 - ok - 05/config 1, infinite buffers
		desc05_12 - ok - 05/config 1, no buffers (buf = 0)
		desc05_13 - ok - 05/config 1, buffers capacity 1 (buf = 1)
		desc05_21 - ok - 05/cfg 2, buf = inf
		desc05_22 - ok - 05/cfg 2, buf = 0
		desc05_23 - ok - 05/cfg 2, buf = 1
		desc05_31 - ok - 05/cfg 3, buf = inf
		desc05_32 - ok - 05/cfg 3, buf = 0
		desc05_33 - ok - 05/cfg 3, buf = 1
	06:
		desc06_14 - ok - 05/cfg 1, buf = 10
		desc06_24 - ok - 05/cfg 2, buf = 10
		desc06_34 - ok - 05/cfg 3, buf = 10
	07:
		desc07_41 - ok - 07 ex.4.1 - modification of desc02_b
		desc07_42 - ok - 07 ex.4.2 - the same like desc03
		desc07_43 - ok - 07 ex.4.3 - ex.4.1 with no buffers
		desc07_44 - ok - 07 ex.4.2 - ex.4.1 with finite buffers
	08:
		desc08_41 - ok - desc02_b
		desc08_42 - ok - desc01_3

=================================
v1.0
	- połączenie dwóch repozytoriów:
		ssh://APKARUXEKDS37YVBPJXF@git-codecommit.eu-central-1.amazonaws.com/v1/repos/sw_phoebe
		git@github.com:stanczyk/phoebe.git
	- nowa obsługa paramterów
		wcześniej docopt>=0.6.2
		teraz click - https://click.palletsprojects.com

2019.08.14
	przełączam się z v0.9 i zaczynam prace nad wersją 1.0
	DO ZROBIENIA:
		Makefile - jakiś dziwny jest
		dokumentacja - koniecznie
		specs - przejżeć, wrzucic do old, a tu zostawić tylko ważne

2019.08.14 DONE v0.9

2018.03.31 DONE v0.8

2018.03.15
	- dorobić (luźne pomysły):
		- dodać możliwość dołączenia własnego skryptu na koniec generowanego opisu
	- przyjęta konwencja
		- wejścia muszą nazywać się u_
		- wyjścia y_
		- a elementy opisujące wektor stanów x_

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

=================================
# eof.
