#
# Makefile
# Copyright (c) 2013-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
#
include ./make/make1.mk

BIN=bin
SRC=phoebe
TST=tests
CFG=code_audit.cfg
BUILD=.cache .eggs phoebe.egg-info dist build .pytest_cache
LSBIN=$(shell ls $(BIN) | sed -e 's:^:./$(BIN)/:')

.PHONY: all
all:
	$(begin)
	@echo "$(white)all targets$(reset) (more details inside Makefile):"
	@echo -n "$(yellow)"
	@$(MAKE) --no-print-directory list
	@echo "$(reset)"
	@echo "other:"
	@echo "  yamllint ./specs/02.desc2.yml"
	@echo "  source .venv/bin/activate"
	@echo "  deactivate"
	@echo "  py.test tests/test_inf.py"
	$(end)

.PHONY: clean
clean:
	$(begin)
	$(RM) $(SRC)/*.pyc
	$(RM) $(TST)/*.pyc
	$(RM) -r $(TST)/__pycache__
	$(RM) -r $(BUILD)
	cd .. ; $(RM) tmp.*
	$(end)

.PHONY: clean-all
clean-all: clean
	$(begin)
	$(RM) -r .venv
	$(end)

.PHONY: init_virtualenv
init_virtualenv:
	$(begin)
	virtualenv .venv
	(\
		. .venv/bin/activate; \
		pip install -r requirements-dev.txt \
	)
	@echo "run: $(white)source .venv/bin/activate$(reset)"
	@echo "at the end: $(white)deactivate$(reset)"
	$(end)

.PHONY: is_virtenv
is_virtenv:
	$(begin)
	@if ./bin/is_venv.py ; then \
		echo "$(red)run it in virtualenv!$(reset)"; \
		echo " -> source .venv/bin/activate"; \
		echo " or"; \
		echo " -> virtualenv .venv and install all requirements"; \
		# echo " -> deactivate"; \
		exit 1; \
	fi
	$(end)

.PHONY: flake8
flake8: is_virtenv
	$(begin)
	flake8 --config=$(CFG) $(BIN) \
		$(SRC) \
		setup.py \
		$(TST)
	$(end)

.PHONY: pylama
pylama: is_virtenv
	$(begin)
	pylama -o $(CFG) $(BIN) \
		$(SRC) \
		setup.py \
		$(TST)
	$(end)

.PHONY: pylint
pylint: is_virtenv
	$(begin)
	pylint --rcfile=$(CFG) setup.py
	@echo $(LSBIN)
	@for py in $(LSBIN) ; \
		do \
			echo "pylint --rcfile=$(CFG) $$py" ; \
			pylint --rcfile=$(CFG) $$py ; \
		done
	pylint --rcfile=$(CFG) $(TST)
	$(end)

.PHONY: src-test
src-test: flake8 pylama pylint

.PHONY: unit-tests
unit-test: is_virtenv
	$(begin)
	python setup.py test
	$(end)

.PHONY: test
test: src-test unit-test

.PHONY: build_latex
build_latex:
	$(begin)
	./bin/phoebe --latex "$(FILE).yml" | tee "$(FILE).tex"
	$(end)

.PHONY: build_matlab
build_matlab:
	$(begin)
	./bin/phoebe "$(FILE).yml" | tee "$(FILE).m"
	$(end)

.PHONY: phoebe
phoebe: is_virtenv build_latex build_matlab

include ./make/make2.mk

# eof
