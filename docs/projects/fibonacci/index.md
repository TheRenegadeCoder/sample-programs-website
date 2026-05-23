---
date: 2018-10-02
featured-image: fibonacci-in-every-language.jpg
last-modified: 2026-05-17
layout: default
tags:
- fibonacci
title: Fibonacci
title1: Fibonacci
title2: ''
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/projects/fibonacci/description.md
- sources/projects/fibonacci/requirements.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the Fibonacci page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

This article was written by:

- Jeremy Grifski

## Description

In mathematics, the Fibonacci numbers are the numbers in the following integer
sequence, called the Fibonacci sequence, and characterized by the fact that
every number after the first two is the sum of the two preceding ones:

    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...


## Requirements

For this sample program, each solution should leverage dynamic programming to produce this
list up to the nth term. For instance, `./fib 5` on the command line should output

```
1: 1
2: 1
3: 2
4: 3
5: 5
```

In addition, there should be some error handling for situations where the user
doesn't supply any input or the user supplies input that is not a number
(i.e. `./fib` or `./fib hello`, respectively).


## Testing

Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Fibonacci.
In order to keep things simple, we split up the testing as follows:

- Fibonacci Valid Tests
- Fibonacci Invalid Tests

### Fibonacci Valid Tests

| Description | Input | Output |
| ----------- | ----- | ------ |
| Sample Input 0 | "0" |  |
| Sample Input 1 | "1" | "1: 1" |
| Sample Input 2 | "2" | "1: 1"<br>"2: 1" |
| Sample Input 5 | "5" | "1: 1"<br>"2: 1"<br>"3: 2"<br>"4: 3"<br>"5: 5" |
| Sample Input 10 | "10" | "1: 1"<br>"2: 1"<br>"3: 2"<br>"4: 3"<br>"5: 5"<br>"6: 8"<br>"7: 13"<br>"8: 21"<br>"9: 34"<br>"10: 55" |

### Fibonacci Invalid Tests

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input | "" |
| Invalid Input: Not A Number | "a" |

All of these tests should output the following:

```
Usage: please input the count of fibonacci numbers to output
```


## Articles

There are 49 articles:

- [Fibonacci in ALGOL 60](/projects/fibonacci/algol60)
- [Fibonacci in ALGOL 68](/projects/fibonacci/algol68)
- [Fibonacci in AWK](/projects/fibonacci/awk)
- [Fibonacci in Ada](/projects/fibonacci/ada)
- [Fibonacci in Bash](/projects/fibonacci/bash)
- [Fibonacci in Beef](/projects/fibonacci/beef)
- [Fibonacci in Boo](/projects/fibonacci/boo)
- [Fibonacci in C](/projects/fibonacci/c)
- [Fibonacci in C#](/projects/fibonacci/c-sharp)
- [Fibonacci in C++](/projects/fibonacci/c-plus-plus)
- [Fibonacci in COBOL](/projects/fibonacci/cobol)
- [Fibonacci in Commodore BASIC](/projects/fibonacci/commodore-basic)
- [Fibonacci in Dart](/projects/fibonacci/dart)
- [Fibonacci in Elvish](/projects/fibonacci/elvish)
- [Fibonacci in Euphoria](/projects/fibonacci/euphoria)
- [Fibonacci in F#](/projects/fibonacci/f-sharp)
- [Fibonacci in Fortran](/projects/fibonacci/fortran)
- [Fibonacci in Go](/projects/fibonacci/go)
- [Fibonacci in Groovy](/projects/fibonacci/groovy)
- [Fibonacci in Haskell](/projects/fibonacci/haskell)
- [Fibonacci in Java](/projects/fibonacci/java)
- [Fibonacci in JavaScript](/projects/fibonacci/javascript)
- [Fibonacci in Julia](/projects/fibonacci/julia)
- [Fibonacci in Kotlin](/projects/fibonacci/kotlin)
- [Fibonacci in Lisp](/projects/fibonacci/lisp)
- [Fibonacci in Lua](/projects/fibonacci/lua)
- [Fibonacci in Mathematica](/projects/fibonacci/mathematica)
- [Fibonacci in MoonScript](/projects/fibonacci/moonscript)
- [Fibonacci in Nim](/projects/fibonacci/nim)
- [Fibonacci in OCaml](/projects/fibonacci/ocaml)
- [Fibonacci in Objective-C](/projects/fibonacci/objective-c)
- [Fibonacci in Octave](/projects/fibonacci/octave)
- [Fibonacci in Odin](/projects/fibonacci/odin)
- [Fibonacci in PHP](/projects/fibonacci/php)
- [Fibonacci in Pascal](/projects/fibonacci/pascal)
- [Fibonacci in Perl](/projects/fibonacci/perl)
- [Fibonacci in PowerShell](/projects/fibonacci/powershell)
- [Fibonacci in Python](/projects/fibonacci/python)
- [Fibonacci in R](/projects/fibonacci/r)
- [Fibonacci in Racket](/projects/fibonacci/racket)
- [Fibonacci in Ruby](/projects/fibonacci/ruby)
- [Fibonacci in Rust](/projects/fibonacci/rust)
- [Fibonacci in Scala](/projects/fibonacci/scala)
- [Fibonacci in Swift](/projects/fibonacci/swift)
- [Fibonacci in TI-BASIC](/projects/fibonacci/ti-basic)
- [Fibonacci in Tcl](/projects/fibonacci/tcl)
- [Fibonacci in TypeScript](/projects/fibonacci/typescript)
- [Fibonacci in Visual Basic](/projects/fibonacci/visual-basic)
- [Fibonacci in m4](/projects/fibonacci/m4)

***

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Factorial)](/projects/factorial)

</div>

<div id="next" markdown="1">

[Next Project (File Input Output) -->](/projects/file-input-output)

</div>

</nav>