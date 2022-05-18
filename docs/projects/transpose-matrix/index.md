---

title: Transpose Matrix in Every Language
layout: default
date: 2020-10-08
last-modified: 2021-10-06
featured-image:
tags: [transpose-matrix]
authors: 
  - DedAvocado

---

Welcome to the Transpose Matrix page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

## Description

In linear algebra, the transpose of a matrix is an operator which flips a matrix over its diagonal; 
that is, it switches the row and column indices of the matrix A by producing another matrix, often 
denoted by A<sup>T</sup>. For example, the following matrix could be the matrix A:

| 1 | 2 | 3 |
| - |:-:| -:|
| 4 | 5 | 6 |
| 7 | 8 | 9 |

Once transposed, A becomes the following matrix, A<sup>T</sup>:

| 1 | 4 | 7 |
| - |:-:| -:|
| 2 | 5 | 8 |
| 3 | 6 | 9 |

The transpose of a matrix was introduced in 1858 by the British mathematician Arthur Cayley.


## Requirements

For the purposes of this project, we'll ask that you create a program which accepts
a matrix as a list of integers and the dimensions of that matrix in the following
format:

```
transpose-matrix.lang 3 3 "1, 2, 3, 4, 5, 6, 7, 8, 9"
```

Here, the first two input numbers indicate the column and row size of the matrix, respectively, and the 
next input is the list of numbers to be included in the matrix.


## Testing

Every project in the Sample Programs repo should be tested. In this section, we specify the set of tests specific to Transpose Matrix. To keep things simple, we split up testing into two subsets: valid and invalid. Valid tests refer to tests that occur under correct input conditions. Invalid tests refer to tests that occur on bad input (e.g., letters instead of numbers).

### Valid Tests

No 'Valid Tests' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

### Invalid Tests

No 'Invalid Tests' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## Articles

- [Transpose Matrix in Python](https://sampleprograms.io/projects/transpose-matrix/python)