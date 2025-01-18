---
date: 2019-10-10
featured-image: fraction-math-in-every-language.jpg
last-modified: 2025-01-18
layout: default
tags:
- fraction-math
title: Fraction Math
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

There are 13 articles:

- [Fraction Math in Algol68](https://sampleprograms.io/projects/fraction-math/algol68)
- [Fraction Math in Beef](https://sampleprograms.io/projects/fraction-math/beef)
- [Fraction Math in C](https://sampleprograms.io/projects/fraction-math/c)
- [Fraction Math in C#](https://sampleprograms.io/projects/fraction-math/c-sharp)
- [Fraction Math in C++](https://sampleprograms.io/projects/fraction-math/c-plus-plus)
- [Fraction Math in Commodore Basic](https://sampleprograms.io/projects/fraction-math/commodore-basic)
- [Fraction Math in Euphoria](https://sampleprograms.io/projects/fraction-math/euphoria)
- [Fraction Math in Go](https://sampleprograms.io/projects/fraction-math/go)
- [Fraction Math in Mathematica](https://sampleprograms.io/projects/fraction-math/mathematica)
- [Fraction Math in Php](https://sampleprograms.io/projects/fraction-math/php)
- [Fraction Math in Python](https://sampleprograms.io/projects/fraction-math/python)
- [Fraction Math in Rust](https://sampleprograms.io/projects/fraction-math/rust)
- [Fraction Math in Swift](https://sampleprograms.io/projects/fraction-math/swift)

***

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Fizz Buzz)](https://sampleprograms.io/projects/fizz-buzz)

</div>

<div id="next" markdown="1">

[Next Project (Hello World) -->](https://sampleprograms.io/projects/hello-world)

</div>

</nav>