---
title: Selection Sort in Mathematica
layout: default
date: 2023-01-19
featured-image: selection-sort-in-every-language.jpg
last-modified: 2023-01-19

---

Welcome to the [Selection Sort](https://sampleprograms.io/projects/selection-sort) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* Implement by recursion.  Mathematica doesn't really have a sense of modifying things 'in place',
   so there isn't much value in trying to simulate it.  Instead, use Mathematica to focus on the algorithm itself: *)

selectionSort[{}] := {}
selectionSort[l_List] := Module[
  {i = First[Ordering[l, 1]]}, (* find the index of the lowest-valued element *)
  Join[ (* build a new list by *)
   Take[l, {i}],(* taking that lowest-valued element *)
   selectionSort[Drop[l, {i}]]]] (* and sorting the rest of the list *)

(* The outer function provides the 'user interface': *)

selectionSortMain = l \[Function]
   Module[{e = "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\""},
    Catch[
     StringRiffle[
      selectionSort @
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

Print /@ selectionSortMain /@ {
    "4, 5, 3, 1, 2",
    "4, 5, 3, 1, 4, 2",
    "1, 2, 3, 4, 5",
    "9, 8, 7, 6, 5, 4, 3, 2, 1"
    };


(* Invalid Tests *)

selectionSortMain[""]
selectionSortMain["1"]
selectionSortMain["4 5 3"]
```

{% endraw %}

[Selection Sort](https://sampleprograms.io/projects/selection-sort) in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).