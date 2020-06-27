CWD     = $(CURDIR)
MODULE  = $(shell echo $(notdir $(CWD)) | tr A-Z a-z )
OS     ?= $(shell uname -s)

NIMBLE  = $(HOME)/.nimble/bin/nimble
NIM     = $(HOME)/.nimble/bin/nim
NPRETTY = $(HOME)/.nimble/bin/nimpretty



.PHONY: all
all:



.PHONY: install update

install: $(OS)_install $(NIMBLE)
update: $(OS)_update

.PHONY: Linux_install Linux_update

Linux_install Linux_update:
	sudo apt update
	sudo apt install -u `cat apt.txt`

$(NIMBLE):
	curl https://nim-lang.org/choosenim/init.sh -sSf | sh



.PHONY: master shadow release

MERGE  = Makefile README.md .gitignore .vscode apt.txt
MERGE += src tests

master:
	git checkout $@
	git pull -v
	git checkout shadow -- $(MERGE)

shadow:
	git checkout $@
	git pull -v

release:
	git tag $(NOW)-$(REL)
	git push -v && git push -v --tags
	$(MAKE) shadow
