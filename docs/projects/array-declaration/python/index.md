---
authors:
- Faiz Nurullah 
date: 2023-29-09
featured-image: array-declaration-python.png
last-modified: 2023-29-09
layout: default
tags:
- python
- array
title: - Array Declaration
---

Welcome to the [Array Declaration](https://sampleprograms.io/projects/array-declaration) page! Here you will learn how to declare arrays in Python programming until the program runs.

## Declaring an Array

In Python we can declare arrays using two ways. Firstly by using lists and secondly by using the Python library.

## Defines Array Contents

The first way is to declare an array variable while defining the contents of the array. This method is used if we already know the value that needs to be given.

```python

var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr)

// Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

```

In the variable "var_arr" we store elements of integer type with a length of 10 elements and the address of each array element (index) is index 0 to 9.

## Accessing Array Elements

Accessing array elements in Python is no different from accessing elements in a list. This is because we use lists as "another form" of arrays. You can use the indexing method to access array elements.

```python

var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr[0])

// Output: 9

```

In the example above, we take the 0th index in the variable "var_arr" which has a value of 9. So, the resulting output is 9.