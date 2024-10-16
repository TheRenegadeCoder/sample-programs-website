---
authors:
- Ben Hekster
date: 2023-01-19
featured-image: quick-sort-in-every-language.jpg
last-modified: 2023-01-19
layout: default
tags:
- mathematica
- quick-sort
title: Quick Sort in Mathematica
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/quick-sort/mathematica/how-to-implement-the-solution.md
- sources/programs/quick-sort/mathematica/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Quick Sort](https://sampleprograms.io/projects/quick-sort) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* To me, some confusion arises from whether the pivot is a value or
an element-- it should be the former, which emphasizes that the pivot value
can occur multiply.  Since we can simultaneously compare for strict inequality
(less than/greater than) and loose inequality (less than or equal/greater than
or equal) we may take advantage of that and not lose that information: this
implies that we should sort pivot values explicitly, into a middle compartment.
Since the pivot values will then already be at the correct position, they
will never undergo resorting.  Also, note that a 'swap' is actually 3 copies
(including the temporary variable); in general, a permutation over an n-cycle
requires n+1 copies, so permutations over 3-cycles move 3 elements more
efficiently at the cost of 4/3 of a swap. *)

(* The partitioning is like Hoare in that it is bidirectional from both ends
until pointers cross.  It is different in that the invariant always keeps
pivot elements on the towards-center side, so that at completion all pivot
elements are found in the center.  The algorithm performs like Hoare in that
it performs no swaps on lists that are already sorted and lists containing
equal elements.  In addition, it excludes all pivot elements from recursive
consideration.  It performs better than Sedgewick by not swapping pivots
that are already at the correct location, and handles the case when the
pivot value occurs multiple times. *)

quicksort = list \[Function]
   If[Length[list] > 1,
    Module[
     {v = list,
      p = list[[Ceiling[Length[list]/2]]], (* choose a pivot value *)
      i = 1, l = 1, j = Length[list], h = Length[list]},
     (* until both ends of the partition meet *)
     While[i <= j,
      (* grow the left side of the partition until a strictly larger element is found *)
      While[i <= j,
       Switch[v[[i]] - p,(* simultaneously compare loose and strict equality against the pivot *)
        (* move strictly lower elements before any accumulated pivot elements *)
         c_ /; c < 0, If[i > l, v = Permute[v, Cycles[{{l, i}}]]]; l++,
        
        (* leave pivot elements at the toward-middle end of the left side *)
         0, Null,
        
        (* stop if we find an element strictly greater than the pivot *)
         _, Break[]];
       i++];
      
      (* mutatis mutandis for the right side of the partition *)
      While[j >= i,
       Switch[v[[j]] - p,
         c_ /; c > 0, If[j < h, v = Permute[v, Cycles[{{h, j}}]]]; h--,
         0, Null,
         _, Break[]];
       j--];
      
      (* pointers have not crossed yet? 
      Then we have a strictly lower and strictly higher element both on the wrong sides of the partition *)
      If[i < j,
       If[i == l \[And] j == h, v = Permute[v, Cycles[{{i, j}}]]];
       If[i > l \[And] j == h, v = Permute[v, Cycles[{{j, l, i}}]]];
       If[i == l \[And] j < h, v = Permute[v, Cycles[{{i, h, j}}]]];
       If[i > l \[And] j < h, v = Permute[v, Cycles[{{i, h}, {j, l}}]]];
       i++; l++; j--; h--]];
     
     (* recurse *)
     Join[
      If[l > 1, quicksort[v[[;; l - 1]]], {}],
      If[h >= l, v[[l ;; h]], {}],
      If[h < Length[list], quicksort[v[[h + 1 ;;]]], {}]]],
    list];

(* The outer function provides the 'user interface': *)

quicksortMain = l \[Function]
   Module[{e = "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\""},
    Catch[
     StringRiffle[
      quicksort @
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

Print /@ quicksortMain /@ {
    "4, 5, 3, 1, 2",
    "4, 5, 3, 1, 4, 2",
    "1, 2, 3, 4, 5",
    "9, 8, 7, 6, 5, 4, 3, 2, 1"
    };


(* Invalid Tests *)

quicksortMain[""]
quicksortMain["1"]
quicksortMain["4 5 3"]

```

{% endraw %}

Quick Sort in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).