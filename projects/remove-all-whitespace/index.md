---
title: Remove All Whitespace in Every Language
layout: default
date: 2020-10-21
last-modified: 2020-10-24
featured-image:
tags: [remove-all-whitespace, c]
authors:
    - barhouum7
---

In this article, we'll outline the Remove All Whitespace project. 

## Requirements

A string is a collection of characters. Sometimes strings contain whitespace characters like " ", "\t", and "\n". 
The purpose of this program is to remove all such spaces from a string as follows:

```
remove-all-whitespace.lang "   Hello, World!   "
"Hello,World!"
```

In this case, we start with a string that has leading, trailing, and inner spaces. Ultimately, we want to
return a string with all of the spaces removed.

## Testing

The following table contains various test cases that you can use to verify the 
correctness of your solution:

| Description                   | Input                         | Output                           |
|-------------------------------|-------------------------------|----------------------------------|
| No Input                      |                               | "Usage: please provide a string" |
| Empty Input                   | ""                            | "Usage: please provide a string" |
| Sample Input: No Spaces       | "RemoveAllWhitespace"         | "RemoveAllWhitespace"            |
| Sample Input: Leading Spaces  | "      RemoveAllWhitespace"   | "RemoveAllWhitespace"            |
| Sample Input: Trailing Spaces | "RemoveAllWhitespace      "   | "RemoveAllWhitespace"            |
| Sample Input: Inner Spaces    | "Remove    All   Whitespace"  | "RemoveAllWhitespace"            |

## Articles

{% include article_list.md collection=site.categories.remove-all-whitespace %}

## Further Reading

- Fill out as needed
