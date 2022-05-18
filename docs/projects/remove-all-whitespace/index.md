---

title: Remove All Whitespace in Every Language
layout: default
date: 2020-10-21
last-modified: 2020-10-28
featured-image:
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

Every project in the Sample Programs repo should be tested. In this section, we specify the set of tests specific to Projects. To keep things simple, we split up testing into two subsets: valid and invalid. Valid tests refer to tests that occur under correct input conditions. Invalid tests refer to tests that occur on bad input (e.g., letters instead of numbers).

### Valid Tests

No 'Valid Tests' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

### Invalid Tests

No 'Invalid Tests' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## Articles

- [Remove All Whitespace in Python](https://sampleprograms.io/projects/remove-all-whitespace/python)