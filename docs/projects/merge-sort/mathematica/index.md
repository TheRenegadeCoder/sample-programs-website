---
authors:
- Ben Hekster
date: 2023-01-19
featured-image: merge-sort-in-every-language.jpg
last-modified: 2023-01-19
layout: default
tags:
- mathematica
- merge-sort
title: Merge Sort in Mathematica
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/merge-sort/mathematica/how-to-implement-the-solution.md
- sources/programs/merge-sort/mathematica/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Merge Sort](https://sampleprograms.io/projects/merge-sort) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* The function takes a Mathematica list of unsorted nonnegative integers: *)

mergeSort = list \[Function]
   (* merge two sorted components *)
   Apply[Function[{l, r},
     First[ (* just the merged list *)
      NestWhile[
       (* merge one element from either the left or right list into output *)
       Apply[Function[{m, l, r},
         If[ (* use the first element of the left list if *)
          (* the right list is empty, or the left list has elements and compares before the right *)
          Length[r] == 0 \[Or] (Length[l] > 0 \[And] First[l] < First[r]),
          {Append[m, First[l]], Rest[l], r},
          {Append[m, First[r]], l, Rest[r]}]]],
       
       (* begin with just the two components *)
       {{} (* will be the merged list *), l, r},
       
       (* while there are still elements in either the left or right list *)
       Apply[Function[{m, l, r}, Length[l] > 0 \[Or] Length[r] > 0]]]]],
    
    (* for each partition component, sort recursively until it contains no more than one element *)
    If[Length[#] <= 1, #, mergeSort[#]] & /@ (
      (* partition the list approximately halfway *)
      #[list, Floor[Length[list]/2]] & /@ {Take, Drop})];

(* The outer function provides the 'user interface': *)

mergeSortMain = l \[Function]
   Module[{e = "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\""},
    Catch[
     StringRiffle[
      mergeSort @
         (* list must have more than one element *)
         If[Length[#] > 1, #, Throw[e]] & @
       Map[
        (* convert string to integer, or throw *)
        s \[Function] If[StringMatchQ[s, DigitCharacter ..],
          FromDigits[s],
          Throw[e]],
        (* construct arguments to merge sort: list of items *)
        StringSplit[l, ", "],
        {-1} (* at each leaf *)],
      ", "]]];


(* Valid Tests *)

Print /@ mergeSortMain /@ {
    "4, 5, 3, 1, 2",
    "4, 5, 3, 1, 4, 2",
    "1, 2, 3, 4, 5",
    "9, 8, 7, 6, 5, 4, 3, 2, 1"
    };


(* Invalid Tests *)

mergeSortMain[""]
mergeSortMain["1"]
mergeSortMain["4 5 3"]

```

{% endraw %}

Merge Sort in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).