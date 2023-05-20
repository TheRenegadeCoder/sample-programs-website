---
title: Transpose Matrix in Every Language
layout: default
date: 2020-10-08
last-modified: 2021-10-06
featured-image: transpose-matrix-in-every-language.jpg
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

Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Transpose Matrix.
In order to keep things simple, we split up the testing as follows:

- Transpose Matrix Valid Tests
- Transpose Matrix Invalid Tests

### Transpose Matrix Valid Tests

| Description | Cols | Rows | Matrix | Output |
| ----------- | ---- | ---- | ------ | ------ |
| Sample Input: Routine | "3" | "2" | "1, 2, 3, 4, 5, 6" | "1, 4, 2, 5, 3, 6" |

### Transpose Matrix Invalid Tests

| Description | Cols | Rows | Matrix |
| ----------- | ---- | ---- | ------ |
| No Input |  |  |  |
| Missing Input: No Columns Or Rows | "" | "" | "1, 2, 3, 4, 5, 6" |
| Missing Input: No Matrix | "3" | "3" | "" |

All of these tests should output the following:

```
Usage: please enter the dimension of the matrix and the serialized matrix
```


## Articles

- [Transpose Matrix in Algol68](https://sampleprograms.io/projects/transpose-matrix/algol68)
- [Transpose Matrix in Euphoria](https://sampleprograms.io/projects/transpose-matrix/euphoria)
- [Transpose Matrix in Mathematica](https://sampleprograms.io/projects/transpose-matrix/mathematica)
- [Transpose Matrix in Php](https://sampleprograms.io/projects/transpose-matrix/php)
- [Transpose Matrix in Python](https://sampleprograms.io/projects/transpose-matrix/python)
- [Transpose Matrix in Rust](https://sampleprograms.io/projects/transpose-matrix/rust)

***

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Sleep Sort)](https://sampleprograms.io/projects/sleep-sort)

</div>

<div id="next" markdown="1">

[Next Project (Baklava) -->](https://sampleprograms.io/projects/baklava)

</div>

</nav>