---
title: Josephus Problem in Mathematica
layout: default
date: 2023-01-20
featured-image: josephus-problem-in-every-language.jpg
last-modified: 2023-01-20

---

Welcome to the [Josephus Problem](https://sampleprograms.io/projects/josephus-problem) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* The code is trivial: *)

josephus[1, _] := 1
josephus[n_Integer, k_Integer] := Mod[josephus[n - 1, k] + (k - 1), n] + 1

(* The outer function provides the 'user interface': *)

josephusMain = Function[{people, skip},
   Catch[
    Module[{e = "Usage: please input the total number of people and number of people to skip."},
     josephus @@ Map[
       (* convert string to integer, or throw *)
       s \[Function] If[StringMatchQ[s, DigitCharacter ..],
         Module[{v = FromDigits[s]},
          If[Positive[v], v, Throw[e]]],(* make sure both numbers are positive *)
         Throw[e]],
       {people, skip}]]]];


(* Valid Tests *)

Print /@ Apply[josephusMain] /@ {
    {"5", "2"},
    {"7", "3"},
    {"41", "4"}
    };


(* Invalid Tests *)

josephusMain["", ""]
josephusMain["word", "word"]
josephusMain["0", "1"]
```

{% endraw %}

[Josephus Problem](https://sampleprograms.io/projects/josephus-problem) in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).