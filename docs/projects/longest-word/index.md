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

The following table contains various test cases that you can use to verify the 
correctness of your solution:

| Description               | Input                           | Output                           |
|---------------------------|---------------------------------|----------------------------------|
| No Input                  |                                 | "Usage: please provide a string" |
| Empty Input               | ""                              | "Usage: please provide a string" |
| Sample Input: Many Words  | "May the force be with you"     | 5                                |
| Sample Input: Single Word | "Floccinaucinihilipilification" | 29                               |
| Sample Input: Multiline   | "Hi,\nMy name is Paul!"         | 5                                |

As always, these tests will be run against any code submitted to the repo via [Glotter][glotter-github].


## Articles

- [Longest Word in Python](https://sampleprograms.io/projects/longest-word/python)