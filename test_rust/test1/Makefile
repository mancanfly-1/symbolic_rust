RUSTC	= /home/mancanfly/.cargo/bin/rustc
O		= o.rust

TEST_SRCS = $(wildcard src/*.rs)
TEST_SRCS := src/a.rs
TEST_LL = $(wildcard o.rust/*.ll)

TEST_LL := $(O)/a.ll

TEST_PY = $(O)/a.py

$(O)/%.ll: src/%.rs
	mkdir -p $(O)
ifneq ("$^", "main.rs")
	@echo "-------------"
	rustc --crate-type staticlib --emit=llvm-ir "$^" -o "$@" -g
endif

$(O)/%.py: $(O)/%.ll
	src/irpy "$<" > "$@"


test:$(TEST_PY)
	cp test.py $(O)
	cd $(O) && python2 test.py

clean:
	rm -r o.rust



