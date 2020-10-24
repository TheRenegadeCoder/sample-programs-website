---
title: removingExtraWhiteSpaces in Every Language
layout: default
date: 2020-10-21
last-modified: 2020-10-21
featured-image:
tags: [removingExtraWhiteSpaces, c]
authors:
    - barhouum7
---

Removing extra white spaces from a given string

Given a string, remove all spaces from the string and return it with it's _length_.

```c
Input:  " Removing   Extra White   Spaces  "
Output: "removingExtraWhiteSpaces"
```

## Requirements

A string is nothing but an array of characters. The value of a string is determined by the terminating character. Its value is considered to be 0.

As given in the example above, you need to enter a string first up.

The string entered here is as follows: "&nbsp;&nbsp;Removing&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Extra&nbsp;White&nbsp;&nbsp;&nbsp;Spaces&nbsp;&nbsp;&nbsp;&nbsp;"

As you can see, there are quite a few blank spaces in the string entered above.

Hence, the string becomes like this after removing all the blank spaces:

"removingExtraWhiteSpaces"

## Testing

The following table contains various test cases that you can use to verify the 
correctness of your solution:

| Description | Input | Output |
|--------------|-------|--------|
| No Input | | "Wrong input! , please try again." |
| Empty Input | "" | "Wrong input! , please try again." |
| Any String Input| "&nbsp;&nbsp;Removing&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Extra&nbsp;White&nbsp;&nbsp;&nbsp;Spaces&nbsp;&nbsp;&nbsp;&nbsp;" | "removingExtraWhiteSpaces" |

## Articles

{% include article_list.md collection=site.categories.removingExtraWhiteSpaces %}

## Further Reading

- Fill out as needed
