---
authors:
- Jeremy Grifski
- Ron Zuckerman
date: 2018-04-10
featured-image: programming-languages.jpg
last-modified: 2026-04-11
layout: default
tags:
- pascal
title: The Pascal Programming Language
title1: The Pascal
title2: Programming Language
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/languages/pascal/description.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the Pascal page! Here, you'll find a description of the language as well as a list of sample programs in that language.

This article was written by:

- Jeremy Grifski
- Ron Zuckerman

## Description

According to [Wikipedia][1], Pascal is an imperative and procedural language which 
first appeared in 1970. Pascal's creator, [Niklaus Wirth][2], designed the language 
with compiler and runtime efficiency in mind. In addition, Wirth drew much of 
the inspiration for [Pascal][1] from the [ALGOL family][3] of languages.

That said, Pascal isn't simply an ALGOL clone. In fact, Pascal includes many 
additions to ALGOL such as mechanisms for defining custom datatypes. Likewise, 
the language includes several additional features like enumerations, subranges, 
and records.

As an added bonus, Pascal is a strongly typed language. This forces the user to 
explicitly write conversions between types, so errors can be caught at compile 
time. Unfortunately, I've read that [Pascal has a loophole in the type system][4]. I 
just haven't found any articles describing it. If you know, let me know in the 
comments.

Before we get into Hello World, I want to look a bit deeper at sets because I find 
them interesting. In Pascal, we can define a set as follows:

```pascal
var
  Set1 : set of 5..20;
  Set2 : set of 'f'..'m';
```

With Pascal being such an old language, I find it interesting how intuitive the set 
syntax is. In fact, I can't think of many industrial languages that have such a nice 
syntax for setting up lists or sets. In fact, here's how you would generate a list of 
numbers in a few languages:

```java
// Java 8+
int[] range = IntStream.rangeClosed(5, 20).toArray();
```

```python
# Python 3
list(range(5, 20))
```

```javascript
// JavaScript
var list = [];
for (var i = 5; i <= 20; i++) {
  list.push(i);
}
```

```c#
// C#
int[] values = Enumerable.Range(5, 15).ToArray();
```

That Pascal set syntax is great. In fact, it even allows us to do fun things like 
check values in some range:

```pascal
if i in [5..20] then
```

At any rate, I think we've played around enough

[1]: https://en.wikipedia.org/wiki/Pascal_(programming_language)
[2]: https://en.wikipedia.org/wiki/Niklaus_Wirth
[3]: https://en.wikipedia.org/wiki/ALGOL
[4]: https://www.lysator.liu.se/c/bwk-on-pascal.html


## Articles

There are 38 articles:

- [Baklava in Pascal](/projects/baklava/pascal)
- [Base64 Encode Decode in Pascal](/projects/base64-encode-decode/pascal)
- [Binary Search in Pascal](/projects/binary-search/pascal)
- [Bubble Sort in Pascal](/projects/bubble-sort/pascal)
- [Capitalize in Pascal](/projects/capitalize/pascal)
- [Convex Hull in Pascal](/projects/convex-hull/pascal)
- [Depth First Search in Pascal](/projects/depth-first-search/pascal)
- [Dijkstra in Pascal](/projects/dijkstra/pascal)
- [Duplicate Character Counter in Pascal](/projects/duplicate-character-counter/pascal)
- [Even Odd in Pascal](/projects/even-odd/pascal)
- [Factorial in Pascal](/projects/factorial/pascal)
- [Fibonacci in Pascal](/projects/fibonacci/pascal)
- [File Input Output in Pascal](/projects/file-input-output/pascal)
- [Fizz Buzz in Pascal](/projects/fizz-buzz/pascal)
- [Fraction Math in Pascal](/projects/fraction-math/pascal)
- [Hello World in Pascal](/projects/hello-world/pascal)
- [Insertion Sort in Pascal](/projects/insertion-sort/pascal)
- [Job Sequencing in Pascal](/projects/job-sequencing/pascal)
- [Josephus Problem in Pascal](/projects/josephus-problem/pascal)
- [Linear Search in Pascal](/projects/linear-search/pascal)
- [Longest Common Subsequence in Pascal](/projects/longest-common-subsequence/pascal)
- [Longest Palindromic Substring in Pascal](/projects/longest-palindromic-substring/pascal)
- [Longest Word in Pascal](/projects/longest-word/pascal)
- [Maximum Array Rotation in Pascal](/projects/maximum-array-rotation/pascal)
- [Maximum Subarray in Pascal](/projects/maximum-subarray/pascal)
- [Merge Sort in Pascal](/projects/merge-sort/pascal)
- [Minimum Spanning Tree in Pascal](/projects/minimum-spanning-tree/pascal)
- [Palindromic Number in Pascal](/projects/palindromic-number/pascal)
- [Prime Number in Pascal](/projects/prime-number/pascal)
- [Quick Sort in Pascal](/projects/quick-sort/pascal)
- [Quine in Pascal](/projects/quine/pascal)
- [Remove All Whitespace in Pascal](/projects/remove-all-whitespace/pascal)
- [Reverse String in Pascal](/projects/reverse-string/pascal)
- [Roman Numeral in Pascal](/projects/roman-numeral/pascal)
- [Rot13 in Pascal](/projects/rot13/pascal)
- [Selection Sort in Pascal](/projects/selection-sort/pascal)
- [Transpose Matrix in Pascal](/projects/transpose-matrix/pascal)
- [Zeckendorf in Pascal](/projects/zeckendorf/pascal)