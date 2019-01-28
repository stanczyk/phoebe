#
# Makefile
# Copyright (c) 2013-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
#
include ./phoebe/make/make.mk
include ./phoebe/make/make1.mk

# plik główny:
MAIN=tmp
STY=$(shell pwd)/../../sty
DESC=./specs/desc1_2.yml

main = $(MAIN).tex

pdf: $(MAIN) clean

pdf-all: $(MAIN) clean

.PHONY: $(MAIN)
$(MAIN): $(main)
	@echo "$(yellow)make $@ $(main)$(reset)"
	$(begin)
	$(MAKE) -f ./../tex/make.mk pdf SRC:=$@
	$(end)

.PHONY: pdf-one
pdf-one: $(main)
	@echo "$(yellow)make $@ $(main)$(reset)"
	$(begin)
	$(MAKE) pdf-once SRC:=$(MAIN)
	$(end)

.PHONY: build_latex
build_latex:
	$(begin)
	./phoebe/bin/phoebe --latex $(DESC) | tee tmp.tex
	$(MAKE) pdf-one
	$(end)

.PHONY: matlab
matlab:
	$(begin)
	./phoebe/bin/phoebe $(DESC) | tee tmp.m
	$(end)

include ./phoebe/make/make2.mk

# eof
