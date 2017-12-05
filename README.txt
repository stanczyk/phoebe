#
# README.txt
# (c) 2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl
#

2017.11.22 DONE
automatyczne modelowanie linii produkcyjnej bazującej na opisie json lub yaml
		a) opis
			yaml command line validator: https://github.com/adrienverge/yamllint
			- sudo apt-get install yamllint
			- sudo apt-get install yamllint
		b) automatyczne testowanie, że przygotowany opis jest OK
		c) opis "analityczny", typu A0x(k) + A1x(k-1) + ...
		d) m-plik z poszczególnymi macierzami - wysyłam na standardowe wyjście

2017.11.25 DONE
poszczególne etapy programowania (python)
		- parsowanie linii poleceń
		- uruchomienie loga - wpis jakiegoś pliku w katalogu tmp (wówczas na bieżąco można będzie go podglądać)
		- parsowanie yaml-a
			- wczytywanie pliku z opisem
			- wyświetlanie opisu

			- automatyczne przypisanie wartości zmiennym (także wygenerowanym automatycznie)
			- wyświetlenie tych zmiennych (do logów?)
		- generowanie opisu
			- wyświetlanie poszczególnych danych/zmiennych: wejścia / wyjścia / ilość maszyn / czasy operacji / czasy transportu
			- opis macierzowy
				na początek po prostu opis wszystkiego co program potrafi (zmienne / macierze / opis formalny...)
				a później może podzielę to na różne sekcje
		- sprawdzanie, czy opis jest zgodny ze schematem
			- konieczne, bo nie każdy yaml jest tym, co chciałbym wczytać
			  https://stackoverflow.com/questions/3262569/validating-a-yaml-document-in-python
		- testy akceptacyjne?

2017.11.27 DONE
	- uruchomienie testów jednostkowych
	- uruchamianie poszczególnych testów:
		z kat. ~/prj/prv/up/max/src/09/phoebe:
		py.test tests/test_inf.py

2017.11.29 DONE
	- zakładamy, że wszystkie czasy (tr- i op-) są zmiennymi typu str! (obliczenia wykonane zostana w matlabie po wygenerowaniu!)

2017.12.01 DONE
	- opis z poszczególnymi czasami operacji/transportu
	- opis dla matlaba
	- sprawdzanie, czy opis jest zgodny ze schematem?
	- kiedy w pełni funkcjonalna wersja dla serial line?

2017.12.05
	- sprawdzanie, czy opis jest zgodny ze schematem?
	- modelowanie braku buforów
	- modelowanie pętli zwrotnych (czy podawać w którym takcie mają powrócić?)
	- transport time = 0 by default (jeśli połączone)
	- połączenie z więcej niż jednym elementem

# eof.
