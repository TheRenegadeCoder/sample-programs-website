---
title: Linear Search in Mathematica
layout: default
date: 2023-01-18
featured-image: linear-search-in-every-language.jpg
last-modified: 2023-01-18

---

Welcome to the [Linear Search](https://sampleprograms.io/projects/linear-search) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* This is simply the 'FirstCase' built-in.  Only an outer function is needed to provide the 'user interface': *)

linearSearchMain = Function[{list, value},
   Module[{e = "Usage: please provide a list of integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")"},
    Catch[
     Replace[
      FirstCase @@ Map[
        (* convert string to integer, or throw *)
        s \[Function] If[StringMatchQ[s, DigitCharacter ..],
          FromDigits[s],
          Throw[e]],
        (* construct arguments to FirstCase: list of items and value to search *)
        {StringSplit[If[list != "", list, Throw[e]], ", "], value},
        {-1} (* at each leaf *)],
      {_Missing -> "false", _ -> "true"}]]]];


(* Valid Tests *)

Print /@ Apply[linearSearchMain] /@ {
    {"1, 3, 5, 7", "1"},
    {"1, 3, 5, 7", "7"},
    {"1, 3, 5, 7", "5"},
    {"5", "5"},
    {"5", "7"},
    {"1, 3, 5, 6", "7"}
    };


(* Invalid Tests *)

linearSearchMain["1, 2, 3, 4", ""]
linearSearchMain["", "5"]
```

{% endraw %}

[Linear Search](https://sampleprograms.io/projects/linear-search) in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).