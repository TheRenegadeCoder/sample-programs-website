---
date: 2018-08-07
featured-image: quine-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- quine
title: Quine
title1: Quine
title2: ''
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/projects/quine/description.md
- sources/projects/quine/requirements.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the Quine page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

This article was written by:

- Jeremy Grifski
- Ron Zuckerman
- rzuckerm

## Description

For those of you that don't know, a quine is a program which can replicate
itself--or more specifically:

> A quine is a non-empty computer program which takes no input and produces a
> copy of its own source code as its only output.

Thanks, [Wikipedia][1]!

[1]: https://en.wikipedia.org/wiki/Quine_(computing)


## Requirements

For the purposes of this repo, the solution should be simple. We're not here
to play code golf, but we're also not here to practice obfuscation. Just be
reasonable with your solution. Finally, the solution must **not** read its own
source code file. For example, this is **not** a permissible solution:

```python
with open("quine.py") as f:
    print(f.read())
```


## Testing

Verify that the actual output matches the expected output
(see [Requirements](#requirements)).


## Articles

There are 37 articles:

- [Quine in ALGOL 60](/projects/quine/algol60)
- [Quine in ALGOL 68](/projects/quine/algol68)
- [Quine in AWK](/projects/quine/awk)
- [Quine in Bash](/projects/quine/bash)
- [Quine in Beef](/projects/quine/beef)
- [Quine in Befunge](/projects/quine/befunge)
- [Quine in C](/projects/quine/c)
- [Quine in C#](/projects/quine/c-sharp)
- [Quine in C++](/projects/quine/c-plus-plus)
- [Quine in COBOL](/projects/quine/cobol)
- [Quine in CoffeeScript](/projects/quine/coffeescript)
- [Quine in Commodore BASIC](/projects/quine/commodore-basic)
- [Quine in Cython](/projects/quine/cython)
- [Quine in Dg](/projects/quine/dg)
- [Quine in Euphoria](/projects/quine/euphoria)
- [Quine in F#](/projects/quine/f-sharp)
- [Quine in GNU Make](/projects/quine/gnu-make)
- [Quine in Go](/projects/quine/go)
- [Quine in Haskell](/projects/quine/haskell)
- [Quine in Java](/projects/quine/java)
- [Quine in JavaScript](/projects/quine/javascript)
- [Quine in Kotlin](/projects/quine/kotlin)
- [Quine in Mathematica](/projects/quine/mathematica)
- [Quine in PHP](/projects/quine/php)
- [Quine in Pascal](/projects/quine/pascal)
- [Quine in Perl](/projects/quine/perl)
- [Quine in PowerShell](/projects/quine/powershell)
- [Quine in Python](/projects/quine/python)
- [Quine in Ruby](/projects/quine/ruby)
- [Quine in Rust](/projects/quine/rust)
- [Quine in Swift](/projects/quine/swift)
- [Quine in Tcl](/projects/quine/tcl)
- [Quine in TypeScript](/projects/quine/typescript)
- [Quine in Visual Basic](/projects/quine/visual-basic)
- [Quine in Whitespace](/projects/quine/whitespace)
- [Quine in m4](/projects/quine/m4)
- [Quine in x86-64](/projects/quine/x86-64)

***

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Quick Sort)](/projects/quick-sort)

</div>

<div id="next" markdown="1">

[Next Project (Remove All Whitespace) -->](/projects/remove-all-whitespace)

</div>

</nav>