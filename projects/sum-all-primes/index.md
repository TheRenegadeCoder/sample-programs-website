---
title: Sum All Primes in Every Language
layout: default
date: 2020-10-26
last-modified: 2020-10-30
featured-image:
tags: [sum-all-primes, javascript]
authors:
    - barhouum7
---

In this article, we'll outline the sum all primes project.

## Description

A prime number is a whole number greater than 1 with exactly two divisors: 1 and itself. 

For example, 2 is a prime number because it is only divisible by 1 and 2.

In contrast, 4 is not prime since it is divisible by 1, 2 and 4.

## Requirements

The purpose of this program is to return the sum of all prime numbers that are less than or equal to a given number as follows:

```javascript
sum-all-primes.lang Input: 10
Output: "17"

sum-all-primes.lang Input: 977
Output: "73156"
```

The result should be a number.

## Testing

The following table contains various test cases that you can use to verify the 
correctness of your solution:

| Description | Input | Output |
|--------------|-------|--------|
| No Input | | "Usage: please provide a number" |
| Empty Input | "" | "Usage: please provide a number" |
| Simple Input | "10" | "17" |
| Simple Input | "977" | "73156" |

## Articles

{% include article_list.md collection=site.categories.sum-all-primes %}

## Further Reading

- Fill out as needed
