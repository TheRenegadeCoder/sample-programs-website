---
title: Even Odd in Mathematica
layout: default
date: 2023-01-21
featured-image: even-odd-in-every-language.jpg
last-modified: 2023-01-21

---

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* The Mathematica built-in EvenQ essentially provides the required behavior;
so the only code needed is the 'user interface' to make it look a little more
like a Unix command-line tool: *)

evenOddMain = Catch[
    Module[{fromNegativeDigits},
     (* oddly, Mathematica doesn't appear to provide a function which can parse strings representing negative integers *)
     fromNegativeDigits = Piecewise[{
         {FromDigits[#], StringMatchQ[#, DigitCharacter ..]},
         {-FromDigits[StringDrop[#, 1]], 
          StringMatchQ[#, "-" ~~ DigitCharacter ..]}},
        Throw["Usage: please input a number"]
        ] &;
     If[EvenQ[fromNegativeDigits[#]], "Even", "Odd"]]] &;


(* Valid Tests *)

Print /@ evenOddMain /@ {"2", "5", "-14", "-27"};


(* Invalid Tests *)

evenOddMain[""]
evenOddMain["a"]
```

{% endraw %}

[Even Odd](https://sampleprograms.io/projects/even-odd) in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).