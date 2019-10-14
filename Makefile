#
# Makefile
# Copyright (c) 2013-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
#
include tools/make/make1b.mk

# static code analysis
CHECK_CFG = setup.cfg
CHECK_DIR = setup.py bin/ phoebe/ tests/

# housekeeping
CLEAN = doc-clean py-clean
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
	@echo "  unit tests:"
	@echo "      unittests"
	@echo "      py.test tests/test_file.py"
	@echo "      py.test tests/test_file.py::Class::method"
	@echo
	@echo "other:"
	@echo "  virtualenv:"
	@echo -e "      $(white)source .venv/bin/activate$(reset)  deactivate"
	$(end)

.PHONY: octave
octave:
	@octave --traditional

include tools/make/make_clean.mk
include tools/make/make_py.mk
include tools/make/make2b.mk
# eof
