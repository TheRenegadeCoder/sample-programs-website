---
title: Longest Palindromic Substring in Every Language
layout: default
date: 2019-10-08
last-modified: 2020-05-02
featured-image: longest-palindromic-substring-in-every-language.jpg
tags: [longest-palindromic-substring]
authors: 
  - Sayantan Paul

---

Welcome to the Longest Palindromic Substring page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

## Description

Palindrome is a phenomenon, where a string has same sequence of letters when read start --> end and end --> start.

Let's say we have a string,

```
s = 'paapaapap'
```

Here, we have seven palindromic substrings. 

```
sub_1 = 'aa'
sub_2 = 'paap'
sub_3 = 'paapaap'
sub_4 = 'aapaa'
sub_5 = 'apap'
sub_6 = 'pap'
sub_7 = 'apaapa'
```

Out of the seven,  `sub_3 = 'paapaap'` is the longest. hence the output would be `'paapaap'`


## Requirements

This problem can be solved using 3 methods.

### Method 1 (Brute Force)

The simple approach is to check each substring whether the substring is a palindrome or not. We can run three loops, the outer two loops pick all substrings one by one by fixing the corner characters, the inner loop checks whether the picked substring is palindrome or not.

- Time complexity: O(n<sup>3</sup>)
- Auxiliary complexity: O(1)

### Method 2 (Dynamic Programming)

The time complexity can be reduced by storing results of subproblems. We maintain a boolean table[n][n] that is filled in bottom up manner. The value of table[i][j] is true, if the substring is palindrome, otherwise false. To calculate table[i][j], we first check the value of table[i+1][j-1], if the value is true and str[i] is same as str[j], then we make table[i][j] true. Otherwise, the value of table[i][j] is made false.

- Time complexity: O(n<sup>2</sup>)
- Auxiliary Space: O(n<sup>2</sup>)

### Method 3

The time complexity of the Dynamic Programming based solution is O(n<sup>2</sup>) and it requires O(n<sup>2</sup>) extra space. We can find the longest palindrome substring in O(n<sup>2</sup>) time with O(1) extra space. The idea is to generate all even length and odd length palindromes and keep track of the longest palindrome seen so far.

#### Step to generate odd length palindrome:

Fix a center and expand in both directions for longer palindromes.

#### Step to generate even length palindrome

Fix two center (low and high) and expand in both directions for longer palindromes.

- Time complexity: O(n<sup>2</sup>) where n is the length of input string.
- Auxiliary Space: O(1)


## Testing

Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Longest Palindromic Substring.
In order to keep things simple, we split up the testing as follows:

- Lps Valid Tests
- Lps Invalid Tests

### Lps Valid Tests

| Description | Input | Output |
| ----------- | ----- | ------ |
| Sample Input: One Palindrome | "racecar" | "racecar" |
| Sample Input: Two Palindrome | "kayak mom" | "kayak" |
| Sample Input: Complex Palindrome | "step on no pets" | "step on no pets" |

### Lps Invalid Tests

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input | "" |
| Invalid Input: No Palindromes | "polip" |

All of these tests should output the following:

```
Usage: please provide a string that contains at least one palindrome
```


## Articles

- [Longest Palindromic Substring in Algol68](https://sampleprograms.io/projects/longest-palindromic-substring/algol68)
- [Longest Palindromic Substring in Euphoria](https://sampleprograms.io/projects/longest-palindromic-substring/euphoria)
- [Longest Palindromic Substring in Go](https://sampleprograms.io/projects/longest-palindromic-substring/go)
- [Longest Palindromic Substring in Javascript](https://sampleprograms.io/projects/longest-palindromic-substring/javascript)
- [Longest Palindromic Substring in Mathematica](https://sampleprograms.io/projects/longest-palindromic-substring/mathematica)
- [Longest Palindromic Substring in Php](https://sampleprograms.io/projects/longest-palindromic-substring/php)
- [Longest Palindromic Substring in Python](https://sampleprograms.io/projects/longest-palindromic-substring/python)
- [Longest Palindromic Substring in Rust](https://sampleprograms.io/projects/longest-palindromic-substring/rust)

***

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Longest Common Subsequence)](https://sampleprograms.io/projects/longest-common-subsequence)

</div>

<div id="next" markdown="1">

[Next Project (Longest Word) -->](https://sampleprograms.io/projects/longest-word)

</div>

</nav>