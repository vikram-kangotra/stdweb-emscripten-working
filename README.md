# Stdweb Emscripten Working

This is a working example of `stdweb` with `emscripten`. It uses `cargo web` to generate the snippets and then the snippets are joined to form a `snipped.c` file which can then be compiled with `emcc`. 
The `snippet.c` file contains the emscripten code required to use stdweb. 

All the instructions are in the `Makefile`.

### How to clone

```
git clone https://github.com/vikram-kangotra/stdweb-emscripten-working.git --recursive
```

### How to run

```
make
```

This will generate the necessary files. Then serve the html file.
