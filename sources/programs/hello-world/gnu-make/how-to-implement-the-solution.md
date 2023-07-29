The [info][1] function displays the text that follows it, so this just displays
"Hello, World!":

```make
$(info Hello, World!)
```

In general, [all functions in GNU Make][5] have this form:

```make
$(function arguments)
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

The [.PHONY][2] keyword specifies targets that will always be built, whether or
not they exist. In this case, that is the `all` target. This target is written
in the [alternate form][4] for brevity:

```make
target: ;command
```

This means that whenever the target needs to be built, `make` will execute the
command following the semicolon. By default, `make` [echoes each command][3]
that it executes. To suppress this, `@` may be used before the command. The
[colon (:) command][6] just exits with non-error status.

[1]: https://www.gnu.org/software/make/manual/html_node/Make-Control-Functions.html#index-info
[2]: https://www.gnu.org/software/make/manual/html_node/Phony-Targets.html
[3]: https://www.gnu.org/software/make/manual/html_node/Echoing.html
[4]: https://www.gnu.org/software/make/manual/html_node/Rule-Syntax.html
[5]: https://www.gnu.org/software/make/manual/html_node/Syntax-of-Functions.html
[6]: https://man7.org/linux/man-pages/man1/colon.1p.html
