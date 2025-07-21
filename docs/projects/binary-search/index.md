---
date: 2019-10-24
featured-image: binary-search-in-every-language.jpg
last-modified: 2025-07-21
layout: default
tags:
- binary-search
title: Binary Search
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/projects/binary-search/description.md
- sources/projects/binary-search/requirements.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the Binary Search page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

This article was written by:

- Jeremy Grifski

## Description

Binary search is a special type of search function which relies on a few properties
of the search space. First, the search space must have constant time random access
(i.e. an array). In addition, the search space must be sorted by some attribute.
As a consequence, we're able to navigate the search space in O(log(N)) instead of
O(N). 

Jargon aside, binary search works by taking advantage of a sorted collection. As a result,
we don't have to search every element in the collection. Instead, we can try the middle.
If the middle element is greater than the element we want to find, we know that the element
must be "to the left" of that element, assuming the collection is sorted least to greatest. 
From there, we can try the element in the middle of the left half, and so on. 

Eventually, we'll find the element we're looking for, or we'll reach the end of our search.
In either case, we'll only explore O(log(N)) elements. This gives us a dramatic improvement
over linear search.


## Requirements

For the purposes of this project, we'll assume that the search space is a list of integers.
Specifically, we'll accept two inputs on the command line: the list of integers and the
integer to find:

```shell
$ ./binary-search.lang "1, 4, 5, 11, 12" "4"
```

If successful, the script should return `true`. Otherwise, the script should return `false`. 
If any user input errors occur, the script should output the following usage message:
`Usage: please provide a list of sorted integers ("1, 4, 5, 11, 12") and the integer to find ("11")`.


## Testing

Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Binary Search.
In order to keep things simple, we split up the testing as follows:

- Binary Search Valid Tests
- Binary Search Invalid Tests

### Binary Search Valid Tests

| Description | List Input | Target Integer Input | Output |
| ----------- | ---------- | -------------------- | ------ |
| Sample Input: First True | "1, 3, 5, 7" | "1" | "true" |
| Sample Input: Last True | "1, 3, 5, 7" | "7" | "true" |
| Sample Input: Middle True | "1, 3, 5, 7" | "5" | "true" |
| Sample Input: One True | "5" | "5" | "true" |
| Sample Input: One False | "5" | "7" | "false" |
| Sample Input: Many False | "1, 3, 5, 6" | "7" | "false" |
| Sample Input: Middle True | "1, 2, 3, 4, 5, 6, 7" | "3" | "true" |

### Binary Search Invalid Tests

| Description | List Input | Target Integer Input |
| ----------- | ---------- | -------------------- |
| No Input |  |  |
| Missing Input: Target | "1, 2, 3, 4" |  |
| Missing Input: List | "" | "5" |
| Out Of Order Input | "3, 5, 1, 2" | "3" |

All of these tests should output the following:

```
Usage: please provide a list of sorted integers ("1, 4, 5, 11, 12") and the integer to find ("11")
```


## Articles

There are 20 articles:

- [Binary Search in Algol68](https://sampleprograms.io/projects/binary-search/algol68)
- [Binary Search in Awk](https://sampleprograms.io/projects/binary-search/awk)
- [Binary Search in Beef](https://sampleprograms.io/projects/binary-search/beef)
- [Binary Search in C](https://sampleprograms.io/projects/binary-search/c)
- [Binary Search in C#](https://sampleprograms.io/projects/binary-search/c-sharp)
- [Binary Search in C++](https://sampleprograms.io/projects/binary-search/c-plus-plus)
- [Binary Search in Commodore Basic](https://sampleprograms.io/projects/binary-search/commodore-basic)
- [Binary Search in Euphoria](https://sampleprograms.io/projects/binary-search/euphoria)
- [Binary Search in Go](https://sampleprograms.io/projects/binary-search/go)
- [Binary Search in Java](https://sampleprograms.io/projects/binary-search/java)
- [Binary Search in Javascript](https://sampleprograms.io/projects/binary-search/javascript)
- [Binary Search in Kotlin](https://sampleprograms.io/projects/binary-search/kotlin)
- [Binary Search in Mathematica](https://sampleprograms.io/projects/binary-search/mathematica)
- [Binary Search in Pascal](https://sampleprograms.io/projects/binary-search/pascal)
- [Binary Search in Php](https://sampleprograms.io/projects/binary-search/php)
- [Binary Search in Powershell](https://sampleprograms.io/projects/binary-search/powershell)
- [Binary Search in Python](https://sampleprograms.io/projects/binary-search/python)
- [Binary Search in Ruby](https://sampleprograms.io/projects/binary-search/ruby)
- [Binary Search in Rust](https://sampleprograms.io/projects/binary-search/rust)
- [Binary Search in Typescript](https://sampleprograms.io/projects/binary-search/typescript)

***

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Base64 Encode Decode)](https://sampleprograms.io/projects/base64-encode-decode)

</div>

<div id="next" markdown="1">

[Next Project (Bubble Sort) -->](https://sampleprograms.io/projects/bubble-sort)

</div>

</nav>