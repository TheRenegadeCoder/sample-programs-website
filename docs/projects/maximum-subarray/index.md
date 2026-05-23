---
date: 2020-10-14
featured-image: maximum-subarray-in-every-language.jpg
last-modified: 2026-05-14
layout: default
tags:
- maximum-subarray
title: Maximum Subarray
title1: Maximum
title2: Subarray
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/projects/maximum-subarray/description.md
- sources/projects/maximum-subarray/requirements.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the Maximum Subarray page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

This article was written by:

- Jeremy Grifski

## Description

Given an array, the maximum subarray is the subarray which gives the maximum sum possible in the array.
Kadane's algorithm is a popular algorithm used to find out this maximum sum value.

Note: A subarray is any continuous portion of an array.

For example:

Given array: `[-1, -2, 1, 2, 3, 4, 5, 23]`

Max sum value of a subarray: `38`

Explanation: The subarray `[1, 2, 3, 4, 5, 23]` gives the max sum value. `(1 + 2 + 3 + 4 + 5 + 23 = 38)`


## Requirements

You must write an executable program that accepts a string of comma separated integers on `standard input` via the sys args, and outputs the maximum subarray sum value to `standard output`.

Note that the Kadane's algorithm assumes that there is atleast 1 negative integer in the array.
If there is no negative integer, then the max subarray sum value is the sum of all the elements of the array.

Also note that if the input string is empty, then the output is "Usage: Please provide a list of at least two integers to sort in the format: '1, 2, 3, 4, 5'".


## Testing

Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Maximum Subarray.
In order to keep things simple, we split up the testing as follows:

- Maximum Subarray Valid Tests
- Maximum Subarray Invalid Tests

### Maximum Subarray Valid Tests

| Description | Input | Output |
| ----------- | ----- | ------ |
| Sample Input: One Element | "1" | "1" |
| Sample Input: Many Positive Values | "1, 2, 3" | "6" |
| Sample Input: Many Negative Values | "-1, -2, -3" | "-1" |
| Sample Input: Many Negative Followed By Positive Values | "-2, -1, 3, 4, 5" | "12" |
| Sample Input: Many Alternating Positive And Negative Values | "-1, -4, 2, 3, -3, -4, 9" | "9" |

### Maximum Subarray Invalid Tests

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input | "" |

All of these tests should output the following:

```
Usage: Please provide a list of integers in the format: "1, 2, 3, 4, 5"
```


## Articles

There are 28 articles:

- [Maximum Subarray in ALGOL 60](/projects/maximum-subarray/algol60)
- [Maximum Subarray in ALGOL 68](/projects/maximum-subarray/algol68)
- [Maximum Subarray in AWK](/projects/maximum-subarray/awk)
- [Maximum Subarray in Ada](/projects/maximum-subarray/ada)
- [Maximum Subarray in Beef](/projects/maximum-subarray/beef)
- [Maximum Subarray in C](/projects/maximum-subarray/c)
- [Maximum Subarray in C#](/projects/maximum-subarray/c-sharp)
- [Maximum Subarray in C++](/projects/maximum-subarray/c-plus-plus)
- [Maximum Subarray in COBOL](/projects/maximum-subarray/cobol)
- [Maximum Subarray in Commodore BASIC](/projects/maximum-subarray/commodore-basic)
- [Maximum Subarray in Euphoria](/projects/maximum-subarray/euphoria)
- [Maximum Subarray in F#](/projects/maximum-subarray/f-sharp)
- [Maximum Subarray in Go](/projects/maximum-subarray/go)
- [Maximum Subarray in Haskell](/projects/maximum-subarray/haskell)
- [Maximum Subarray in Java](/projects/maximum-subarray/java)
- [Maximum Subarray in JavaScript](/projects/maximum-subarray/javascript)
- [Maximum Subarray in Mathematica](/projects/maximum-subarray/mathematica)
- [Maximum Subarray in PHP](/projects/maximum-subarray/php)
- [Maximum Subarray in Pascal](/projects/maximum-subarray/pascal)
- [Maximum Subarray in PowerShell](/projects/maximum-subarray/powershell)
- [Maximum Subarray in Python](/projects/maximum-subarray/python)
- [Maximum Subarray in Ruby](/projects/maximum-subarray/ruby)
- [Maximum Subarray in Rust](/projects/maximum-subarray/rust)
- [Maximum Subarray in Swift](/projects/maximum-subarray/swift)
- [Maximum Subarray in Tcl](/projects/maximum-subarray/tcl)
- [Maximum Subarray in TypeScript](/projects/maximum-subarray/typescript)
- [Maximum Subarray in Visual Basic](/projects/maximum-subarray/visual-basic)
- [Maximum Subarray in m4](/projects/maximum-subarray/m4)

***

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Maximum Array Rotation)](/projects/maximum-array-rotation)

</div>

<div id="next" markdown="1">

[Next Project (Merge Sort) -->](/projects/merge-sort)

</div>

</nav>