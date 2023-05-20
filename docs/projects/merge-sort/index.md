---
title: Merge Sort in Every Language 
layout: default
date: 2018-11-29
last-modified: 2020-05-02
featured-image: merge-sort-in-every-language.jpg
tags: [merge-sort]
authors:
  - auroq

---

Welcome to the Merge Sort page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

## Description

Merge sort is an algorithm that works by dividing a list into smaller lists.
It continues dividing until each list only has a single element in it
because lists of a single element are by definition already sorted.
It then merges each sublist in a sorted fashion until they all become a single sorted list.

Step by step the process is:

1. Divide the sorted list into lists of 1 element.
2. Continually merge the lists together until they become a single list. Do the merge as follows:
    * Compare the smallest items in each of the two lists to be merged.
    * Move the smaller of the two to the new merged list
    * Repeat until there are no unmerged items


### Performance

The performance of sorting algorithms is generally defined in "Big O notation".
If you are not familiar with such notations, please refer to the relevant
article by [Rob Bell][1] or the [Wikipedia][2] entry listed in further readings below.

| Cases        | Big O Notatation |
| ------------ | ---------------- |
| Best case    | O(n log n)       |
| Average case | O(n log n)       |
| Worst case   | O(n log n)       |

### Examples

The examples below were taken from [Wikipedia's article about Merge sort][3].

![Merge sort example image](https://upload.wikimedia.org/wikipedia/commons/e/e6/Merge_sort_algorithm_diagram.svg)

![Merge sort example gif](https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif)

[1]: https://robbell.io/2009/06/a-beginners-guide-to-big-o-notation
[2]: https://en.wikipedia.org/wiki/Big_O_notation
[3]: https://en.wikipedia.org/wiki/Merge_sort


## Requirements

Write a sample program that takes a list of numbers in the format "4, 5, 3, 1, 2".
It should then sort the numbers and output them:

```console
$ ./merge-sort.lang "4, 5, 3, 1, 2"
1, 2, 3, 4, 5
```

The solution should handle duplicate elements

```console
$ ./merge-sort.lang "4, 5, 3, 1, 4, 2"
1, 2, 3, 4, 4, 5
```

In addition, there should be some error handling for situations where the user
doesn't supply correct input.


## Testing

Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Merge Sort.
In order to keep things simple, we split up the testing as follows:

- Merge Sort Valid Tests
- Merge Sort Invalid Tests

### Merge Sort Valid Tests

| Description | Input | Output |
| ----------- | ----- | ------ |
| Sample Input | "4, 5, 3, 1, 2" | "1, 2, 3, 4, 5" |
| Sample Input: With Duplicate | "4, 5, 3, 1, 4, 2" | "1, 2, 3, 4, 4, 5" |
| Sample Input: Already Sorted | "1, 2, 3, 4, 5" | "1, 2, 3, 4, 5" |
| Sample Input: Reverse Sorted | "9, 8, 7, 6, 5, 4, 3, 2, 1" | "1, 2, 3, 4, 5, 6, 7, 8, 9" |

### Merge Sort Invalid Tests

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

- [Merge Sort in Algol68](https://sampleprograms.io/projects/merge-sort/algol68)
- [Merge Sort in C](https://sampleprograms.io/projects/merge-sort/c)
- [Merge Sort in C#](https://sampleprograms.io/projects/merge-sort/c-sharp)
- [Merge Sort in C++](https://sampleprograms.io/projects/merge-sort/c-plus-plus)
- [Merge Sort in Euphoria](https://sampleprograms.io/projects/merge-sort/euphoria)
- [Merge Sort in Go](https://sampleprograms.io/projects/merge-sort/go)
- [Merge Sort in Groovy](https://sampleprograms.io/projects/merge-sort/groovy)
- [Merge Sort in Haskell](https://sampleprograms.io/projects/merge-sort/haskell)
- [Merge Sort in Java](https://sampleprograms.io/projects/merge-sort/java)
- [Merge Sort in Javascript](https://sampleprograms.io/projects/merge-sort/javascript)
- [Merge Sort in Kotlin](https://sampleprograms.io/projects/merge-sort/kotlin)
- [Merge Sort in Mathematica](https://sampleprograms.io/projects/merge-sort/mathematica)
- [Merge Sort in Matlab](https://sampleprograms.io/projects/merge-sort/matlab)
- [Merge Sort in Objective C](https://sampleprograms.io/projects/merge-sort/objective-c)
- [Merge Sort in Php](https://sampleprograms.io/projects/merge-sort/php)
- [Merge Sort in Python](https://sampleprograms.io/projects/merge-sort/python)
- [Merge Sort in Rust](https://sampleprograms.io/projects/merge-sort/rust)

***

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Maximum Subarray)](https://sampleprograms.io/projects/maximum-subarray)

</div>

<div id="next" markdown="1">

[Next Project (Minimum Spanning Tree) -->](https://sampleprograms.io/projects/minimum-spanning-tree)

</div>

</nav>