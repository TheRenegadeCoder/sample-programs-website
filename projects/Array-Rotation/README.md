---
title: Maximum Array Rotation in Every Language
layout: default
date: 2020-10-14
last-modified: 2020-10-14
featured-image: 
tags: [maximum-array-rotation]
authors:
  - agasheaditya
---

In this article, we'll learn about the Maximum Array Rotation project.

## Description

Given a list, L, of integers, we can compute the weighted sum, W, as followed:

```
W = L[0] * 0 + L[1] * 1 + ... + L[N - 1] * N - 1
```

In this case, N is the length of the list. As a result, if the list contained 5 items,
the last term in the list would be multiplied by 4.

Given that we can compute the weighted sum, the purpose of this project is to
find the maximum array rotation. In other words, if we were to rotate the list N 
times, what's the largest weighted sum we could get? Here's what that would look
like with this list (2, 8, 3, 1): 

 > array after 1st rotation ->[2, 8, 3, 1]
                                            0
                                            8
                                            6
                                            3
-----------------------------------------------
 > array after 2nd rotation ->[1, 2, 8, 3]
                                            0
                                            2
                                            16
                                            9
------------------------------------------------
 > array after 3rd rotation ->[3, 1, 2, 8]
                                            0
                                            1
                                            4
                                            24
------------------------------------------------
 > array after 4th rotation ->[8, 3, 1, 2]
                                            0
                                            3
                                            2
                                            6
------------------------------------------------

## Requirements

```shell
./sample-program.lang "8, 3, 1, 2"
```

## Testing

| Description                  | Input                     | Output                                                         |
| ---------------------------- | ------------------------- | -------------------------------------------------------------- |
| No Input                     |                           | "Usage: please provide a list of integers (e.g. "8, 3, 1, 2")" |
| Empty Input                  | ""                        | "Usage: please provide a list of integers (e.g. "8, 3, 1, 2")" |
| Sample Input: No Rotation    | "3, 1, 2, 8"              | 29                                                             |
| Sample Input: One Rotation   | "1, 2, 8, 3"              | 29                                                             |
| Sample Input: Many Rotations | "8, 3, 1, 2"              | 29                                                             |


## Articles

{% include article_list.md collection=site.categories.maximum-array-rotation %}

## Further Reading

- > https://docs.python.org/3/tutorial/datastructures.html
