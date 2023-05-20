---
title: Longest Word in Mathematica
layout: default
date: 2023-01-16
featured-image: longest-word-in-every-language.jpg
last-modified: 2023-01-16

---

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* Trivial: *)

longestWord = s \[Function] Max @@ StringLength /@ StringSplit[s];

(* The outer function provides the 'user interface' (e.g., the string parsing): *)

longestWordMain = Function[{s},
   Module[{e = "Usage: please provide a string"},
    Catch[
     longestWord @
      If[StringLength[s] > 0, s, Throw[e]]]]];


(* Valid Tests *)

Print /@ longestWord /@ {
    "May the force be with you",
    "Floccinaucinihilipilification",
    "Hi,\nMy name is Paul!"
    };


(* Invalid Tests *)

longestWordMain[""]
```

{% endraw %}

[Longest Word](https://sampleprograms.io/projects/longest-word) in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).