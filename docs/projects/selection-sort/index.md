---

title: Selection Sort in Every Language 
layout: default
date: 2018-11-29
last-modified: 2020-05-02
featured-image:
tags: [selection-sort]
authors:
  - auroq

---

Welcome to the Selection Sort page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

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
article by Rob Bell or the wikipedia entry listed in further readings below.

| | |
|---|---|
| Best case | O(n<sup>2</sup>) |
| Average case | O(n<sup>2</sup>) |
| Worst case | O(n<sup>2</sup>) |

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

Every project in the Sample Programs repo should be tested. In this section, we specify the set of tests specific to Projects. To keep things simple, we split up testing into two subsets: valid and invalid. Valid tests refer to tests that occur under correct input conditions. Invalid tests refer to tests that occur on bad input (e.g., letters instead of numbers).

### Valid Tests

No 'Valid Tests' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

### Invalid Tests

No 'Invalid Tests' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## Articles

- [Selection Sort in Bash](https://sampleprograms.io/projects/selection-sort/bash)
- [Selection Sort in C](https://sampleprograms.io/projects/selection-sort/c)
- [Selection Sort in C#](https://sampleprograms.io/projects/selection-sort/c-sharp)
- [Selection Sort in C++](https://sampleprograms.io/projects/selection-sort/c-plus-plus)
- [Selection Sort in Go](https://sampleprograms.io/projects/selection-sort/go)
- [Selection Sort in Haskell](https://sampleprograms.io/projects/selection-sort/haskell)
- [Selection Sort in Java](https://sampleprograms.io/projects/selection-sort/java)
- [Selection Sort in Javascript](https://sampleprograms.io/projects/selection-sort/javascript)
- [Selection Sort in Julia](https://sampleprograms.io/projects/selection-sort/julia)
- [Selection Sort in Matlab](https://sampleprograms.io/projects/selection-sort/matlab)
- [Selection Sort in Php](https://sampleprograms.io/projects/selection-sort/php)
- [Selection Sort in Python](https://sampleprograms.io/projects/selection-sort/python)