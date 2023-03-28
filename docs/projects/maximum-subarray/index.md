---

title: Maximum Subarray in Every Language
layout: default
date: 2020-10-06
last-modified: 2020-10-14
featured-image:
tags: [maximum-subarray]
authors:
  - Senpai1199

---

Welcome to the Maximum Subarray page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

## Description

Given an array, the maximum subarray is the subarray which gives the maximum sum possible in the array.
Kadane's algorithm is a popular algorithm used to find out this maximum sum value.

Note: A subarray is any continuous portion of an array.

For example:

Given array: `[-1, -2, 1, 2, 3, 4, 5, 23]`

Max sum value of a subarray: `38`

Explanation: The subarray `[1, 2, 3, 4, 5, 23]` gives the max sum value. `(1 + 2 + 3 + 4 + 5 + 23 = 38)`


## Requirements

You must write an executable program that accepts a string of comma separated integers on `standard input` via the sys args, and outputs the maximum subarray sum value to `standard output`.

Note that the Kadane's algorithm assumes that there is atleast 1 negative integer in the array.
If there is no negative integer, then the max subarray sum value is the sum of all the elements of the array.

Also note that if the input string is empty, then the output is "Usage: Please provide a list of at least two integers to sort in the format: '1, 2, 3, 4, 5'".


## Testing

Some tests for your program are:

| Description                                                  | Input                     | Output                                                                                       |
| :----------------------------------------------------------- | :------------------------ | :------------------------------------------------------------------------------------------- |
| No input                                                     |                           | Usage: Please provide a list of integers in the format: "1, 2, 3, 4, 5" |
| Empty input                                                  | " "                       | Usage: Please provide a list of integers in the format: "1, 2, 3, 4, 5" |
| Sample Input: Array with size 1                              | 1                         | 1                                                                                            |
| Sample Input: Array with no negative integers                | "1, 2, 3"                 | 6                                                                                            |
| Sample Input: Array with all negative integers               | "-1, -2, -3"              | -1                                                                                           |
| Sample Input: Array with both positive and negative integers | "-2, -1, 3, 4, 5"         | 12                                                                                           |
| Sample Input: Array with both positive and negative integers | "-1, -4, 2, 3, -3, -4, 9" | 9                                                                                            |
| Sample Input: Array with both positive and negative integers | "-1, -4, 2, 9, -3, -4, 9" | 13                                                                                           |


## Articles

- [Maximum Subarray in Algol68](https://sampleprograms.io/projects/maximum-subarray/algol68)
- [Maximum Subarray in Euphoria](https://sampleprograms.io/projects/maximum-subarray/euphoria)
- [Maximum Subarray in Mathematica](https://sampleprograms.io/projects/maximum-subarray/mathematica)
- [Maximum Subarray in Php](https://sampleprograms.io/projects/maximum-subarray/php)
- [Maximum Subarray in Python](https://sampleprograms.io/projects/maximum-subarray/python)

---

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Maximum Array Rotation)](https://sampleprograms.io/projects/maximum-array-rotation)

</div>

<div id="next" markdown="1">

[Next Project (Merge Sort) -->](https://sampleprograms.io/projects/merge-sort)

</div>

</nav>