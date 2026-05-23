---
date: 2019-10-10
featured-image: fraction-math-in-every-language.jpg
last-modified: 2026-05-18
layout: default
tags:
- fraction-math
title: Fraction Math
title1: Fraction
title2: Math
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/projects/fraction-math/description.md
- sources/projects/fraction-math/requirements.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the Fraction Math page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

This article was written by:

- Jeremy Grifski

## Description

Languages like python have built-in utilities or functions for working with fractions.
Many of these fractions functions follow a similar pattern across programming languages: 
takes a numerator and a denomenator as an attribute.
Perform basic arithmatic and relational operations with operator overloading.


## Requirements

In general, a fractions library should perform the following:

1. Perform arithmatic operation like multiplications, addition etc.
2. Give output for relational operations like >=, >, == etc.

More specifically, begin with creating object instance of fraction class with two attributes:
numerator and denomenator.Using operator overloading feature of langauge implement basic arithmatic
and relational operaions.

For instance `./fraction-math "6/2" "+" "1/4"` would output `13/4`

In addition, there should be some error handling for situations where the user
doesn't supply any input.


## Testing

Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Fraction Math.
In order to keep things simple, we split up the testing as follows:

- Fractions Valid Tests
- Fractions Invalid Tests

### Fractions Valid Tests

| Description | Fraction 1 | Operation | Fraction 2 | Output |
| ----------- | ---------- | --------- | ---------- | ------ |
| Sample Input: Addition | "2/3" | "+" | "4/5" | "22/15" |
| Sample Input: Multiplication | "2/3" | "*" | "4/5" | "8/15" |
| Sample Input: Subtraction | "2/3" | "-" | "4/5" | "-2/15" |
| Sample Input: Division | "2/3" | "/" | "4/5" | "5/6" |
| Sample Input: Equals | "2/3" | "==" | "4/5" | "0" |
| Sample Input: Greater Than | "2/3" | ">" | "4/5" | "0" |
| Sample Input: Less Than | "2/3" | "<" | "4/5" | "1" |
| Sample Input: Greater Than Equals | "2/3" | ">=" | "4/5" | "0" |
| Sample Input: Less Than Equals | "2/3" | "<=" | "4/5" | "1" |
| Sample Input: Not Equals | "2/3" | "!=" | "4/5" | "1" |

### Fractions Invalid Tests

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input | "" |

All of these tests should output the following:

```
Usage: ./fraction-math operand1 operator operand2
```


## Articles

There are 29 articles:

- [Fraction Math in ALGOL 60](/projects/fraction-math/algol60)
- [Fraction Math in ALGOL 68](/projects/fraction-math/algol68)
- [Fraction Math in AWK](/projects/fraction-math/awk)
- [Fraction Math in Ada](/projects/fraction-math/ada)
- [Fraction Math in Beef](/projects/fraction-math/beef)
- [Fraction Math in C](/projects/fraction-math/c)
- [Fraction Math in C#](/projects/fraction-math/c-sharp)
- [Fraction Math in C++](/projects/fraction-math/c-plus-plus)
- [Fraction Math in COBOL](/projects/fraction-math/cobol)
- [Fraction Math in Commodore BASIC](/projects/fraction-math/commodore-basic)
- [Fraction Math in Euphoria](/projects/fraction-math/euphoria)
- [Fraction Math in F#](/projects/fraction-math/f-sharp)
- [Fraction Math in Go](/projects/fraction-math/go)
- [Fraction Math in Haskell](/projects/fraction-math/haskell)
- [Fraction Math in Java](/projects/fraction-math/java)
- [Fraction Math in JavaScript](/projects/fraction-math/javascript)
- [Fraction Math in Mathematica](/projects/fraction-math/mathematica)
- [Fraction Math in Modula-2](/projects/fraction-math/modula2)
- [Fraction Math in PHP](/projects/fraction-math/php)
- [Fraction Math in Pascal](/projects/fraction-math/pascal)
- [Fraction Math in PowerShell](/projects/fraction-math/powershell)
- [Fraction Math in Python](/projects/fraction-math/python)
- [Fraction Math in Ruby](/projects/fraction-math/ruby)
- [Fraction Math in Rust](/projects/fraction-math/rust)
- [Fraction Math in Swift](/projects/fraction-math/swift)
- [Fraction Math in Tcl](/projects/fraction-math/tcl)
- [Fraction Math in TypeScript](/projects/fraction-math/typescript)
- [Fraction Math in Visual Basic](/projects/fraction-math/visual-basic)
- [Fraction Math in m4](/projects/fraction-math/m4)

***

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Fizz Buzz)](/projects/fizz-buzz)

</div>

<div id="next" markdown="1">

[Next Project (Hello World) -->](/projects/hello-world)

</div>

</nav>