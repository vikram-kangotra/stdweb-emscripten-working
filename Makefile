C_SOURCES = snippet.c
EMCC_FLAGS = -lstdweb_emscripten_working -L.
GENERATE_SCRIPT = python3 generate_emscripten_bindings.py
CLEAN_FILES = libstdweb_emscripten_working.a main.js main.wasm snippet.c

# Patch file and marker for apply_patch target
PATCH_FILE := patches/stdweb-fix-emscripten.patch
MARKER_FILE := .patch_applied

all: apply_patch main.js

main.js: libstdweb_emscripten_working.a $(C_SOURCES) main.c
	emcc $(C_SOURCES) main.c $(EMCC_FLAGS) -o main.js --post-js runtime.js --post-js runtime_emscripten.js

snippet.c: libstdweb_emscripten_working.a
	$(GENERATE_SCRIPT) target/.cargo-web/snippets snippet.c

libstdweb_emscripten_working.a: src/lib.rs
	cargo web build --target wasm32-unknown-emscripten
	cp target/wasm32-unknown-emscripten/debug/libstdweb_emscripten_working.a .

apply_patch: $(MARKER_FILE)

$(MARKER_FILE): $(PATCH_FILE)
	@echo "Applying patch ../$(PATCH_FILE)"
	cd stdweb && git apply ../$(PATCH_FILE)
	touch $(MARKER_FILE)
	@echo "Patch applied"

clean:
	rm -f $(CLEAN_FILES)
	rm -f $(MARKER_FILE)
	cd stdweb && git reset --hard HEAD

.PHONY: all clean apply_patch
