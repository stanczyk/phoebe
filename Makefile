#
# Makefile
# Copyright (c) 2013-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
#
include tools/make/make1b.mk

.PHONY: all
all: info
	$(begin)
	@echo "development:"
	@echo "  documentation:"
	@echo "      doc-build doc-clean doc-serve"
	@echo "  virtualenv:"
	@echo "      venv-init venv-check venv-clean"
	@echo "  static code analysis:"
	@echo "      check-flake8 check-pylama check-pylint"
	@echo "  unit tests:"
	@echo "      unittests"
	@echo "      py.test tests/test_file.py"
	@echo "  clean-up:"
	@echo "      clean doc-clean venv-clean clean-all"
	@echo
	@echo "other:"
	@echo "  virtualenv:  source .venv/bin/activate  deactivate"
	$(end)

# .PHONY: clean
# clean: doc-clean
#
# .PHONY: doc
# doc:
# 	$(begin)
# 	cd docs; \
# 		$(MAKE) html
# 	$(end)

# .PHONY: doc-clean
# doc-clean:
# 	$(begin)
# 	@if [ -d docs/build ]; then \
# 		echo "$(RM) -r docs/build"; \
# 		$(RM) -r docs/build; \
# 	fi
# 	$(end)

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

include tools/make/make_py.mk
include tools/make/make2b.mk
# eof
