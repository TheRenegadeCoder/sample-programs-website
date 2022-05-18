---

title: Longest Word in Every Language
layout: default
date: 2020-10-31
last-modified: 2020-10-31
featured-image:
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

Every project in the Sample Programs repo should be tested. In this section, we specify the set of tests specific to Projects. To keep things simple, we split up testing into two subsets: valid and invalid. Valid tests refer to tests that occur under correct input conditions. Invalid tests refer to tests that occur on bad input (e.g., letters instead of numbers).

### Valid Tests

No 'Valid Tests' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

### Invalid Tests

No 'Invalid Tests' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## Articles

- [Longest Word in Python](https://sampleprograms.io/projects/longest-word/python)