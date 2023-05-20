---
title: Bubble Sort in Every Language
layout: default
date: 2018-11-29
last-modified: 2022-05-18
featured-image: bubble-sort-in-every-language.jpg
tags: [bubble-sort]
authors:
  - auroq
  - the_renegade_coder

---

Welcome to the Bubble Sort page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

## Description

Bubble sort is a sorting algorithm that repeatedly cycles through a list of elements
and swaps adjacent elements if they are not in order. It works as follows:

1. Identify the next two adjacent elements in the list (start with the 1st and 2nd, then 2nd and 3rd, 3rd and 4th, and so on)
2. If the elements are not in order swap them.
3. If the end of this list has not been reached, repeat steps 1-3 again
4. If any elements were swapped in the above pass, repeat steps 1-4 again

### Performance

The performance of sorting algorithms is generally defined in "Big O notation".
If you are not familiar with such notations, please refer to the relevant
article by [Rob Bell][1] or the [Wikipedia][2] entry listed in further readings below.

| Cases        | Big O Notatation |
| ------------ | ---------------- |
| Best case    | O(n)             |
| Average case | O(n<sup>2</sup>) |
| Worst case   | O(n<sup>2</sup>) |

Bubble sort is generally not an efficient sorting algorithm; however, it does have one advantage.
When the elements are already sorted, bubble sort will only pass throught the list once; whereas,
most other algorithms will still perform their complete sorting process.

### Example: "4, 5, 3, 1, 2"

In the example below, "pass" refers to one pass through the list (steps 1-4 one time).
Each row in the pass shows a single comparison (steps 1-2 one time).
The elements in __bold__ on each line are the two being compared.
If the row is labeled "swap," a swap will occur after the comparison.

__Pass 1__
- __4__ __5__   3     1     2
-   4   __5__ __3__   1     2   -> swap
-   4     3   __5__ __1__   2   -> swap
-   4     3     1   __5__ __2__ -> swap

__Pass 2__
- __4__ __3__   1     2     5   -> swap
-  3    __4__ __1__   2     5   -> swap
-  3      1   __4__ __2__   5   -> swap
-  3      1     2   __4__ __5__

__Pass 3__
- __3__ __1__   2     4     5   -> swap
-  1    __3__ __2__   4     5   -> swap
-  1      2   __3__ __4__   5
-  1      2     3   __4__ __5__

__Pass 4__
- __1__ __2__   3     4     5
-  1    __2__ __3__   4     5
-  1      2   __3__ __4__   5
-  1      2     3   __4__ __5__

Note that although the elements were sorted at the end of pass 3,
the algorithm needs an additional pass without any swapping in order to know that the elements are sorted.

[1]: https://robbell.io/2009/06/a-beginners-guide-to-big-o-notation
[2]: https://en.wikipedia.org/wiki/Big_O_notation


## Requirements

Write a sample program that takes a list of numbers in the format "4, 5, 3, 1, 2".
It should then sort the numbers and output them:

```console
$ ./bubble-sort.lang "4, 5, 3, 1, 2"
1, 2, 3, 4, 5
```

The solution should handle duplicate elements

```console
$ ./bubble-sort.lang "4, 5, 3, 1, 4, 2"
1, 2, 3, 4, 4, 5
```

In addition, there should be some error handling for situations where the user
doesn't supply correct input.


## Testing

Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Bubble Sort.
In order to keep things simple, we split up the testing as follows:

- Bubble Sort Valid Tests
- Bubble Sort Invalid Tests

### Bubble Sort Valid Tests

| Description | Input | Output |
| ----------- | ----- | ------ |
| Sample Input | "4, 5, 3, 1, 2" | "1, 2, 3, 4, 5" |
| Sample Input: With Duplicate | "4, 5, 3, 1, 4, 2" | "1, 2, 3, 4, 4, 5" |
| Sample Input: Already Sorted | "1, 2, 3, 4, 5" | "1, 2, 3, 4, 5" |
| Sample Input: Reverse Sorted | "9, 8, 7, 6, 5, 4, 3, 2, 1" | "1, 2, 3, 4, 5, 6, 7, 8, 9" |

### Bubble Sort Invalid Tests

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

- [Bubble Sort in Algol68](https://sampleprograms.io/projects/bubble-sort/algol68)
- [Bubble Sort in Bash](https://sampleprograms.io/projects/bubble-sort/bash)
- [Bubble Sort in C](https://sampleprograms.io/projects/bubble-sort/c)
- [Bubble Sort in C#](https://sampleprograms.io/projects/bubble-sort/c-sharp)
- [Bubble Sort in C++](https://sampleprograms.io/projects/bubble-sort/c-plus-plus)
- [Bubble Sort in Clojure](https://sampleprograms.io/projects/bubble-sort/clojure)
- [Bubble Sort in Dart](https://sampleprograms.io/projects/bubble-sort/dart)
- [Bubble Sort in Elixir](https://sampleprograms.io/projects/bubble-sort/elixir)
- [Bubble Sort in Erlang](https://sampleprograms.io/projects/bubble-sort/erlang)
- [Bubble Sort in Euphoria](https://sampleprograms.io/projects/bubble-sort/euphoria)
- [Bubble Sort in Go](https://sampleprograms.io/projects/bubble-sort/go)
- [Bubble Sort in Haskell](https://sampleprograms.io/projects/bubble-sort/haskell)
- [Bubble Sort in Java](https://sampleprograms.io/projects/bubble-sort/java)
- [Bubble Sort in Javascript](https://sampleprograms.io/projects/bubble-sort/javascript)
- [Bubble Sort in Julia](https://sampleprograms.io/projects/bubble-sort/julia)
- [Bubble Sort in Kotlin](https://sampleprograms.io/projects/bubble-sort/kotlin)
- [Bubble Sort in Lua](https://sampleprograms.io/projects/bubble-sort/lua)
- [Bubble Sort in Mathematica](https://sampleprograms.io/projects/bubble-sort/mathematica)
- [Bubble Sort in Matlab](https://sampleprograms.io/projects/bubble-sort/matlab)
- [Bubble Sort in Perl](https://sampleprograms.io/projects/bubble-sort/perl)
- [Bubble Sort in Php](https://sampleprograms.io/projects/bubble-sort/php)
- [Bubble Sort in Python](https://sampleprograms.io/projects/bubble-sort/python)
- [Bubble Sort in Ruby](https://sampleprograms.io/projects/bubble-sort/ruby)
- [Bubble Sort in Rust](https://sampleprograms.io/projects/bubble-sort/rust)
- [Bubble Sort in Scala](https://sampleprograms.io/projects/bubble-sort/scala)
- [Bubble Sort in Visual Basic](https://sampleprograms.io/projects/bubble-sort/visual-basic)

***

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Binary Search)](https://sampleprograms.io/projects/binary-search)

</div>

<div id="next" markdown="1">

[Next Project (Capitalize) -->](https://sampleprograms.io/projects/capitalize)

</div>

</nav>