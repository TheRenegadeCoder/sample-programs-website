---
date: 2018-12-02
featured-image: selection-sort-in-every-language.jpg
last-modified: 2024-10-13
layout: default
tags:
- selection-sort
title: Selection Sort
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/projects/selection-sort/description.md
- sources/projects/selection-sort/requirements.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the Selection Sort page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

This article was written by:

- Jeremy Grifski
- Parker Johansen
- Ron Zuckerman

## Description

Selection sort is an algorithm that operates on two lists, one of sorted elements and one of unsorted.
With each pass, the algorithm finds the smallest item in the unsorted list and moves it
to the front of the sorted list. At the beginning the sorted list is empty, and the algorithm completes
when the unsorted list is empty (meaning that all elements have been moved to the sorted list).

There is also a variant that uses a single list and moves the elements in place. In this variant,
the sorted elements are just placed at the front of the list rather than in a separate list, and
the algorithm starts each pass with the index of the first unsorted element in the list.

### Performance

The performance of sorting algorithms is generally defined in "Big O notation".
If you are not familiar with such notations, please refer to the relevant
article by [Rob Bell][1] or the [Wikipedia][2] entry listed in further readings below.

| Cases        | Big O Notatation |
| ------------ | ---------------- |
| Best case    | O(n<sup>2</sup>) |
| Average case | O(n<sup>2</sup>) |
| Worst case   | O(n<sup>2</sup>) |

Selection sort always performs at O(n<sup>2</sup>). This is because the algorithm's
loops do not depend on the values of the items in the list. That means that even if
the list is already sorted, the full sorting process will still be performed.

### Examples: Two lists

In the examples below, each row is a single pass through all elements in the unsorted list.
The element in __bold__ is the one that will be moved to the sorted list after the pass.

#### "4, 5, 3, 1, 2"

| Sorted List | Unsorted List                 |
|-------------|-------------------------------|
|             |   4     5     3   __1__   2   |
| 1           |   4     5     3   __2__       |
| 1 2         |   4     5   __3__             |
| 1 2 3       | __4__   5                     |
| 1 2 3 4     | __5__                         |
| 1 2 3 4 5   |                               |

#### "3, 5, 4, 1, 2"

| Sorted List | Unsorted List                 |
|-------------|-------------------------------|
|             |   3     5     4   __1__   2   |
| 1           |   3     5     4   __2__       |
| 1 2         | __3__   5     4               |
| 1 2 3       |   5   __4__                   |
| 1 2 3 4     | __5__                         |
| 1 2 3 4 5   |                               |


### Examples: Single list

In the examples below, each row is a single pass through all elements in the unsorted list.
The element in __bold__ is the one that will be moved to the end of the sorted section after the pass.

#### "4, 5, 3, 1, 2"

-   4     5     3   __1__   2   
-   1     4     5     3   __2__ 
-   1     2     4     5   __3__ 
-   1     2     3   __4__   5   
-   1     2     3     4   __5__ 
-   1     2     3     4     5    

#### "3, 5, 4, 1, 2"

-   3     5     4   __1__   2   
-   1     3     5     4   __2__ 
-   1     2   __3__   5     4   
-   1     2     3     5   __4__ 
-   1     2     3     4   __5__ 
-   1     2     3     4     5    

[1]: https://robbell.io/2009/06/a-beginners-guide-to-big-o-notation
[2]: https://en.wikipedia.org/wiki/Big_O_notation


## Requirements

Write a sample program that takes a list of numbers in the format "4, 5, 3, 1, 2".
It should then sort the numbers and output them:

```console
$ ./selection-sort.lang "4, 5, 3, 1, 2"
1, 2, 3, 4, 5
```

The solution should handle duplicate elements

```console
$ ./selection-sort.lang "4, 5, 3, 1, 4, 2"
1, 2, 3, 4, 4, 5
```

In addition, there should be some error handling for situations where the user
doesn't supply correct input.


## Testing

Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Selection Sort.
In order to keep things simple, we split up the testing as follows:

- Selection Sort Valid Tests
- Selection Sort Invalid Tests

### Selection Sort Valid Tests

| Description | Input | Output |
| ----------- | ----- | ------ |
| Sample Input | "4, 5, 3, 1, 2" | "1, 2, 3, 4, 5" |
| Sample Input: With Duplicate | "4, 5, 3, 1, 4, 2" | "1, 2, 3, 4, 4, 5" |
| Sample Input: Already Sorted | "1, 2, 3, 4, 5" | "1, 2, 3, 4, 5" |
| Sample Input: Reverse Sorted | "9, 8, 7, 6, 5, 4, 3, 2, 1" | "1, 2, 3, 4, 5, 6, 7, 8, 9" |

### Selection Sort Invalid Tests

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input | "" |
| Invalid Input: Not A List | "1" |
| Invalid Input: Wrong Format | "4 5 3" |

All of these tests should output the following:

```
Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"
```


## Articles

There are 20 articles:

- [Selection Sort in Algol68](https://sampleprograms.io/projects/selection-sort/algol68)
- [Selection Sort in Bash](https://sampleprograms.io/projects/selection-sort/bash)
- [Selection Sort in Beef](https://sampleprograms.io/projects/selection-sort/beef)
- [Selection Sort in C](https://sampleprograms.io/projects/selection-sort/c)
- [Selection Sort in C#](https://sampleprograms.io/projects/selection-sort/c-sharp)
- [Selection Sort in C++](https://sampleprograms.io/projects/selection-sort/c-plus-plus)
- [Selection Sort in Commodore Basic](https://sampleprograms.io/projects/selection-sort/commodore-basic)
- [Selection Sort in Euphoria](https://sampleprograms.io/projects/selection-sort/euphoria)
- [Selection Sort in Go](https://sampleprograms.io/projects/selection-sort/go)
- [Selection Sort in Haskell](https://sampleprograms.io/projects/selection-sort/haskell)
- [Selection Sort in Java](https://sampleprograms.io/projects/selection-sort/java)
- [Selection Sort in Javascript](https://sampleprograms.io/projects/selection-sort/javascript)
- [Selection Sort in Julia](https://sampleprograms.io/projects/selection-sort/julia)
- [Selection Sort in Mathematica](https://sampleprograms.io/projects/selection-sort/mathematica)
- [Selection Sort in Octave](https://sampleprograms.io/projects/selection-sort/octave)
- [Selection Sort in Perl](https://sampleprograms.io/projects/selection-sort/perl)
- [Selection Sort in Php](https://sampleprograms.io/projects/selection-sort/php)
- [Selection Sort in Python](https://sampleprograms.io/projects/selection-sort/python)
- [Selection Sort in Rust](https://sampleprograms.io/projects/selection-sort/rust)
- [Selection Sort in Typescript](https://sampleprograms.io/projects/selection-sort/typescript)

***

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Rot13)](https://sampleprograms.io/projects/rot13)

</div>

<div id="next" markdown="1">

[Next Project (Sleep Sort) -->](https://sampleprograms.io/projects/sleep-sort)

</div>

</nav>