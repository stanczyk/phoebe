#
# Makefile for phoebe project
# (c) 2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl
#
include ./../../tex/make1.mk

BIN=bin
SRC=phoebe
TST=tests
CFG=code_audit.cfg
# BUILD=build .cache dist vcm.egg-info

.PHONY: all
all:
	$(begin)
	@echo "$(white)all targets$(reset) (more details inside Makefile):"
	@echo -n "$(yellow)"
	@$(MAKE) --no-print-directory list
	@echo "$(reset)"
	$(end)

.PHONY: clean
clean:
	$(begin)
	rm -f $(SRC)/*.pyc
	rm -f $(TST)/*.pyc
	rm -rf $(TST)/__pycache__
	# rm -rf .eggs
	# for i in $(BUILD) ; do \
	# 	rm -rf $$i ; \
	# done
	# rm -rf $(BUILD)
	$(end)

.PHONY: clean-all
clean-all: clean
	$(begin)
	rm -rf .venv
	$(end)

.PHONY: init
init:
	$(begin)
	virtualenv .venv
	(\
		. .venv/bin/activate; \
		pip install -r requirements-dev.txt \
	)
	$(end)

.PHONY: is_virtenv
is_virtenv:
	$(begin)
	@if ./bin/is_venv.py ; then \
		echo "$(red)run it in virtualenv!$(reset)"; \
		echo " -> source .venv/bin/activate"; \
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
	@for py in $(lsbin) ; \
	do \
		echo "pylint --rcfile=$(CFG) $$py" ; \
		pylint --rcfile=$(CFG) $$py ; \
	done
	pylint --rcfile=$(CFG) $(TST)
	$(end)

.PHONY: tests
tests: is_virtenv
	$(begin)
	python setup.py test
	$(end)

include ./../../tex/make2.mk
# eof.
