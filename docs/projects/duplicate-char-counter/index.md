---

title: Duplicate Character Counting in Every Language
layout: default
date: 2020-10-11
last-modified: 2020-10-11
featured-image: 
tags: [duplicate-character-counting]
authors:
  - GoodbyeBlues

---

Welcome to the Duplicate Char Counter page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

## Description

Although a one line solution for this problem is feasible, just as huge brute force solutions are, we should avoid both of these approaches. Instead, our goal should be to find a fine line between both, where the code is not bogged down but is largely readable and maintainable.


## Requirements

The code should return the count of all duplicate, case-insensitive, alphanumeric characters, that occur more than once in the given string. Characters should also be presented in the order in which they appear in the string. For instance, 'abba' should output 'a' as the firstcharacter that has a duplicate.


## Testing

|   Description  | Input           | Output                                                                                                        |
| :--------------| :-------------: | :-----------------------------------------------------------------------------------------------------------: |
| Basic String   | "goodbyeblues"  | Characters: o, Occurrences: 2 <br /> Characters: b, Occurrences: 2 <br /> Characters: e, Occurrences: 2 <br />|
| Correct Order  | "abba"          | Characters: a, Occurrences: 2 <br /> Characters: b, Occurrences: 2                                            |
| Case Distinct  | "aAbB"          | No duplicate characters                                                                                       |


**Note:** Duplicate Char Counter is not currently tested by Glotter. Consider contributing!

## Articles

- [Duplicate Char Counter in Javascript](https://sampleprograms.io/projects/duplicate-char-counter/javascript)