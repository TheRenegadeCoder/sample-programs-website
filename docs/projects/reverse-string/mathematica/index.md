---
authors:
- Ben Hekster
date: 2023-01-16
featured-image: reverse-string-in-every-language.jpg
last-modified: 2023-01-16
layout: default
tags:
- mathematica
- reverse-string
title: Reverse String in Mathematica
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/mathematica/how-to-implement-the-solution.md
- sources/programs/reverse-string/mathematica/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* The actual function operating on Mathematica strings is just the built-in StringReverse.  An outer function provides the 'user interface': *)

stringReverseMain = Function[{s},
   Catch[
    StringReverse[
     If[
      StringQ[s] \[And] \[Not] StringMatchQ[s, ""],
      s,
      Throw["Usage: please provide a string"]]]]];


(* Valid Tests *)

Print /@ stringReverseMain /@ {
    "Hello, World"
    };


(* Invalid Tests *)

stringReverseMain[""]

```

{% endraw %}

Reverse String in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).