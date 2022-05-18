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

Every project in the Sample Programs repo should be tested. In this section, we specify the set of tests specific to Maximum Subarray. To keep things simple, we split up testing into two subsets: valid and invalid. Valid tests refer to tests that occur under correct input conditions. Invalid tests refer to tests that occur on bad input (e.g., letters instead of numbers).

### Valid Tests

No 'Valid Tests' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

### Invalid Tests

No 'Invalid Tests' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## Articles

- [Maximum Subarray in Python](https://sampleprograms.io/projects/maximum-subarray/python)