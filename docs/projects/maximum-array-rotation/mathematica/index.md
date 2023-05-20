---
title: Maximum Array Rotation in Mathematica
layout: default
date: 2023-01-19
featured-image: maximum-array-rotation-in-every-language.jpg
last-modified: 2023-01-19

---

Welcome to the [Maximum Array Rotation](https://sampleprograms.io/projects/maximum-array-rotation) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* The actual maximum array rotation operating on Mathematica lists: *)

longestArrayRotation = a \[Function] Max @@
    Table[
     Dot[ (* inner product *)
      RotateRight[a, i], (* rotated input list *)
      Range[0, Length[a] - 1](* list of weights *)],
     {i, Length[a]}];

(* The outer function provides the 'user interface': *)

longestArrayRotationMain = l \[Function]
   Module[{e = "Usage: please provide a list of integers (e.g. \"8, 3, 1, 2\")"},
    Catch[
     longestArrayRotation @@ Map[
       (* convert string to integer, or throw *)
       s \[Function] If[StringMatchQ[s, DigitCharacter ..],
         FromDigits[s],
         Throw[e]],
       (* construct argument to array rotation *)
       {StringSplit[If[StringLength[l] > 0, l, Throw[e]], ", "]},
       {-1} (* at each leaf *)]]];


(* Valid Tests *)

Print /@ longestArrayRotationMain /@ {
    "3, 1, 2, 8",
    "1, 2, 8, 3",
    "8, 3, 1, 2"
    };


(* Invalid Tests *)

longestArrayRotationMain[""]
```

{% endraw %}

[Maximum Array Rotation](https://sampleprograms.io/projects/maximum-array-rotation) in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).