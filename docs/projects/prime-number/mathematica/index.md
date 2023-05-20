---
title: Prime Number in Mathematica
layout: default
date: 2023-01-17
featured-image: prime-number-in-every-language.jpg
last-modified: 2023-01-17

---

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* This is provided by a Mathematica built-in PrimeQ.  Only a function to provide the 'user interface' is needed: *)

primeNumberMain = s \[Function] Module[
    {e = "Usage: please input a non-negative integer"},
    Catch[
     Replace[
      PrimeQ@
       (* convert string to integer, or throw *)
       If[StringMatchQ[s, DigitCharacter ..],
        FromDigits[s],
        Throw[e]],
      {False -> "Composite", True -> "Prime"}]]];


(* Valid Tests *)

Print /@ primeNumberMain /@ {
    "0",
    "1",
    "2",
    "4",
    "7",
    "4011",
    "3727"
    };


(* Invalid Tests *)

primeNumberMain[""]
primeNumberMain["a"]
palindromicNumberMain["6.7"]
palindromicNumberMain["-7"]
```

{% endraw %}

[Prime Number](https://sampleprograms.io/projects/prime-number) in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).