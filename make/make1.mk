#
# make1.mk
# Copyright (c) 2017-2018 Jarosław Stańczyk <jaroslaw.stanczyk@upwr.edu.pl>
# 2017.08.06
#

black=\033[0;30m
blue=\033[0;34m
brown=\033[0;33m
green=\033[0;32m
greenw=\033[92m
grey=\033[1;30m
purple=\033[0;35m
red=\033[0;31m
yellow=\033[1;33m
white=\033[1;37m
reset=\033[0m

begin=@echo "$(blue)START [$@]$(reset)"
end=@echo "$(blue)END   [$@]$(reset)"

# eof.