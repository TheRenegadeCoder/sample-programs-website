---

title: Binary Search
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Binary Search page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

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
./binary-search.lang "1, 4, 5, 11, 12" "4"
```

If successful, the script should return `true`. Otherwise, the script should return `false`. 
If any user input errors occur, the script should output the following usage message:
`Usage: please provide a list of sorted integers ("1, 4, 5, 11, 12") and the integer to find ("11")`.


## Testing

| Description | List Input | Target Integer Input | Output |
|-------------|------------|---------------|--------|
| No Input    |            |               | error\* |
| Missing Input: List | `1, 2, 3, 4` | | error\* |
| Missing Input: Target | `""` | `5` | error\* |
| Out of Order Input | `3, 5, 1, 2` | `3` | error\* |
| Sample Input: First True | `1, 3, 5, 7` | `1` | `true` |
| Sample Input: Last True | `1, 3, 5, 7` | `7` | `true` |
| Sample Input: Middle True | `1, 3, 5, 7` | `5` | `true` |
| Sample Input: One True | `5` | `5` | `true` |
| Sample Input: One False | `5` | `7` | `false` |
| Sample Input: Many False | `1, 3, 5, 6` | `7` | `false` |

\*The error string to print: `Usage: please provide a list of sorted integers ("1, 4, 5, 11, 12") and the integer to find ("11")`


## Articles

- [Binary Search in C++](https://sampleprograms.io/projects/binary-search/c-plus-plus)
- [Binary Search in Go](https://sampleprograms.io/projects/binary-search/go)
- [Binary Search in Javascript](https://sampleprograms.io/projects/binary-search/javascript)
- [Binary Search in Python](https://sampleprograms.io/projects/binary-search/python)
- [Binary Search in Rust](https://sampleprograms.io/projects/binary-search/rust)