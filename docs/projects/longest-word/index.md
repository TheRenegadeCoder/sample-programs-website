---
title: Longest Word in Every Language
layout: default
date: 2020-10-31
last-modified: 2020-10-31
featured-image: longest-word-in-every-language.jpg
tags: [longest-word]
authors:
    - barhouum7
    - the_renegade_coder

---

Welcome to the Longest Word page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

## Description

Given a string, this program should break it up into words and determine
the length of the longest word. In this case, a word is defined as anything
surrounded by whitespace. For simplicity, we'll restrict whitespace to the
following four special characters:

- Spaces: " "
- Tabs: "\t"
- Newlines: "\n"
- Carriage Returns: "\r"

For example, if we had a string, "How now brown cow", we can figure out which
word is the longest by breaking up the string into words. In this case, this
string has the following four words:

- "How"
- "now"
- "brown"
- "cow"

In this case, "brown" is clearly the longest word, so we'll return 5 as a result.


## Requirements

To satisfy the requirements, a program must accept a string on the command line 
and return the length of the longest word in the string:

```shell
$ ./longest-word-in-string.lang "Google do a barrel roll"
$ 6
```

In this case, we have a string with 5 words. It appears that there are two words
that share the largest number of characters: Google and barrel. Naturally, we
don't care to decide between the two words. Instead, we return the length of them 
both: 6.


## Testing

Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Longest Word.
In order to keep things simple, we split up the testing as follows:

- Longest Word Valid Tests
- Longest Word Invalid Tests

### Longest Word Valid Tests

| Description | Input | Output |
| ----------- | ----- | ------ |
| Sample Input: Many Words | "May the force be with you" | "5" |
| Sample Input: Single Word | "Floccinaucinihilipilification" | "29" |
| Sample Input: Multiline | "Hi,\nMy name is Paul!" | "5" |

### Longest Word Invalid Tests

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input | "" |

All of these tests should output the following:

```
Usage: please provide a string
```


## Articles

- [Longest Word in Algol68](https://sampleprograms.io/projects/longest-word/algol68)
- [Longest Word in C](https://sampleprograms.io/projects/longest-word/c)
- [Longest Word in C++](https://sampleprograms.io/projects/longest-word/c-plus-plus)
- [Longest Word in Euphoria](https://sampleprograms.io/projects/longest-word/euphoria)
- [Longest Word in Go](https://sampleprograms.io/projects/longest-word/go)
- [Longest Word in Java](https://sampleprograms.io/projects/longest-word/java)
- [Longest Word in Mathematica](https://sampleprograms.io/projects/longest-word/mathematica)
- [Longest Word in Php](https://sampleprograms.io/projects/longest-word/php)
- [Longest Word in Python](https://sampleprograms.io/projects/longest-word/python)
- [Longest Word in Rust](https://sampleprograms.io/projects/longest-word/rust)

***

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Longest Palindromic Substring)](https://sampleprograms.io/projects/longest-palindromic-substring)

</div>

<div id="next" markdown="1">

[Next Project (Maximum Array Rotation) -->](https://sampleprograms.io/projects/maximum-array-rotation)

</div>

</nav>