---
title: Palindromic Number in Mathematica
layout: default
date: 2023-01-18
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2023-01-18

---

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* This is provided by a Mathematica built-in PalindromeQ.  Only a function to provide the 'user interface' is needed: *)

palindromicNumberMain = s \[Function] Module[
    {e = "Usage: please input a non-negative integer"},
    Catch[
     Replace[
      PalindromeQ@
       (* convert string to integer, or throw *)
       If[StringMatchQ[s, DigitCharacter ..],
        FromDigits[s],
        Throw[e]],
      {False -> "false", True -> "true"}]]];


(* Valid Tests *)

Print /@ palindromicNumberMain /@ {
    "7",
    "2442",
    "232",
    "5215",
    "521"
    };


(* Invalid Tests *)

palindromicNumberMain[""]
palindromicNumberMain["a"]
palindromicNumberMain["-5"]
palindromicNumberMain["5.41"]
```

{% endraw %}

[Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).