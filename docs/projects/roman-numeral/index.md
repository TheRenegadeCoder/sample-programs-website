---
date: 2018-10-07
featured-image: roman-numeral-in-every-language.jpg
last-modified: 2026-05-03
layout: default
tags:
- roman-numeral
title: Roman Numeral
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/projects/roman-numeral/description.md
- sources/projects/roman-numeral/requirements.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the Roman Numeral page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

This article was written by:

- Jeremy Grifski

## Description

Roman numerals are the numbers that were used in ancient Rome, which employed
combinations of letters from the Latin alphabet (I, V, X, L, C, D and M).

The following table shows the letter to decimal mapping:

| Letter | Decimal |
| ------ | ------- |
| I      | 1       |
| V      | 5       |
| X      | 10      |
| L      | 50      |
| C      | 100     |
| D      | 500     |
| M      | 1000    |

Stringing together these digits yields a value that is the sum of their
respective mappings. However, there is a catch. Roman numerals must appears in
order of greatest to least. If a smaller value appears before a larger one,
the smaller value is subtracted from the total.

As a result, a string like `XV` would evaluate to 15 while `XIV` would
evaluate to 14.

Of course, there are other limitations, but we'll ignore those for simplicity.


## Requirements

Create a file called Roman Numeral Conversion using whatever naming
convention is appropriate for the choice language.

Using the table above, write a sample program which accepts a Roman numeral on
the command line and outputs its decimal value on standard output. Be careful
to appropriately handle invalid input such as `XT`. More on that in the testing
section.

_Please_ make sure your program is executable. In other words, the solution
should be able to be called in the appropriate environment with a string
of roman numerals (i.e. `./roman-numeral-conversion XXVI`).


## Testing

Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Roman Numeral.
In order to keep things simple, we split up the testing as follows:

- Roman Numeral Valid Tests
- Roman Numeral Invalid Tests

### Roman Numeral Valid Tests

| Description | Input | Output |
| ----------- | ----- | ------ |
| Empty Input | "" | "0" |
| Single I | "I" | "1" |
| Single V | "V" | "5" |
| Single X | "X" | "10" |
| Single L | "L" | "50" |
| Single C | "C" | "100" |
| Single D | "D" | "500" |
| Single M | "M" | "1000" |
| Addition | "XXV" | "25" |
| Subtraction | "XIV" | "14" |

### Roman Numeral Invalid Tests

| Description | Input | Output |
| ----------- | ----- | ------ |
| No Input |  | "Usage: please provide a string of roman numerals" |
| Invalid Input | "XT" | "Error: invalid string of roman numerals" |


## Articles

There are 29 articles:

- [Roman Numeral in ALGOL 60](https://sampleprograms.io/projects/roman-numeral/algol60)
- [Roman Numeral in ALGOL 68](https://sampleprograms.io/projects/roman-numeral/algol68)
- [Roman Numeral in AWK](https://sampleprograms.io/projects/roman-numeral/awk)
- [Roman Numeral in Beef](https://sampleprograms.io/projects/roman-numeral/beef)
- [Roman Numeral in C](https://sampleprograms.io/projects/roman-numeral/c)
- [Roman Numeral in C#](https://sampleprograms.io/projects/roman-numeral/c-sharp)
- [Roman Numeral in C++](https://sampleprograms.io/projects/roman-numeral/c-plus-plus)
- [Roman Numeral in COBOL](https://sampleprograms.io/projects/roman-numeral/cobol)
- [Roman Numeral in Commodore BASIC](https://sampleprograms.io/projects/roman-numeral/commodore-basic)
- [Roman Numeral in Dart](https://sampleprograms.io/projects/roman-numeral/dart)
- [Roman Numeral in Euphoria](https://sampleprograms.io/projects/roman-numeral/euphoria)
- [Roman Numeral in F#](https://sampleprograms.io/projects/roman-numeral/f-sharp)
- [Roman Numeral in Go](https://sampleprograms.io/projects/roman-numeral/go)
- [Roman Numeral in Haskell](https://sampleprograms.io/projects/roman-numeral/haskell)
- [Roman Numeral in Java](https://sampleprograms.io/projects/roman-numeral/java)
- [Roman Numeral in JavaScript](https://sampleprograms.io/projects/roman-numeral/javascript)
- [Roman Numeral in Lua](https://sampleprograms.io/projects/roman-numeral/lua)
- [Roman Numeral in Mathematica](https://sampleprograms.io/projects/roman-numeral/mathematica)
- [Roman Numeral in PHP](https://sampleprograms.io/projects/roman-numeral/php)
- [Roman Numeral in Pascal](https://sampleprograms.io/projects/roman-numeral/pascal)
- [Roman Numeral in PowerShell](https://sampleprograms.io/projects/roman-numeral/powershell)
- [Roman Numeral in Python](https://sampleprograms.io/projects/roman-numeral/python)
- [Roman Numeral in Ruby](https://sampleprograms.io/projects/roman-numeral/ruby)
- [Roman Numeral in Rust](https://sampleprograms.io/projects/roman-numeral/rust)
- [Roman Numeral in Swift](https://sampleprograms.io/projects/roman-numeral/swift)
- [Roman Numeral in Tcl](https://sampleprograms.io/projects/roman-numeral/tcl)
- [Roman Numeral in TypeScript](https://sampleprograms.io/projects/roman-numeral/typescript)
- [Roman Numeral in Visual Basic](https://sampleprograms.io/projects/roman-numeral/visual-basic)
- [Roman Numeral in m4](https://sampleprograms.io/projects/roman-numeral/m4)

***

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Reverse String)](https://sampleprograms.io/projects/reverse-string)

</div>

<div id="next" markdown="1">

[Next Project (Rot13) -->](https://sampleprograms.io/projects/rot13)

</div>

</nav>