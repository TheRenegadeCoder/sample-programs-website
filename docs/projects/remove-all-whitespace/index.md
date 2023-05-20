---
title: Remove All Whitespace in Every Language
layout: default
date: 2020-10-21
last-modified: 2020-10-28
featured-image: remove-all-whitespace-in-every-language.jpg
tags: [remove-all-whitespace]
authors:
    - barhouum7
    - the_renegade_coder

---

Welcome to the Remove All Whitespace page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

## Description

A string is a collection of characters. Sometimes strings contain whitespace characters like " ", "\t", and "\n". 
The purpose of this project is to remove all such spaces from a string. For example, given the string 
"Remove All Whitespace", we could generate a new string with all the whitespace removed as follows: 
"RemoveAllWhitespace". In this case, two spaces were removed at positions 6 and 10.   

For simplicity, we will be restricting the types of whitespace to these four types of characters: spaces (" "),
tabs ("\t"), newlines ("\n"), and carriage returns ("\r"). We are aware that other types of whitespace exist.
That said, programs in this collection tend to be simple, so we can replicate them in as many programming
languages as possible. 


## Requirements

To satisfy the requirements, a program must accept a string on the command line and return a new string
with all spaces removed as follows:

```shell
$ remove-all-whitespace.lang "   Hello, World!   "
$ "Hello,World!"
```

In this case, we start with a string that has leading, trailing, and inner spaces. Ultimately, we want to
return a string with all of the spaces removed.


## Testing

Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Remove All Whitespace.
In order to keep things simple, we split up the testing as follows:

- Remove All Whitespace Valid Tests
- Remove All Whitespace Invalid Tests

### Remove All Whitespace Valid Tests

| Description | Input |
| ----------- | ----- |
| Sample Input: No Spaces | "RemoveAllWhitespace" |
| Sample Input: Leading Spaces | "    RemoveAllWhitespace" |
| Sample Input: Trailing Spaces | "RemoveAllWhitespace    " |
| Sample Input: Inner Spaces | "Remove All Whitespace" |
| Sample Input: Tabs | "\tRemove\tAll\tWhitespace\t" |
| Sample Input: Newlines | "\nRemove\nAll\nWhitespace\n" |
| Sample Input: Carriage Returns | "\rRemove\rAll\rWhitespace\r" |

All of these tests should output the following:

```
RemoveAllWhitespace
```

### Remove All Whitespace Invalid Tests

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input | "" |

All of these tests should output the following:

```
Usage: please provide a string
```


## Articles

- [Remove All Whitespace in Algol68](https://sampleprograms.io/projects/remove-all-whitespace/algol68)
- [Remove All Whitespace in Euphoria](https://sampleprograms.io/projects/remove-all-whitespace/euphoria)
- [Remove All Whitespace in Julia](https://sampleprograms.io/projects/remove-all-whitespace/julia)
- [Remove All Whitespace in Mathematica](https://sampleprograms.io/projects/remove-all-whitespace/mathematica)
- [Remove All Whitespace in Php](https://sampleprograms.io/projects/remove-all-whitespace/php)
- [Remove All Whitespace in Python](https://sampleprograms.io/projects/remove-all-whitespace/python)
- [Remove All Whitespace in Rust](https://sampleprograms.io/projects/remove-all-whitespace/rust)

***

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Quine)](https://sampleprograms.io/projects/quine)

</div>

<div id="next" markdown="1">

[Next Project (Reverse String) -->](https://sampleprograms.io/projects/reverse-string)

</div>

</nav>