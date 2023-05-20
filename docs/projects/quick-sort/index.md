---
title: Quick Sort in Every Language 
layout: default
date: 2018-11-29
last-modified: 2020-05-02
featured-image: quick-sort-in-every-language.jpg
tags: [quick-sort]
authors:
  - auroq

---

Welcome to the Quick Sort page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

## Description

Quick sort is an algorithm that works by dividing a list into smaller lists.
It recursively partially sorts and divides each sublist into further lists until it
reaches the base case of a list that is either empty or contains only a single element, because
those cases are by definition already sorted. After that it concatenates all of the sublists
together into a single sorted list.

Step by step the process is:

1. Pick an element. This element is called the pivot.
2. Move all elements in the list that are greater than the pivot after the pivot
3. Move all elements that are less than the pivot before the pivot.
4. Recursively repeat steps 1-4 until a list of size 0-1 is found.
5. Concatinate all the sublists into a single sorted list.

### Performance

The performance of sorting algorithms is generally defined in "Big O notation".
If you are not familiar with such notations, please refer to the relevant
article by [Rob Bell][1] or the [Wikipedia][2] entry listed in further readings below.

| Cases        | Big O Notatation |
| ------------ | ---------------- |
| Best case    | O(n log n)       |
| Average case | O(n log n)       |
| Worst case   | O(n<sup>2</sup>) |

As the name implies, quicksort is a rather efficient algorithm; however,
its performance can be affected by the pivot that is selected. For example,
always selecting the last element in the list (or sublist) can make the algorithm easy
to write, but on a sorted list that will lead to an efficiency of O(n<sup>2</sup>)
(the worst case).

### Examples

The example below was taken from [Wikipedia's article about Quick sort][3].
The __bolded__ elements are the pivots. In this example, the last element in each list/sublist
was chosen to be the pivot, but that is not necesary. (See the section about performance above.)
Each row shows the comparison of an element to the pivot (steps 2-3).
The arrows convey splitting each list into sublists and then bringing them back together (steps
4-5).

![Quick sort example](https://upload.wikimedia.org/wikipedia/commons/a/af/Quicksort-diagram.svg)

[1]: https://robbell.io/2009/06/a-beginners-guide-to-big-o-notation
[2]: https://en.wikipedia.org/wiki/Big_O_notation
[3]: https://en.wikipedia.org/wiki/Quicksort


## Requirements

Write a sample program that takes a list of numbers in the format "4, 5, 3, 1, 2".
It should then sort the numbers and output them:

```console
$ ./quick-sort.lang "4, 5, 3, 1, 2"
1, 2, 3, 4, 5
```

The solution should handle duplicate elements

```console
$ ./quick-sort.lang "4, 5, 3, 1, 4, 2"
1, 2, 3, 4, 4, 5
```

In addition, there should be some error handling for situations where the user
doesn't supply correct input.


## Testing

Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Quick Sort.
In order to keep things simple, we split up the testing as follows:

- Quick Sort Valid Tests
- Quick Sort Invalid Tests

### Quick Sort Valid Tests

| Description | Input | Output |
| ----------- | ----- | ------ |
| Sample Input | "4, 5, 3, 1, 2" | "1, 2, 3, 4, 5" |
| Sample Input: With Duplicate | "4, 5, 3, 1, 4, 2" | "1, 2, 3, 4, 4, 5" |
| Sample Input: Already Sorted | "1, 2, 3, 4, 5" | "1, 2, 3, 4, 5" |
| Sample Input: Reverse Sorted | "9, 8, 7, 6, 5, 4, 3, 2, 1" | "1, 2, 3, 4, 5, 6, 7, 8, 9" |

### Quick Sort Invalid Tests

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

- [Quick Sort in Algol68](https://sampleprograms.io/projects/quick-sort/algol68)
- [Quick Sort in Bash](https://sampleprograms.io/projects/quick-sort/bash)
- [Quick Sort in C](https://sampleprograms.io/projects/quick-sort/c)
- [Quick Sort in C#](https://sampleprograms.io/projects/quick-sort/c-sharp)
- [Quick Sort in C++](https://sampleprograms.io/projects/quick-sort/c-plus-plus)
- [Quick Sort in Dart](https://sampleprograms.io/projects/quick-sort/dart)
- [Quick Sort in Euphoria](https://sampleprograms.io/projects/quick-sort/euphoria)
- [Quick Sort in Go](https://sampleprograms.io/projects/quick-sort/go)
- [Quick Sort in Haskell](https://sampleprograms.io/projects/quick-sort/haskell)
- [Quick Sort in Java](https://sampleprograms.io/projects/quick-sort/java)
- [Quick Sort in Javascript](https://sampleprograms.io/projects/quick-sort/javascript)
- [Quick Sort in Kotlin](https://sampleprograms.io/projects/quick-sort/kotlin)
- [Quick Sort in Lisp](https://sampleprograms.io/projects/quick-sort/lisp)
- [Quick Sort in Mathematica](https://sampleprograms.io/projects/quick-sort/mathematica)
- [Quick Sort in Objective C](https://sampleprograms.io/projects/quick-sort/objective-c)
- [Quick Sort in Php](https://sampleprograms.io/projects/quick-sort/php)
- [Quick Sort in Python](https://sampleprograms.io/projects/quick-sort/python)
- [Quick Sort in Rust](https://sampleprograms.io/projects/quick-sort/rust)
- [Quick Sort in Scala](https://sampleprograms.io/projects/quick-sort/scala)

***

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Prime Number)](https://sampleprograms.io/projects/prime-number)

</div>

<div id="next" markdown="1">

[Next Project (Quine) -->](https://sampleprograms.io/projects/quine)

</div>

</nav>