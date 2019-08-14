#
# make.mk
# Copyright (c) 2003-2005, 2015-2018 Jarosław Stańczyk <jaroslaw.stanczyk@upwr.edu.pl>
#

# SRC=max-plus
BRANCH:=$(shell git rev-parse --abbrev-ref HEAD)
USER:=$(shell whoami)
STY=$(shell pwd)/../sty

FIGF=$(patsubst figF%.tex, figF%.pdf, $(wildcard figF*.tex))
FIGG=$(patsubst figG%.tex, figG%.pdf, $(wildcard figG*.tex))
FIGP=$(patsubst figP%.tex, figP%.pdf, $(wildcard figP*.tex))

ifdef SRC
    FROM_SRC:=$(MAKE) pdf-src
else
    FROM_SRC:=@echo "nic nie trzeba kompilować"
endif

.PHONY: all
all:
	$(begin)
	@echo "USER=$(USER), BRANCH=$(BRANCH), SRC=$(SRC), MAIN=$(MAIN)"
	@echo
	@echo what do you want to do?
	@echo "   make pdf   --- compile latex sources into pdf"
	@echo "   make clean --- remove all temporary files"
	@echo
	@echo "$(white)all targets$(reset) (more details inside Makefile):"
	@echo -n "$(yellow)"
	@$(MAKE) --no-print-directory list
	@echo "$(reset)"
	$(end)

figF%.pdf: figF%.tex
	@echo "$(yellow)make $@ $(reset)"
	$(begin)
	$(MAKE) figgas SRC=$(shell basename $@ .pdf)
	$(end)

figG%.pdf: figG%.tex
	@echo "$(yellow)make $@ $(reset)"
	$(begin)
	pdflatex --shell-escape $(shell basename $@ .pdf)
	$(end)

figP%.pdf: figP%.tex
	@echo "$(yellow)make $@ $(reset)"
	$(begin)
	$(MAKE) pdf-once SRC=$(shell basename $@ .pdf)
	$(end)

.PHONY: pdf
pdf:
	@echo "$(yellow)make $@ $(reset)"
	$(begin)
	$(FROM_SRC)
	$(end)

.PHONY: pdf-src
pdf-src:
	@echo "$(yellow)make $@ $(SRC)$(reset)"
	$(begin)
	$(MAKE) biber
	$(MAKE) pdf-once
	$(end)

.PHONY: pdf-once
pdf-once:
	@echo "$(yellow)make $@ $(SRC)$(reset)"
	$(begin)
	export TEXINPUTS=".:$(STY):" ; pdflatex $(SRC)
	$(end)

.PHONY: biber
biber: pdf-once
	@echo "$(yellow)make $@ $(SRC)$(reset)"
	$(begin)
	biber $(SRC)
	$(end)

.PHONY: clean
clean: clean-tex clean-m-src
	$(begin)
	$(RM) *.aux
	$(RM) *.bbl
	$(RM) *.bcf
	$(RM) *.blg
	$(RM) *.idx
	$(RM) *.ilg
	$(RM) *.ind
	$(RM) *.log
	$(RM) *.out
	$(RM) *.toc
	$(RM) *.xml
	$(end)

.PHONY: clean-m-src
clean-m-src:
	$(begin)
	$(RM) m-src/mp_tab.tex
	$(RM) m-src/mp_gantt.tex
	$(end)

.PHONY: clean-tex
clean-tex:
	$(begin)
	$(RM) *-md5.txt
	$(RM) *.dvi
	$(RM) *.ps
	$(end)

.PHONY: clean-all
clean-all: clean
	$(begin)
	$(RM) *.pdf
	$(RM) ./fig/*-eps-converted-to.pdf
	$(end)

.PHONY: figgas
figgas:
	@echo "$(yellow)make $@ $(SRC)$(reset)"
	$(begin)
	$(MAKE) pdf-once
	export DVIPSHEADERS=".:$(STY):" ; dvipdf $(SRC)
	$(end)

.PHONY: octave
octave:
	@octave --traditional

.PHONY: ifac
ifac: $(main)
	$(begin)
	pdflatex $(MAIN)
	bibtex $(MAIN)
	pdflatex $(MAIN)
	pdflatex $(MAIN)
	$(end)

.PHONY: ifac-init
ifac-init:
	$(begin)
	ln -s ../../sty/ifacconf.cls .
	ln -s ../../sty/ifacconf.bst .
	ln -s ../../sty/ifacconf-harvard.bst .
	$(end)

.PHONY: ifac-deinit
ifac-deinit:
	$(begin)
	$(RM) ifacconf.cls
	$(RM) *.bst
	$(end)

# eof.
