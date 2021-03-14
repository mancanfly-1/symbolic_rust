-include config.mk

PROJECT      ?= hv6
ARCH         ?= x86_64
O            ?= o.$(ARCH)
NR_CPUS      ?= 1
QEMU_ACCEL   ?= kvm:tcg
QEMU_CPU     ?= max
QEMU_DISPLAY ?= none
# some Ubuntu doesn't have e1000e
QEMU_NIC     ?= e1000
BOCHS_CPU    ?= broadwell_ult
IOMMU        ?= intel-iommu
USE_LL       ?= 0

SRCARCH      := $(ARCH)
ifeq ($(ARCH),x86_64)
SRCARCH      := x86
endif

V             = @
Q             = $(V:1=)
QUIET_CC      = $(Q:@=@echo    '     CC       '$@;)
QUIET_CC_IR   = $(Q:@=@echo    '     CC_IR    '$@;)
QUIET_IRPY    = $(Q:@=@echo    '     IRPY     '$@;)
QUIET_PY2     = $(Q:@=@echo    '     PY2      '$@;)
QUIET_CC_USER = $(Q:@=@echo    '     CC.user  '$@;)
QUIET_LD      = $(Q:@=@echo    '     LD       '$@;)
QUIET_LD_USER = $(Q:@=@echo    '     LD.user  '$@;)
QUIET_GEN     = $(Q:@=@echo    '     GEN      '$@;)
QUIET_CXX     = $(Q:@=@echo    '     C++      '$@;)
QUIET_AR      = $(Q:@=@echo    '     AR       '$@;)
QUIET_RANLIB  = $(Q:@=@echo    '     RANLIB   '$@;)

CFLAGS       += -fno-PIE
CFLAGS       += -ffreestanding -MD -MP
CFLAGS       += -Wall
CFLAGS       += -g
CFLAGS       += -mno-red-zone
CFLAGS       += -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx
CFLAGS       += -DCOMMIT_HASH=$(shell git rev-parse --short --verify HEAD)
CFLAGS       += -DCOMMIT_BRANCH=$(shell git rev-parse --abbrev-ref --verify HEAD)
CFLAGS       += -imacros kernel/config.h
CFLAGS       += -I include -I $(O)/include

KERNEL_CFLAGS = $(CFLAGS) -DNR_CPUS=$(NR_CPUS) -fwrapv -I $(PROJECT) -I kernel -I kernel/include

USER_CFLAGS   = $(CFLAGS)

MKDIR_P      := mkdir -p
LN_S         := ln -s
UNAME_S      := $(shell uname -s)
TOP          := $(shell echo $${PWD-`pwd`})
HOST_CC      := cc
PY2          := python2

# Try the latest version first
LLVM_CONFIG  := llvm-config-11
ifeq ($(shell which $(LLVM_CONFIG) 2> /dev/null),)
LLVM_CONFIG  := llvm-config
endif
# Homebrew hides llvm here
ifeq ($(shell which $(LLVM_CONFIG) 2> /dev/null),)
LLVM_CONFIG  := /usr/bin/llvm-config-11
endif
ifeq ($(shell which $(LLVM_CONFIG) 2> /dev/null),)
LLVM_PREFIX  :=
else
LLVM_PREFIX  := "$(shell '$(LLVM_CONFIG)' --bindir)/"
endif
LLVM_CC      += $(LLVM_PREFIX)clang -target $(ARCH)-linux-gnu -Wno-initializer-overrides
LLVM_LINK    := $(LLVM_PREFIX)llvm-link

KERNEL_LDS   := $(O)/kernel/kernel.lds

ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(ARGS):;@:)

include irpy/Makefrag

all: $(PROJECT)


clean:
	-rm -rf $(O)

format:
	find . -regextype egrep -regex '.*\.(c|h|cc|hh|cpp)$$' -not -path './user/lwip/*' -print -exec clang-format -style=file -i {} \;

.PHONY: kernel qemu qemu-gdb bochs iso tar gdb clean tags check irpy verify esp format

