#
# README.txt
# (c) 2017 Jaroslaw Stanczyk, e-mail: j.stanczyk@hotmail.com
#

2017.11.22
automatyczne modelowanie linii produkcyjnej bazującej na opisie json lub yaml
	DONE:
		a) opis
			yaml command line validator: https://github.com/adrienverge/yamllint
			- sudo apt-get install yamllint
			- sudo apt-get install yamllint
		b) automatyczne testowanie, że przygotowany opis jest OK

	TO-DO:
	w pythonie napisać programik, który, na podstawie yaml-a wygeneruje:
		c) opis "analityczny", typu A0x(k) + A1x(k-1) + ...
		d) m-plik z poszczególnymi macierzami

2017.11.25
poszczególne etapy programowania (python)
	DONE:
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

	TO-DO:
		- sprawdzanie, czy opis jest zgodny ze schematem
			- konieczne, bo nie każdy yaml jest tym, co chciałbym wczytać
			  https://stackoverflow.com/questions/3262569/validating-a-yaml-document-in-python
		- testy akceptacyjne?

2017.11.27 DONE
	- uruchomienie testów jednostkowych
	- uruchamianie poszczególnych testów:
		z kat. ~/prj/prv/up/max/src/09/phoebe:
		py.test tests/test_inf.py

# eof.
