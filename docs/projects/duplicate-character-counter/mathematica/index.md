---
title: Duplicate Character Counter in Mathematica
layout: default
date: 2023-01-21
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2023-01-21

---

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* The inner function does the work, returning the output as a Mathematica list: *)

duplicateCharacterCounter = Function[{s},
   Select[
    {First[#], Length[#]} & /@ Gather[Characters[s]],
    #[[2]] > 1 &]];

(* The outer function performs the output text formatting: *)

duplicateCharacterCounterMain = s \[Function]
   Print[#[[1]], ": ", #[[2]]] & /@ duplicateCharacterCounter[s];


(* Valid Tests *)

duplicateCharacterCounterMain /@ {
   "goodbyeblues",
   "abba",
   "aAbB"
   };


(* Invalid Tests *)
```

{% endraw %}

[Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).