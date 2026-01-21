---
date: 2026-01-19
featured-image: zeckendorf-in-every-language.png
last-modified: 2026-01-20
layout: default
tags:
- zeckendorf
title: Zeckendorf
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/projects/zeckendorf/description.md
- sources/projects/zeckendorf/requirements.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the Zeckendorf page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

This article was written by:

- rzuckerm

## Description

[Edouard Zeckendorf][3] was a Belgian amateur mathematician who proposed a
[Theorem][1] that states that every non-negative integer (_N_) can be
represented as a sum of distinct non-consecutive [Fibonacci Numbers][2]. In
other words,

* _N_ = _F_<sub>_c_<sub>1</sub></sub> + _F_<sub>_c_<sub>2</sub></sub> + ... + _F_<sub>_c_<sub>_n_</sub></sub>

where:

* _F_<sub>_k_</sub> is the _k_ th Fibonacci number
* _c_<sub>_i_</sub> &ge; 2
* _c_<sub>_i_ + 1</sub> &gt; _c_<sub>_i_</sub> + 1

Each Fibonacci number (_F_<sub>_k_</sub>) is the sum of the previous two Fibonacci
numbers:

* _F_<sub>0</sub> = 0
* _F_<sub>1</sub> = 1
* _F_<sub>2</sub> = _F_<sub>1</sub> + _F_<sub>0</sub> = 0 + 1 = 1
* _F_<sub>3</sub> = _F_<sub>2</sub> + _F_<sub>1</sub> = 1 + 1 = 2
* ...
* _F_<sub>_k_</sub> = _F_<sub>_k_ - 1</sub> + _F_<sub>_k_ - 2</sub>

This relationship is the reason why non-consecutive Fibonacci numbers are used.

To find the Fibonacci numbers that add up to _N_:

* Find all the Fibonacci numbers up to and including _N_, starting at
  _F_<sub>2</sub>.
* Going from largest to smallest, select each Fibonacci number such that the
  sum of this value plus all the prior selected values is less than or equal to
  _N_.

For example, for _N_ = 67, these are the Fibonacci numbers up to 67:

* 1, 2, 3, 5, 8, 13, 21, 34, 55

Select the appropriate Fibonacci numbers:

| Trial Sum   | Fibonacci Number | Selected |
| :---------: | :--------------: | :------: |
| 0           | 55               | &#9989;  |
| 55          | 34               |          |
| 55          | 21               |          |
| 55          | 13               |          |
| 55          | 8                | &#9989;  |
| 63          | 5                |          |
| 63          | 3                | &#9989;  |
| 66          | 2                |          |
| 66          | 1                | &#9989;  |

Therefore, using the selected numbers, _N_ can be represented as:

* 67 = 55 + 8 + 3 + 1

A possible optimization for this procedure would be to skip Fibonacci
numbers that are consecutive to the last selected value and to terminate
the loop as soon as the sum equals to _N_.

[1]: https://en.wikipedia.org/wiki/Zeckendorf%27s_theorem
[2]: https://en.wikipedia.org/wiki/Fibonacci_sequence
[3]: https://en.wikipedia.org/wiki/Edouard_Zeckendorf


## Requirements

Create a file called "Zeckendorf" using the naming convention appropriate for
your language of choice.

Write a sample program that accepts a single non-negative integer from the
command line and outputs a comma-separated list of Fibonacci numbers whose
sum equals the specified value. For zero, output an empty list. If the command
line argument is missing or not a non-negative integer, output the error
message specified in the [Testing](#testing) section.


## Testing

Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Zeckendorf.
In order to keep things simple, we split up the testing as follows:

- Zeckendorf Valid Tests
- Zeckendorf Invalid Tests

### Zeckendorf Valid Tests

| Description | Input | Output |
| ----------- | ----- | ------ |
| Zero | "0" | "" |
| Small Fibonacci Value | "55" | "55" |
| Small Non-Fibonacci Value | "67" | "55, 8, 3, 1" |
| Large Fibonacci Value | "10946" | "10946" |
| Large Non-Fibonacci Value | "16383" | "10946, 4181, 987, 233, 34, 2" |

### Zeckendorf Invalid Tests

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input | "" |
| Negative Input | "-2" |
| Floating Point Input | "2.6" |
| Non-Numeric Input | "bad" |

All of these tests should output the following:

```
Usage: please input a non-negative integer
```


## Articles

There are 2 articles:

- [Zeckendorf in Algol68](https://sampleprograms.io/projects/zeckendorf/algol68)
- [Zeckendorf in Python](https://sampleprograms.io/projects/zeckendorf/python)

***

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Transpose Matrix)](https://sampleprograms.io/projects/transpose-matrix)

</div>

<div id="next" markdown="1">

[Next Project (Baklava) -->](https://sampleprograms.io/projects/baklava)

</div>

</nav>