---
title: Longest Word in Every Language
layout: default
date: 2020-10-25
last-modified: 2020-10-30
featured-image:
tags: [longest-word]
authors:
    - barhouum7
    - the_renegade_coder
---

In this article, we'll outline the longest word in a string project.

## Description

You have to go through each word and figure out which one is the longest and 
return not the word, but how many characters it has.

In this program, we want to look at each individual word and count how many 
letters are in each. Then, compare the counts to determine which word has the 
most characters and return the length of the longest word.

## Requirements

The purpose of this program is to return the length of the longest word in 
the provided sentence as follows:

```shell
$ ./longest-word-in-string.lang "Google do a barrel roll"
$ 6
```

The result should be a number.

## Testing

The following table contains various test cases that you can use to verify the 
correctness of your solution:

| Description               | Input                           | Output                           |
|---------------------------|---------------------------------|----------------------------------|
| No Input                  |                                 | "Usage: please provide a string" |
| Empty Input               | ""                              | "Usage: please provide a string" |
| Sample Input: Many Words  | "May the force be with you"     | 5                                |
| Sample Input: Single Word | "Floccinaucinihilipilification" | 29                               |

As always, these tests will be run against any code submitted to the repo via [Glotter][glotter-github].

## Articles

{% include article_list.md collection=site.categories.longest-word %}

## Further Reading

- Fill out as needed

[glotter-github]: https://github.com/auroq/glotter
