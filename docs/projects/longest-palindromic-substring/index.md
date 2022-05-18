---

title: Longest Palindromic Substring in Every Language
layout: default
date: 2019-10-08
last-modified: 2020-05-02
featured-image:
tags: [longest-palindrome-substring]
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

### Method 1 ( Brute Force )

The simple approach is to check each substring whether the substring is a palindrome or not. We can run three loops, the outer two loops pick all substrings one by one by fixing the corner characters, the inner loop checks whether the picked substring is palindrome or not.

- Time complexity: O (n<sup>3</sup>)
- Auxiliary complexity: O (1)

### Method 2 ( Dynamic Programming )

The time complexity can be reduced by storing results of subproblems. We maintain a boolean table[n][n] that is filled in bottom up manner. The value of table[i][j] is true, if the substring is palindrome, otherwise false. To calculate table[i][j], we first check the value of table[i+1][j-1], if the value is true and str[i] is same as str[j], then we make table[i][j] true. Otherwise, the value of table[i][j] is made false.

- Time complexity: O ( n^2 )
- Auxiliary Space: O ( n^2 )

### Method 3

The time complexity of the Dynamic Programming based solution is O(n<sup>2</sup>) and it requires O(n<sup>2</sup>) extra space. We can find the longest palindrome substring in (n<sup>2</sup>) time with O(1) extra space. The idea is to generate all even length and odd length palindromes and keep track of the longest palindrome seen so far.

#### Step to generate odd length palindrome:

Fix a centre and expand in both directions for longer palindromes.

#### Step to generate even length palindrome

Fix two centre ( low and high ) and expand in both directions for longer palindromes.

- Time complexity: O (n<sup>2</sup>) where n is the length of input string.
- Auxiliary Space: O ( 1 )


## Testing

Every project in the Sample Programs repo should be tested. In this section, we specify the set of tests specific to Projects. To keep things simple, we split up testing into two subsets: valid and invalid. Valid tests refer to tests that occur under correct input conditions. Invalid tests refer to tests that occur on bad input (e.g., letters instead of numbers).

### Valid Tests

No 'Valid Tests' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

### Invalid Tests

No 'Invalid Tests' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## Articles

- [Longest Palindromic Substring in Go](https://sampleprograms.io/projects/longest-palindromic-substring/go)
- [Longest Palindromic Substring in Javascript](https://sampleprograms.io/projects/longest-palindromic-substring/javascript)
- [Longest Palindromic Substring in Python](https://sampleprograms.io/projects/longest-palindromic-substring/python)