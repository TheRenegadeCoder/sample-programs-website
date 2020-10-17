---
title: Jump Search in Every Language
layout: default
date: 2020-10-02
last-modified: 2020-10-02
featured-image: jump-search-python.png
tags: [jump-search]
authors:
  - soumalyatheking22012001
---

In this article, we lay out all the requirements for Jump search algorithm in python but it can be recreated in any language.

## Description

Like Binary Search, Jump Search is a searching algorithm for sorted arrays. The basic idea is to check fewer elements (than linear search) by jumping ahead by fixed steps or skipping some elements in place of searching all elements.
For example, suppose we have an array arr[] of size n and block (to be jumped) size m. Then we search at the indexes arr[0], arr[m], arr[2m]…..arr[km] and so on. Once we find the interval (arr[km] < x < arr[(k+1)m]), we perform a linear search operation from the index km to find the element x.
Let’s consider the following array: (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610). Length of the array is 16. Jump search will find the value of 55 with the following steps assuming that the block size to be jumped is 4.

STEP 1: Jump from index 0 to index 4;

STEP 2: Jump from index 4 to index 8;

STEP 3: Jump from index 8 to index 12;

STEP 4: Since the element at index 12 is greater than 55 we will jump back a step to come to index 8.

STEP 5: Perform linear search from index 8 to get the element 55.

## Requirements

For the purposes of this project, we'll assume that the search space is a list of integers.
Specifically, we'll accept two inputs on the command line: the list of integers and the
integer to find:

```shell
./ python "jump search.py"
Enter array elements: 3 4 1 7
Sorting the array for better results!
Sorted array:
[1, 3, 4, 7]
Enter the element to be searched: 4
number 1 is at index 3
```

If successful, the script should return `true`. Otherwise, the script should return `false`.
If any user input errors occur, the script should output the following usage message:

## What is the optimal block size to be skipped

In the worst case, we have to do n/m jumps and if the last checked value is greater than the element to be searched for, we perform m-1 comparisons more for linear search. Therefore the total number of comparisons in the worst case will be ((n/m) + m-1). The value of the function ((n/m) + m-1) will be minimum when m = √n. Therefore, the best step size is m = √n.

## Testing

| Description | List Input | Target Integer Input | Output |
|-------------|------------|---------------|--------|
| No Input    |            |               | error\* |
| Missing Input: List | `1, 2, 3, 4` | | error\* |
| Missing Input: Target | `""` | `5` | error\* |
| Out of Order Input | `3, 5, 1, 2` | `3` | error\* |
| Sample Input: First True | `1, 3, 5, 7` | `1` | `1` |
| Sample Input: Last True | `1, 3, 5, 7` | `7` | `7` |
| Sample Input: Middle True | `1, 3, 5, 7` | `5` | `5` |
| Sample Input: One True | `5` | `5` | `5` |
| Sample Input: One False | `5` | `7` | `-1` |
| Sample Input: Many False | `1, 3, 5, 6` | `7` | `-1` |

\*The error string to print: `Usage: please provide a list of  integers ("1, 4, 5, 11, 12") and the integer to find ("11")`

## Time complexity

O(√n)

## Auxillary Space

O(1)

## Articles

{% include article_list.md collection=site.categories.jump-search %}

## Further Reading

- Fill out as needed
