---
title: Duplicate Character Counting in Every Language
layout: default
date: 2020-10-04
last-modified: 2020-10-04
featured-image: <name of featured image file in assets folder>
tags: [<a list of tags>]
authors:
  - GoodbyeBlues
---

An overview of the duplicate characters counting problem.

## Goal

Although a one line solution for this problem is feasible, just as huge brute force solutions are, we should avoid both of these approaches. Instead, our goal should be to find a fine line between both, where the code is not bogged down but is largely readable and maintainable

## Requirements

The code should return the count of all duplicate, case-insensitive, alphanumeric characters, that occur more than once in the given string. 

## Examples

* "Hello, World!"  # 'l' occurs 3 times and 'o' occurs 2 times
* "Goodbye, Blues!"  # 'o' occurs 2 times and 'e' occurs 2 times
* "aaaAAA"  # 'a' occurs 3 times and 'A' occurs 3 times

## Articles

{% include article_list.md collection=site.categories.[name of project] % }

## Further Reading

- [List useful links here]
