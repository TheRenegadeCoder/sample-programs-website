---
title: Insertion Sort in Mathematica
layout: default
date: 2023-01-21
featured-image: insertion-sort-in-every-language.jpg
last-modified: 2023-01-21

---

Welcome to the [Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* The actual insertion sort which takes and returns a Mathematica list is easy: *)

insertionSort = l \[Function] NestWhile[
    (* insert a single element *)
    Module[{li = Length[#] + 1},
      Insert[
       #, (* sorted list so far *)
       l[[li]],(* next element to insert *)
       First[FirstPosition[#, (* at what index to insert it *)
         v_ /; v > l[[li]], (* element that is greater than the element to insert *)
         {li},(* or else insert at end *)
         {1}, Heads -> False](* only look at list elements *)]]] &,
    
    (* start with an empty sorted list *)
    {},
    
    (* while there are still elements left to insert into the sorted list *)
    Length[#] < Length[l] &];

(* The outer function provides the 'user interface': *)

insertionSortMain = Function[{l},
   Module[{e = "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\""},
    Catch[
     StringRiffle[(* format output as required *)
      insertionSort @@ Map[
        (* convert string to integer, or throw *)
        s \[Function] If[StringMatchQ[s, DigitCharacter ..],
          FromDigits[s],
          Throw[e]],
        (* construct arguments to insertion sort: list of items *)
        {If[Length[#] > 1, #, Throw[e]] &[StringSplit[l, ", "]]},
        {-1} (* at each leaf *)],
      ", "]]]];


(* Valid Tests *)

Print /@ insertionSortMain /@ {
    "4, 5, 3, 1, 2",
    "4, 5, 3, 1, 4, 2",
    "1, 2, 3, 4, 5",
    "9, 8, 7, 6, 5, 4, 3, 2, 1"
    };


(* Invalid Tests *)

insertionSortMain[""]
insertionSortMain["1"]
insertionSortMain["4 5 3"]
```

{% endraw %}

[Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).