---

title: Palindromic Number in Every Language
layout: default
date: 2020-10-07
last-modified: 2022-10-10
featured-image: 
tags: [palindromic-number]
authors:
  - anohene1
  - the_renegade_coder

---

Welcome to the Palindromic Number page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

## Description

A palindromic number is a number that reads the same backward and forward.
Example: 343, 121, 909, 222


## Requirements

To implement this algorithm, your program should accept a positive integer
from the command line as follows:

```console
./palindromic-number.lang 56765
```

And report whether or not that number is a palindrome using the values
"true" and "false." See testing below for examples.


## Testing

Every project in the Sample Programs repo should be tested. In this section, we specify the set of tests specific to Palindromic Number. To keep things simple, we split up testing into two subsets: valid and invalid. Valid tests refer to tests that occur under correct input conditions. Invalid tests refer to tests that occur on bad input (e.g., letters instead of numbers).

### Valid Tests

| Description                  | Positive Integer | Output |
| ---------------------------- | ---------------- | ------ |
| sample input: one digit      | 7                | true   |
| sample input: routine        | 232              | true   |
| sample input: not palindrome | 521              | false  |


### Invalid Tests

| Description                    | Input |
| ------------------------------ | ----- |
| no input                       | None  |
| empty input                    | ""    |
| invalid input: not a number    | a     |
| invalid input: negative number | -5    |

All invalid tests should spit out a usage statement in the following form: 

```
Usage: please input a non-negative integer
```


## Articles

- [Palindromic Number in C](https://sampleprograms.io/projects/palindromic-number/c)
- [Palindromic Number in C++](https://sampleprograms.io/projects/palindromic-number/c-plus-plus)
- [Palindromic Number in Java](https://sampleprograms.io/projects/palindromic-number/java)
- [Palindromic Number in Javascript](https://sampleprograms.io/projects/palindromic-number/javascript)
- [Palindromic Number in Kotlin](https://sampleprograms.io/projects/palindromic-number/kotlin)
- [Palindromic Number in Pascal](https://sampleprograms.io/projects/palindromic-number/pascal)
- [Palindromic Number in Perl](https://sampleprograms.io/projects/palindromic-number/perl)
- [Palindromic Number in Python](https://sampleprograms.io/projects/palindromic-number/python)

---

<nav class="project-nav">

<div id="prev">

[<-- Previous Project (Minimum Spanning Tree)](https://sampleprograms.io/projects/minimum-spanning-tree)

</div>

<div id="next">

[Next Project (Prime Number) -->](https://sampleprograms.io/projects/prime-number)

</div>

</nav>