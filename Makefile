#
# Makefile
# (c) 2003-2005, 20015-2017 Jaroslaw Stanczyk, e-mail: j.stanczyk@hotmail.com
#
include ./../tex/make.mk
include ./../tex/make1.mk

# plik główny:
MAIN=tmp
STY=$(shell pwd)/../../sty

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

.PHONY: build
build:
	$(begin)
	./phoebe/bin/phoebe ./phoebe/bin/02.desc2.yml | tee tmp.tex
	$(MAKE) pdf-one
	$(end)

include ./../tex/make2.mk
# eof.
