---
authors:
- rzuckerm
date: 2023-07-11
featured-image: hello-world-in-gnu-make.jpg
last-modified: 2023-07-17
layout: default
tags:
- gnu-make
- hello-world
title: Hello World in Gnu Make
---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Gnu Make](https://sampleprograms.io/languages/gnu-make) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```gnu_make
$(info Hello, World!)

.PHONY: all
all: ;@:

```

{% endraw %}

Hello World in [Gnu Make](https://sampleprograms.io/languages/gnu-make) was written by:

- rzuckerm

This article was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

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
[2]: https://www.gnu.org/software/make/manual/html_node/Phony-Targets.html#index-phony-targets
[3]: https://www.gnu.org/software/make/manual/html_node/Echoing.html#index-_0040-_0028in-recipes_0029
[4]: https://www.gnu.org/software/make/manual/html_node/Rule-Syntax.html
[5]: https://www.gnu.org/software/make/manual/html_node/Syntax-of-Functions.html#index-_0024_002c-in-function-call
[6]: https://man7.org/linux/man-pages/man1/colon.1p.html


## How to Run the Solution

To run this program just download [the latest GNU Make][7], download a copy
of [Hello World in GNU Make][8], and run this command:

```
make -sf hello-world.mk
```

[7]: https://www.gnu.org/software/make/#download
[8]: https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/g/gnu-make/hello-world.mk
