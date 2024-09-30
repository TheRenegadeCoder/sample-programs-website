---
authors:
- rzuckerm
date: 2023-08-02
featured-image: quine-in-every-language.jpg
last-modified: 2023-08-07
layout: default
tags:
- gnu-make
- quine
title: Quine in Gnu Make
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/quine/gnu-make/how-to-implement-the-solution.md
- sources/programs/quine/gnu-make/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Quine](https://sampleprograms.io/projects/quine) in [Gnu Make](https://sampleprograms.io/languages/gnu-make) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```gnu_make
q=$(info q=$(value q))$(info $$(q))$(eval q:;@:)
$(q)

```

{% endraw %}

Quine in [Gnu Make](https://sampleprograms.io/languages/gnu-make) was written by:

- rzuckerm

This article was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

I can't take credit for this solution. I got the code from [Rosetta Code][1].

Let's break it down. First, there is this variable assignment:

```make
q=$(info q=$(value q))$(info $$(q))$(eval q:;@:)
```

Since `=` is used, [deferred evaluation is done][2]. This means that the
expression is not evaluated until it is needs to be. In other words, the
variable `q` is just set to the value after the equal sign.

The real magic doesn't happen until this line:

```make
$(q)
```

This forces `q` to be evaluted. The first expression to be evaluated is this:

```make
$(info q=$(value q))
```

The [value][3] function returns the value of the specified variable without
expanding it. The [info][4] function displays the text that follows it.
Putting those together, this displays the `q=` followed by the value of `q`.
This displays the first line of the code.

The second expression to be evaluated is this:

```make
$(info $$(q))
```

The `$$` is just the way that a literal `$` character must be represented
since `$` has a special meaning in GNU Make. Therefore, this just displays the
second line of the code.

The final expression to be evaluated is this:

```make
$(eval q:;@:)
```

The [eval][5] function evaluation the expression that follows it and returns
an empty string. In this case, it is creating this target:

```make
q:;@:
```

Since GNU Make is a build system, it needs something to build, or else it will
give this error:

```
make: *** No targets.  Stop.
```

To give `make` something to do, this "do nothing" target called `q` is
provided. The `q` target is written in the [alternate form][6].

```make
target:;command
```

This means that whenever the target needs to be built, `make` will execute the
command following the semicolon. By default, `make` [echoes each command][7]
that it executes. To suppress this, `@` may be used before the command. The
[colon (:) command][8] just exits with non-error status.


[1]: https://rosettacode.org/wiki/Quine#make
[2]: https://www.gnu.org/software/make/manual/html_node/Reading-Makefiles.html
[3]: https://www.gnu.org/software/make/manual/html_node/Value-Function.html
[4]: https://www.gnu.org/software/make/manual/html_node/Make-Control-Functions.html
[5]: https://www.gnu.org/software/make/manual/html_node/Eval-Function.html
[6]: https://www.gnu.org/software/make/manual/html_node/Rule-Syntax.html
[7]: https://www.gnu.org/software/make/manual/html_node/Echoing.html
[8]: https://man7.org/linux/man-pages/man1/colon.1p.html


## How to Run the Solution

To run this program, download and install the latest GNU Make using these
instructions:

* [Windows][9]
* For [Linux][10], see "How to Download" section
* [Mac][11]

Download a copy of [Quine in GNU Make][12], and run this command:

```
make -sf quine.mk
```

[9]: https://leangaurav.medium.com/how-to-setup-install-gnu-make-on-windows-324480f1da69
[10]: https://www.incredibuild.com/integrations/gnu-make
[11]: https://formulae.brew.sh/formula/make
[12]: https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/g/gnu-make/quine.mk
