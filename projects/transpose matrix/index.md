---
title: Transpose matrix in Every Language
layout: default
date: 2020-10-08
last-modified: 2020-10-08
featured-image:
tags: [transpose-matrix]
authors: 
  - DedAvocado
---

In this article, we'll demonstrate how to find Transpose of a Matrix, its requirements, and how
to test it.

## Description

In linear algebra, the transpose of a matrix is an operator which flips a matrix over its diagonal; that is, it switches the row and column indices of the matrix A by producing another matrix, often denoted by Aᵀ. The transpose of a matrix was introduced in 1858 by the British mathematician Arthur Cayley.

The solution can be generated using nested loops and exchanging the indexes of the matrix.

## Requirements
Input:

| 1 | 2 | 3 |
| - |:-:| -:|
| 4 | 5 | 6 |
| 7 | 8 | 9 |

The following is the expected output:
| 1 | 4 | 7 |
| - |:-:| -:|
| 2 | 5 | 8 |
| 3 | 6 | 9 |

1.  The first matrix is from the given input.
2.  The second  matrix is the desired output i.e, the transpose of the matrix.

To execute the program :
```transpose.lang 3 3 "1, 2, 3, 4, 5, 6, 7, 8, 9"``` </br>
Here the first two input numbers indicate the size of the matrix and the next input is the list of numbers to be included in the matrix.

## Testing

Verify that the actual output matches the expected output (see [requirements][1])

| Description | size1 | size2 | integers | Output |
| - |:-:|:-:|:-:| -:|
| No input |   |   |   | error:please enter the dimension of the matrix and the serialized matrix |
| Missing input: Size |   |   | ```1, 2, 3, 4, 5, 6``` | error:please enter the dimension of the matrix |
| Missing input: integers | 3 | 3 |   | error:please enter the serialized matrix |
| Sample input | 3 | 2 | ```1, 2, 3, 4, 5, 6``` | ```1, 4, 2, 5, 3, 6``` |

## Articles

{% include article_list.md collection=site.categories.transpose-matrix %}

[1]: #requirements
