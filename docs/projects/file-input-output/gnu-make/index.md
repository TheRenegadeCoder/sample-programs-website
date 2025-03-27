---
authors:
- Ron Zuckerman
- rzuckerm
date: 2023-07-13
featured-image: file-input-output-in-every-language.jpg
last-modified: 2023-07-29
layout: default
tags:
- file-input-output
- gnu-make
title: File Input Output in Gnu Make
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/gnu-make/how-to-implement-the-solution.md
- sources/programs/file-input-output/gnu-make/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Gnu Make](https://sampleprograms.io/languages/gnu-make) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```gnu_make
define TEXT
Hello from GNU Make
Here are some lines:
This is line 1
This is line 2
Goodbye!
endef

$(file >output.txt,$(TEXT))
$(info $(file <output.txt))

.PHONY: all
all: ;@:

```

{% endraw %}

File Input Output in [Gnu Make](https://sampleprograms.io/languages/gnu-make) was written by:

- rzuckerm

This article was written by:

- Ron Zuckerman
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

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


## How to Run the Solution

To run this program, download and install the latest GNU Make using these
instructions:

* [Windows][8]
* For [Linux][9], see "How to Download" section
* [Mac][10]

Download a copy of [File Input Output in GNU Make][11], and run this command:

```
make -sf file-input-output.mk
```

[8]: https://leangaurav.medium.com/how-to-setup-install-gnu-make-on-windows-324480f1da69
[9]: https://www.incredibuild.com/integrations/gnu-make
[10]: https://formulae.brew.sh/formula/make
[11]: https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/g/gnu-make/file-input-output.mk
