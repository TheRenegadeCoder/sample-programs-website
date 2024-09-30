---
authors:
- Ben Hekster
date: 2023-01-21
featured-image: factorial-in-every-language.jpg
last-modified: 2023-01-21
layout: default
tags:
- factorial
- mathematica
title: Factorial in Mathematica
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/mathematica/how-to-implement-the-solution.md
- sources/programs/factorial/mathematica/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* The Mathematica built-in Factorial essentially provides the required behavior;
so the only code needed is the 'user interface' to make it look a little more
like a Unix command-line tool: *)

factorialMain = Catch[
    (* convert string to integer, or throw *)
    If[
     StringMatchQ[#, DigitCharacter ..],
     FromDigits[#]!,
     Throw["Usage: please input a non-negative integer"]]] &;


(* Valid Tests *)

Print /@ factorialMain /@ {"0", "1", "4", "8", "10"};

(* Note that Mathematica (as far as I know) doesn't impose an upper limit on computations: *)
factorialMain["10000"]


(* Invalid Tests *)

factorialMain[""]
factorialMain["asdf"]
factorialMain["-1"]

```

{% endraw %}

Factorial in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).