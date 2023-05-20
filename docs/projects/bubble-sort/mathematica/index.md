---
title: Bubble Sort in Mathematica
layout: default
date: 2023-01-19
featured-image: bubble-sort-in-every-language.jpg
last-modified: 2023-01-19

---

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* The actual bubble sort operating on Mathematica lists: *)

(* keep making passes over the list until it stops changing *)
bubbleSort = Function[{l},
   FixedPoint[Function[{l},
     (* pass over a pair of elements in the list *)
     Fold[Function[{l, i},
       (* element pair is out of order?*)
       If[l[[i]] > l[[i + 1]],
        (* swap the two elements *)
        Permute[l, Cycles[{{i, i + 1}}]],
        l]],
      l, (* begin with the list in its original state *)
      Range[Length[l] - 1]]],(* over each pair of elements *)
    l]];

(* The outer function provides the 'user interface': *)

bubbleSortMain = l \[Function]
   Module[{e = 
      "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\""},
    Catch[
     StringRiffle[
      bubbleSort@
         (* list must have more than one element *)
         If[Length[#] > 1, #, Throw[e]] & @
       Map[
        (* convert string to integer, or throw *)
        s \[Function] If[StringMatchQ[s, DigitCharacter ..],
          FromDigits[s],
          Throw[e]],
        (* construct arguments to bubble sort: list of items *)
        StringSplit[l, ", "],
        {-1} (* at each leaf *)],
      ", "]]];


(* Valid Tests *)
Print /@ bubbleSortMain /@ {
    "4, 5, 3, 1, 2",
    "4, 5, 3, 1, 4, 2",
     "1, 2, 3, 4, 5",
    "9, 8, 7, 6, 5, 4, 3, 2, 1" 
    };


(* Invalid Tests *)
bubbleSortMain[""]
```

{% endraw %}

[Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).