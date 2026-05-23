---
date: 2018-11-20
featured-image: rot13-in-every-language.jpg
last-modified: 2026-05-14
layout: default
tags:
- rot13
title: Rot13
title1: Rot13
title2: ''
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/projects/rot13/description.md
- sources/projects/rot13/requirements.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the Rot13 page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

This article was written by:

- Jeremy Grifski
- Ron Zuckerman

## Description

ROT13 is a letter substitution cipher where every letter is replaced by the
letter 13 letters after it alphabetically and wrapping from `Z` to `A` if necessary:

    ABCDEFGHIJKLMNOPQRSTUVWXYZ -> NOPQRSTUVWXYZABCDEFGHIJKLM

As a result, encrypted strings can be decrypted using the same algorithm:

    NOPQRSTUVWXYZABCDEFGHIJKLM -> ABCDEFGHIJKLMNOPQRSTUVWXYZ


## Requirements

Write a sample program that takes a string of text as input.
It should then encrypt the inputted text using ROT13 and output the result to the console.

```console
$ ./rot13.lang "the quick brown fox jumped over the lazy dog"
gur dhvpx oebja sbk whzcrq bire gur ynml qbt
```

The solution should handle both lower case and capital letters

```console
$ ./rot13.lang "THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG"
GUR DHVPX OEBJA SBK WHZCRQ BIRE GUR YNML QBT
```

Any characters/symbols besides a-z and A-Z should be ignored.

```console
$ ./rot13.lang "The quick brown fox jumped. Was it over the lazy dog?"
Gur dhvpx oebja sbk whzcrq. Jnf vg bire gur ynml qbt?
```

In addition, there should be some error handling for situations where the user
doesn't supply any input.


## Testing

Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Rot13.
In order to keep things simple, we split up the testing as follows:

- Rot13 Valid Tests
- Rot13 Invalid Tests

### Rot13 Valid Tests

| Description | Input | Output |
| ----------- | ----- | ------ |
| Sample Input Lower Case | "the quick brown fox jumped over the lazy dog" | "gur dhvpx oebja sbk whzcrq bire gur ynml qbt" |
| Sample Input Upper Case | "THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG" | "GUR DHVPX OEBJA SBK WHZCRQ BIRE GUR YNML QBT" |
| Sample Input Punctuation | "The quick brown fox jumped. Was it over the lazy dog?" | "Gur dhvpx oebja sbk whzcrq. Jnf vg bire gur ynml qbt?" |

### Rot13 Invalid Tests

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input | "" |

All of these tests should output the following:

```
Usage: please provide a string to encrypt
```


## Articles

There are 34 articles:

- [Rot13 in ALGOL 60](/projects/rot13/algol60)
- [Rot13 in ALGOL 68](/projects/rot13/algol68)
- [Rot13 in AWK](/projects/rot13/awk)
- [Rot13 in Beef](/projects/rot13/beef)
- [Rot13 in Brainfuck](/projects/rot13/brainfuck)
- [Rot13 in C](/projects/rot13/c)
- [Rot13 in C#](/projects/rot13/c-sharp)
- [Rot13 in C++](/projects/rot13/c-plus-plus)
- [Rot13 in COBOL](/projects/rot13/cobol)
- [Rot13 in Commodore BASIC](/projects/rot13/commodore-basic)
- [Rot13 in Dart](/projects/rot13/dart)
- [Rot13 in Elvish](/projects/rot13/elvish)
- [Rot13 in Euphoria](/projects/rot13/euphoria)
- [Rot13 in F#](/projects/rot13/f-sharp)
- [Rot13 in Go](/projects/rot13/go)
- [Rot13 in Haskell](/projects/rot13/haskell)
- [Rot13 in Java](/projects/rot13/java)
- [Rot13 in JavaScript](/projects/rot13/javascript)
- [Rot13 in Kotlin](/projects/rot13/kotlin)
- [Rot13 in Lua](/projects/rot13/lua)
- [Rot13 in Mathematica](/projects/rot13/mathematica)
- [Rot13 in PHP](/projects/rot13/php)
- [Rot13 in Pascal](/projects/rot13/pascal)
- [Rot13 in Perl](/projects/rot13/perl)
- [Rot13 in PowerShell](/projects/rot13/powershell)
- [Rot13 in Python](/projects/rot13/python)
- [Rot13 in Ruby](/projects/rot13/ruby)
- [Rot13 in Rust](/projects/rot13/rust)
- [Rot13 in Swift](/projects/rot13/swift)
- [Rot13 in TI-BASIC](/projects/rot13/ti-basic)
- [Rot13 in Tcl](/projects/rot13/tcl)
- [Rot13 in TypeScript](/projects/rot13/typescript)
- [Rot13 in Visual Basic](/projects/rot13/visual-basic)
- [Rot13 in m4](/projects/rot13/m4)

***

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Roman Numeral)](/projects/roman-numeral)

</div>

<div id="next" markdown="1">

[Next Project (Selection Sort) -->](/projects/selection-sort)

</div>

</nav>