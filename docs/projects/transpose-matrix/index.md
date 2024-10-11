---
date: 2022-05-13
featured-image: transpose-matrix-in-every-language.jpg
last-modified: 2024-10-11
layout: default
tags:
- transpose-matrix
title: Transpose Matrix
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/projects/transpose-matrix/description.md
- sources/projects/transpose-matrix/requirements.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the Transpose Matrix page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

This article was written by:

- Jeremy Grifski
- rzuckerm

## Description

<style>
    .matrix {
        text-align: center;
    }

    .empty {
        background-color: transparent;
    }

    .right {
        text-align: right;
    }
</style>

In linear algebra, the transpose of a matrix is an operator which flips a matrix over its diagonal; 
that is, it switches the row and column indices of the matrix A by producing another matrix, often 
denoted by A<sup>T</sup>. For example, the following matrix could be the matrix A:

<table class="matrix">
    <tr>
        <th class="empty;">&nbsp;</th>
        <th>column 1</th>
        <th>column 2</th>
        <th>column 3</th>
    </tr>
    <tr>
        <th class="right">row 1</th>
        <td>1</td>
        <td>2</td>
        <td>3</td>
    </tr>
    <tr>
        <th class="right">row 2</th>
        <td>4</td>
        <td>5</td>
        <td>6</td>
    </tr>
    <tr>
        <th class="right">row 3</th>
        <td>7</td>
        <td>8</td>
        <td>9</td>
    </tr>
</table>

Once transposed, A becomes the following matrix, A<sup>T</sup>:

<table class="matrix">
    <tr>
        <th class="empty">&nbsp;</th>
        <th>column 1</th>
        <th>column 2</th>
        <th >column 3</th>
    </tr>
    <tr>
        <th class="right">row 1</th>
        <td>1</td>
        <td>4</td>
        <td>7</td>
    </tr>
    <tr>
        <th class="right">row 2</th>
        <td>2</td>
        <td>5</td>
        <td>8</td>
    </tr>
    <tr>
        <th class="right">row 3</th>
        <td>3</td>
        <td>6</td>
        <td>9</td>
    </tr>
</table>

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

There are 11 articles:

- [Transpose Matrix in Algol68](https://sampleprograms.io/projects/transpose-matrix/algol68)
- [Transpose Matrix in Beef](https://sampleprograms.io/projects/transpose-matrix/beef)
- [Transpose Matrix in Commodore Basic](https://sampleprograms.io/projects/transpose-matrix/commodore-basic)
- [Transpose Matrix in Euphoria](https://sampleprograms.io/projects/transpose-matrix/euphoria)
- [Transpose Matrix in Go](https://sampleprograms.io/projects/transpose-matrix/go)
- [Transpose Matrix in Javascript](https://sampleprograms.io/projects/transpose-matrix/javascript)
- [Transpose Matrix in Mathematica](https://sampleprograms.io/projects/transpose-matrix/mathematica)
- [Transpose Matrix in Php](https://sampleprograms.io/projects/transpose-matrix/php)
- [Transpose Matrix in Python](https://sampleprograms.io/projects/transpose-matrix/python)
- [Transpose Matrix in Rust](https://sampleprograms.io/projects/transpose-matrix/rust)
- [Transpose Matrix in Typescript](https://sampleprograms.io/projects/transpose-matrix/typescript)

***

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Sleep Sort)](https://sampleprograms.io/projects/sleep-sort)

</div>

<div id="next" markdown="1">

[Next Project (Baklava) -->](https://sampleprograms.io/projects/baklava)

</div>

</nav>