---

title: Insertion Sort in Every Language 
layout: default
date: 2018-12-16
last-modified: 2020-05-02
featured-image:
tags: [insertion-sort]
authors:
  - auroq

---

Welcome to the Insertion Sort page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

## Description

Insertion sort is an algorithm that generally operates on a single list in place.
It tracks a pointer that iterates through the list a single time, takes each
item and inserts it sorted at the beginning of the list. At any given point
all elements, from the beginning of the list up through the pointer, are in order.
Once the pointer has iterated through the entire list, all elements have been inserted
in order at the front of the list, and the list is now fully sorted.

### Performance

The performance of sorting algorithms is generally defined in "Big O notation".
If you are not familiar with such notations, please refer to the relevant
article by Rob Bell or the wikipedia entry listed in further readings below.

| | |
|---|---|
| Best case | O(n) |
| Average case | O(n<sup>2</sup>) |
| Worst case | O(n<sup>2</sup>) |

Although the main pointer of insertion sort only iterates through the list once
it must also iterate through the existing sorted items at the beginning of the list
every time an element is inserted. Thus the average case is O(n<sup>2</sup>), but so
is the worst case.


### Examples

In the examples below, each row inserts the element from the main pointer 
into the front of the list and moves the main pointer to the next element.
The element in __bold__ is the main pointer.

#### "4, 5, 3, 1, 2"

- __4__   5     3     1     2   
-   4   __5__   3     1     2   
-   4     5   __3__   1     2   
-   3     4     5   __1__   2   
-   1     3     4     5   __2__ 
-   1     2     3     4     5    

#### "3, 5, 4, 1, 2"

- __3__   5     4     1     2   
-   3   __5__   4     1     2   
-   3     5   __4__   1     2   
-   3     4     5   __1__   2   
-   1     3     4     5   __2__ 
-   1     2     3     4     5    


## Requirements

Write a sample program that takes a list of numbers in the format "4, 5, 3, 1, 2".
It should then sort the numbers and output them:

```console
$ ./insertion-sort.lang "4, 5, 3, 1, 2"
1, 2, 3, 4, 5
```

The solution should handle duplicate elements

```console
$ ./insertion-sort.lang "4, 5, 3, 1, 4, 2"
1, 2, 3, 4, 4, 5
```

In addition, there should be some error handling for situations where the user
doesn't supply correct input.


## Testing

The following table contains various test cases that you can use to
verify the correctness of your solution:

| Description                  | Input | Output |
|------------------------------|-------|--------|
| No Input                     |       | Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5" |
| Empty Input                  | ""    | Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5" |
| Invalid Input: Not a list    | 1     | Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5" |
| Invalid Input: Wrong Format  | 4 5 3 | Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5" |
| Sample Input                 | 4, 5, 3, 1, 2             | 1, 2, 3, 4, 5             |
| Sample Input: With Duplicate | 4, 5, 3, 1, 4, 2          | 1, 2, 3, 4, 4, 5          |
| Sample Input: Already Sorted | 1, 2, 3, 4, 5             | 1, 2, 3, 4, 5             |
| Sample Input: Reverse Sorted | 9, 8, 7, 6, 5, 4, 3, 2, 1 | 1, 2, 3, 4, 5, 6, 7, 8, 9 |


## Articles

- [Insertion Sort in C](https://sampleprograms.io/projects/insertion-sort/c)
- [Insertion Sort in C#](https://sampleprograms.io/projects/insertion-sort/c-sharp)
- [Insertion Sort in C++](https://sampleprograms.io/projects/insertion-sort/c-plus-plus)
- [Insertion Sort in Go](https://sampleprograms.io/projects/insertion-sort/go)
- [Insertion Sort in Haskell](https://sampleprograms.io/projects/insertion-sort/haskell)
- [Insertion Sort in Java](https://sampleprograms.io/projects/insertion-sort/java)
- [Insertion Sort in Javascript](https://sampleprograms.io/projects/insertion-sort/javascript)
- [Insertion Sort in Matlab](https://sampleprograms.io/projects/insertion-sort/matlab)
- [Insertion Sort in Perl](https://sampleprograms.io/projects/insertion-sort/perl)
- [Insertion Sort in Php](https://sampleprograms.io/projects/insertion-sort/php)
- [Insertion Sort in Python](https://sampleprograms.io/projects/insertion-sort/python)
- [Insertion Sort in Rust](https://sampleprograms.io/projects/insertion-sort/rust)

---

- [Previous Project](https://sampleprograms.io/projects/hello-world)
- [Next Project](https://sampleprograms.io/projects/job-sequencing)