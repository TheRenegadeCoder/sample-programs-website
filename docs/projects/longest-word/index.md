---
date: 2022-04-28
featured-image: longest-word-in-every-language.jpg
last-modified: 2025-10-04
layout: default
tags:
- longest-word
title: Longest Word
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/projects/longest-word/description.md
- sources/projects/longest-word/requirements.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the Longest Word page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

This article was written by:

- Jeremy Grifski

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

There are 31 articles:

- [Longest Word in Algol68](https://sampleprograms.io/projects/longest-word/algol68)
- [Longest Word in Awk](https://sampleprograms.io/projects/longest-word/awk)
- [Longest Word in Beef](https://sampleprograms.io/projects/longest-word/beef)
- [Longest Word in Brainfuck](https://sampleprograms.io/projects/longest-word/brainfuck)
- [Longest Word in C](https://sampleprograms.io/projects/longest-word/c)
- [Longest Word in C#](https://sampleprograms.io/projects/longest-word/c-sharp)
- [Longest Word in C++](https://sampleprograms.io/projects/longest-word/c-plus-plus)
- [Longest Word in Coffeescript](https://sampleprograms.io/projects/longest-word/coffeescript)
- [Longest Word in Commodore Basic](https://sampleprograms.io/projects/longest-word/commodore-basic)
- [Longest Word in Dart](https://sampleprograms.io/projects/longest-word/dart)
- [Longest Word in Euphoria](https://sampleprograms.io/projects/longest-word/euphoria)
- [Longest Word in Go](https://sampleprograms.io/projects/longest-word/go)
- [Longest Word in Java](https://sampleprograms.io/projects/longest-word/java)
- [Longest Word in Javascript](https://sampleprograms.io/projects/longest-word/javascript)
- [Longest Word in Julia](https://sampleprograms.io/projects/longest-word/julia)
- [Longest Word in Kotlin](https://sampleprograms.io/projects/longest-word/kotlin)
- [Longest Word in Lua](https://sampleprograms.io/projects/longest-word/lua)
- [Longest Word in M4](https://sampleprograms.io/projects/longest-word/m4)
- [Longest Word in Mathematica](https://sampleprograms.io/projects/longest-word/mathematica)
- [Longest Word in Odin](https://sampleprograms.io/projects/longest-word/odin)
- [Longest Word in Pascal](https://sampleprograms.io/projects/longest-word/pascal)
- [Longest Word in Perl](https://sampleprograms.io/projects/longest-word/perl)
- [Longest Word in Php](https://sampleprograms.io/projects/longest-word/php)
- [Longest Word in Powershell](https://sampleprograms.io/projects/longest-word/powershell)
- [Longest Word in Python](https://sampleprograms.io/projects/longest-word/python)
- [Longest Word in R](https://sampleprograms.io/projects/longest-word/r)
- [Longest Word in Ruby](https://sampleprograms.io/projects/longest-word/ruby)
- [Longest Word in Rust](https://sampleprograms.io/projects/longest-word/rust)
- [Longest Word in Swift](https://sampleprograms.io/projects/longest-word/swift)
- [Longest Word in Typescript](https://sampleprograms.io/projects/longest-word/typescript)
- [Longest Word in Visual Basic](https://sampleprograms.io/projects/longest-word/visual-basic)

***

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Longest Palindromic Substring)](https://sampleprograms.io/projects/longest-palindromic-substring)

</div>

<div id="next" markdown="1">

[Next Project (Maximum Array Rotation) -->](https://sampleprograms.io/projects/maximum-array-rotation)

</div>

</nav>