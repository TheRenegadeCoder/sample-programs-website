---
title: Longest Palindromic Substring in Mathematica
layout: default
date: 2023-01-18
featured-image: longest-palindromic-substring-in-every-language.jpg
last-modified: 2023-01-18

---

Welcome to the [Longest Palindromic Substring](https://sampleprograms.io/projects/longest-palindromic-substring) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* Brute force approach of generating all substrings and testing: *)

longestPalindromicSubstring = word \[Function] First @ MaximalBy[
     Select[PalindromeQ][
      Flatten[Table[
        StringTake[word, {i, j}],
        {i, 1, StringLength[word]}, {j, i + 1, StringLength[word]}],
       1]],
     StringLength,
     UpTo[1]];

(* The outer function provides the 'user interface' (e.g., the string parsing): *)

longestPalindromicSubstringMain = Function[{s},
   Module[{e = "Usage: please provide a string that contains at least one palindrome"},
    Catch[
     longestPalindromicSubstring @
      If[StringLength[s] > 0, s, Throw[e]]]]];


(* Valid Tests *)

Print /@ longestPalindromicSubstringMain /@ {
    "racecar",
    "kayak mom",
    "step on no pets"
    };


(* Invalid Tests *)

longestPalindromicSubstringMain[""]
```

{% endraw %}

[Longest Palindromic Substring](https://sampleprograms.io/projects/longest-palindromic-substring) in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).