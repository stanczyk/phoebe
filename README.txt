=======
repo:
	phoebe
version:
	v0.6

(c) 2017, 2018 Jarek Stańczyk, e-mail: j.stanczyk@hotmail.com

=================================
moje wypociny dot. generatora opisu systemów w algebrze (max, +)


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

2017.12.05 DONE
	- v0.2
	- transport time = 0 by default (jeśli połączone)
	- sprawdzanie, czy opis jest zgodny ze schematem?

2017.12.06 DONE
	- v0.3
	- modelowanie braku buforów (i pojemności buforów za pomocą pojedynczych maszyn)

2017.12.08 DONE
	- v0.4
	- połączenie z więcej niż jednym elementem

2017.12.09
	- v0.5
	- modelowanie pętli zwrotnych (w następnym takcie)

2017.12.09
	- modelowanie pojemności buforów
	- modelowanie pętli zwrotnych (z podaniem taktu, w którym mają powrócić)

2017.12.19
	splitting a subfolder out into a new repository
	- https://help.github.com/articles/splitting-a-subfolder-out-into-a-new-repository/

# eof.