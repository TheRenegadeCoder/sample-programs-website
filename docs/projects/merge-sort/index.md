---

title: Merge Sort in Every Language 
layout: default
date: 2018-11-29
last-modified: 2020-05-02
featured-image:
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
article by Rob Bell or the wikipedia entry listed in further readings below.

| | |
|---|---|
| Best case | O(n log n) |
| Average case | O(n log n) |
| Worst case | O(n log n) |

### Examples

The examples below were taken from [Wikipedia's article about Merge sort][1].

![Merge sort example image](https://upload.wikimedia.org/wikipedia/commons/e/e6/Merge_sort_algorithm_diagram.svg)

![Merge sort example gif](https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif)


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

Every project in the Sample Programs repo should be tested. In this section, we specify the set of tests specific to Projects. To keep things simple, we split up testing into two subsets: valid and invalid. Valid tests refer to tests that occur under correct input conditions. Invalid tests refer to tests that occur on bad input (e.g., letters instead of numbers).

### Valid Tests

No 'Valid Tests' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

### Invalid Tests

No 'Invalid Tests' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## Articles

- [Merge Sort in C](https://sampleprograms.io/projects/merge-sort/c)
- [Merge Sort in C#](https://sampleprograms.io/projects/merge-sort/c-sharp)
- [Merge Sort in C++](https://sampleprograms.io/projects/merge-sort/c-plus-plus)
- [Merge Sort in Go](https://sampleprograms.io/projects/merge-sort/go)
- [Merge Sort in Groovy](https://sampleprograms.io/projects/merge-sort/groovy)
- [Merge Sort in Haskell](https://sampleprograms.io/projects/merge-sort/haskell)
- [Merge Sort in Java](https://sampleprograms.io/projects/merge-sort/java)
- [Merge Sort in Javascript](https://sampleprograms.io/projects/merge-sort/javascript)
- [Merge Sort in Kotlin](https://sampleprograms.io/projects/merge-sort/kotlin)
- [Merge Sort in Matlab](https://sampleprograms.io/projects/merge-sort/matlab)
- [Merge Sort in Objective C](https://sampleprograms.io/projects/merge-sort/objective-c)
- [Merge Sort in Php](https://sampleprograms.io/projects/merge-sort/php)
- [Merge Sort in Python](https://sampleprograms.io/projects/merge-sort/python)
- [Merge Sort in Rust](https://sampleprograms.io/projects/merge-sort/rust)