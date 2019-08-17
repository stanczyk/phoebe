#
# Makefile
# Copyright (c) 2013-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
#
include tools/make/make1b.mk

# static code analysis
CHECK_CFG = setup.cfg
CHECK_DIR = setup.py bin/
	# phoebe/ tests/ setup.py

# housekeeping
CLEAN = doc-clean
CLEAN-ALL = venv-clean

.PHONY: all
all: info
	$(begin)
	@echo "use:"
	@echo "  documentation:"
	@echo "      doc doc-build doc-clean doc-serve"
	@echo "  housekeeping:"
	@echo "      clean doc-clean venv-clean clean-all"
	@echo
	@echo "development:"
	@echo "  virtualenv:"
	@echo "      venv-init venv-check venv-clean"
	@echo "  static code analysis:"
	@echo "      check-flake8 check-pylama check-pylint"
	@# echo "  unit tests:"
	@# echo "      unittests"
	@# echo "      py.test tests/test_file.py"
	@echo
	@echo "other:"
	@echo "  virtualenv:"
	@echo -e "      $(white)source .venv/bin/activate$(reset)  deactivate"
	$(end)

# plik główny:
# MAIN=tmp
# STY=$(shell pwd)/../../sty
# DESC=./specs/desc1_2.yml
# main = $(MAIN).tex
# pdf: $(MAIN) clean
# pdf-all: $(MAIN) clean

# .PHONY: $(MAIN)
# $(MAIN): $(main)
# 	@echo "$(yellow)make $@ $(main)$(reset)"
# 	$(begin)
# 	$(MAKE) -f ./../tex/make.mk pdf SRC:=$@
# 	$(end)

# .PHONY: pdf-one
# pdf-one: $(main)
# 	@echo "$(yellow)make $@ $(main)$(reset)"
# 	$(begin)
# 	$(MAKE) pdf-once SRC:=$(MAIN)
# 	$(end)

# .PHONY: build_latex
# build_latex:
# 	$(begin)
# 	./phoebe/bin/phoebe --latex $(DESC) | tee tmp.tex
# 	$(MAKE) pdf-one
# 	$(end)

# .PHONY: matlab
# matlab:
# 	$(begin)
# 	./phoebe/bin/phoebe $(DESC) | tee tmp.m
# 	$(end)

include tools/make/make_clean.mk
include tools/make/make_py.mk
include tools/make/make2b.mk
# eof
