---
title: Capitalize in Mathematica
layout: default
date: 2023-01-16
featured-image: capitalize-in-every-language.jpg
last-modified: 2023-01-16

---

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* The actual capitalization operating on Mathematica strings: *)

capitalize = StringReplace[
   StartOfString ~~ l : LetterCharacter  -> ToUpperCase[l]];

(* The outer function provides the 'user interface': *)

capitalizeMain = s \[Function]
   Catch[
    capitalize[
     If[
      StringQ[s] \[And] \[Not] StringMatchQ[s, ""],
      s,
      Throw["Usage: please provide a string"]]]];


(* Valid Tests *)
Print /@ capitalizeMain /@ {
    "hello",
    "Hello",
    "hello world",
    "heLLo World",
    "12345"
    };


(* Invalid Tests *)
capitalizeMain[""]
```

{% endraw %}

[Capitalize](https://sampleprograms.io/projects/capitalize) in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).