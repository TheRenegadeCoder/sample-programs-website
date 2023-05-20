---
title: Maximum Subarray in Mathematica
layout: default
date: 2023-01-20
featured-image: maximum-subarray-in-every-language.jpg
last-modified: 2023-01-20

---

Welcome to the [Maximum Subarray](https://sampleprograms.io/projects/maximum-subarray) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* The actual maximum subarray operating on Mathematica lists, using essentially Kadane's algorithm: *)

maximumSubarray = a \[Function] Max[
    FoldList[
     Max[#2 (* A[i] *) , #2 + #1 (* A[i] + local-maximum *)] &,
     a]];

(* The outer function provides the 'user interface': *)

maximumSubarrayMain = l \[Function] Catch[
    Module[{e = "Usage: Please provide a list of integers in the format: \"1, 2, 3, 4, 5\"",
      fromNegativeDigits},
     (* oddly, Mathematica doesn't appear to provide a function which can parse strings representing negative integers *)
     fromNegativeDigits = Piecewise[{
         {FromDigits[#], StringMatchQ[#, DigitCharacter ..]},
         {-FromDigits[StringDrop[#, 1]], 
          StringMatchQ[#, "-" ~~ DigitCharacter ..]}},
        Throw[e]] &;
     maximumSubarray @ Map[
       (* convert string to integer, or throw *)
       fromNegativeDigits,
       (* construct arguments to maximum subarray *)
       StringSplit[If[StringLength[l] > 0, l, Throw[e]], ", "],
       {-1} (* at each leaf *)]]];


(* Valid Tests *)

Print /@ maximumSubarrayMain /@ {
    "1, 2, 3",
    "-1, -2, -3",
    "-2, -1, 3, 4, 5",
    "-1, -4, 2, 3, -3, -4, 9",
    "-1, -4, 2, 9, -3, -4, 9"
    };


(* Invalid Tests *)

maximumSubarrayMain[""]
```

{% endraw %}

[Maximum Subarray](https://sampleprograms.io/projects/maximum-subarray) in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Feb 06 2023 19:40:54. The solution was first committed on Jan 20 2023 09:27:27. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).