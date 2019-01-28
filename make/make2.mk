#
# make2.mk
# Copyright (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
# 2017.08.06
#
# fragment of Makefile link after target "all"
#

# REPD - REPo Directory
REPD:=
ifeq ($(USER), vagrant)
REPD:=/home/vagrant/prj/repo
endif

.PHONY: log
log:
	$(begin)
		git log --graph --date=format:'%y-%m-%d %H:%M:%S' --pretty=format:"%C(Yellow)%H%C(reset) %ad %C(green)%an%C(reset) %s"
	$(end)

.PHONY: status
status:
	$(begin)
	@git status -s
	@git submodule foreach -q --recursive \
		'path="$${toplevel#${DIR}}" ; \
		 echo ".$${path}/$(greenw)$$name$(reset)" ; \
		 git status -s'
	$(end)

w1=File
w2=Finished Make data base
ifeq ($(LANGUAGE), pl)
w1=Plik
w2=Zakończono tworzenie bazy danych
endif
ifeq ($(LANGUAGE), pl:en)
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

.PHONY: push
push:
	$(begin)
	@echo "BRANCH=$(BRANCH)"
	-@git push --dry-run 2>&1 >/dev/null | grep $(BRANCH) >> /dev/null \
		&& \
			( git push ; \
			  echo "$$(date "+%y-%m-%d %H:%M") pushed $$(basename `git rev-parse --show-toplevel`)" >> $(REPD)/.lastpush.txt ; \
			  tail -1 $(REPD)/.lastpush.txt ) \
		|| \
			echo "nothing to push"
	$(end)

# eof.
