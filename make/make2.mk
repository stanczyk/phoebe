#
# make2.mk
# (c) 2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl
# 2017.08.06
#
# part of Makefile link after target "all"
#

.PHONY: log
log:
	$(begin)
		git log --graph --date=format:'%y-%m-%d %H:%M:%S' --pretty=format:"%C(Yellow)%H%C(reset) %ad %C(green)%an%C(reset) %s"
	$(end)

.PHONY: status
status:
	@# check the git status of repository and all submodules
	$(begin)
	@echo "$(greenw)[.]$(reset)"
	@git status -s
	@git submodule foreach -q --recursive \
		'echo "$(greenw)[$$name]$(reset)" ; \
		git status -s'
	$(end)

w1=File
w2=Finished Make data base
ifeq ($(LANGUAGE), pl)
w1=Plik
w2=Zakończono tworzenie bazy danych
endif

.PHONY: list
list:
	@# $(MAKE) -pRrq -f Makefile
	@# $(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST))
	@$(MAKE) -pRrq -f Makefile : 2>/dev/null | \
		awk -v RS= -F: '/^# $(w1)/,/^# $(w2)/ {if ($$1 !~ "^[#.]") {print $$1}}' | \
		sort | \
		egrep -v -e '^[^[:alnum:]]' -e '^$@$$' | \
		xargs

# eof.