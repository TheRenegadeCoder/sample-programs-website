The [define][1] keyword assigns a multi-line value to a variable. The value
is terminated with an `endef` keyword. For this sample program, this is the
text that will be written to the output file:

```make
define TEXT
Hello from GNU Make
Here are some lines:
This is line 1
This is line 2
Goodbye!
endef
```

The [file][2] function allows files to be read and written. The general form
of this function is this:

```make
$(file op filename[,text])
```

where:

* `op` is the file operation:
  * `<` means input from the specified file.
  * `>` means output to the specified file.
  * `>>` means append to the specified file.
* `filename` is the path to the file.
* `text` is the text to be written to the file for the `>` and `>>` file
  operations.

This writes the text (stored in the `TEXT` variable) to a file called
`output.txt`:

```make
$(file >output.txt,$(TEXT))
```

This reads the text from `output.txt` and displays it using the [info][3]
function.

```make
$(info $(file <output.txt))
```

Since GNU Make is a build system, it needs something to build, or else it will
give this error:

```
make: *** No targets.  Stop.
```

To give `make` something to do, a "do nothing" target called `all` is provided
like this:

```make
.PHONY: all
all: ;@:
```

The [.PHONY][4] keyword specifies targets that will always be built, whether or
not they exist. In this case, that is the `all` target. This target is written
in the [alternate form][5] for brevity:

```make
target: ;command
```

This means that whenever the target needs to be built, `make` will execute the
command following the semicolon. By default, `make` [echoes each command][6]
that it executes. To suppress this, `@` may be used before the command. The
[colon (:) command][7] just exits with non-error status.


[1]: https://www.gnu.org/software/make/manual/html_node/Multi_002dLine.html
[2]: https://www.gnu.org/software/make/manual/html_node/File-Function.html
[3]: https://www.gnu.org/software/make/manual/html_node/Make-Control-Functions.html
[4]: https://www.gnu.org/software/make/manual/html_node/Phony-Targets.html
[5]: https://www.gnu.org/software/make/manual/html_node/Rule-Syntax.html
[6]: https://www.gnu.org/software/make/manual/html_node/Echoing.html
[7]: https://man7.org/linux/man-pages/man1/colon.1p.html
