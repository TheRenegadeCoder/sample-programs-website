---
authors:
- Ben Hekster
date: 2023-01-18
featured-image: convex-hull-in-every-language.jpg
last-modified: 2023-01-18
layout: default
tags:
- convex-hull
- mathematica
title: Convex Hull in Mathematica
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/convex-hull/mathematica/how-to-implement-the-solution.md
- sources/programs/convex-hull/mathematica/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Convex Hull](https://sampleprograms.io/projects/convex-hull) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* Convex hull option convexHull1 is based on the built-in ConvexHullMesh: *)

convexHull1 = Function[{ps},
   Module[{mesh = ConvexHullMesh[ps]},
    Round /@ Part[
      MeshCoordinates[mesh],
       First[First[MeshCells[mesh, 2]]]]]];

(* If that is considered cheating, then option convexHull2 implements it directly using Jarvis' algorithm: *)

convexHull2 = Function[{inputList},
   Module[{orientation, l = inputList, i, j},
    (* compute the direction in which three vertices are oriented *)
    orientation = Function[{a, b, c}, Det[{a - b, c - b}]];
    
    (* keep sorting the convex hull vertices to the beginning of the list;
    'i' is the index of the last vertex in the convex hull;
    'j' is the index of the next vertex selected to be permuted to the front *)
    For[
     (* initially *)
     i = 0; (* no vertices selected into the convex hull *)
     j = First[OrderingBy[l, First, 1]], (* find the first vertex by minimum x-coordinate *)
     
     (* continue as long as the next selected vertex is not already in the convex hull *)
     j > i,
     
     (* iteration done in the body *),
     
     (* permute the next selected vertex to the front of the list *)
     i++;
     l = Permute[l, If[i != j, Cycles[{{i, j}}], {}]];
     
     (* find the next vertex that is clockwise to all other vertices *)
     
     j = Mod[i + 1, Length[l], 1];
     Do[ (* for all vertices *)
      (* if 'k' is such that 'i', 'j', 'k' are counterclockwise, let 'k' become the new 'j' *)
      If[orientation @@ l[[{i, j, k}]] > 0, j = k],
      {k, Length[l]}];
     ];
    (* return only the front part of the list containing the convex hull *)
    Take[l, i]]];

(* The outer function provides the 'user interface' (e.g., the string parsing): *)

convexHullMain = Function[{lx, ly},
   Module[{e = "Usage: please provide at least 3 x and y coordinates as separate lists (e.g. \"100, 440, 210\")"},
    Catch[
     convexHull2[
      Transpose[
       If[MatrixQ[#] \[And] Length[First[#]] >= 3,
          #, Throw[e]] &[
        Map[
         (* convert string to integer, or throw *)
         s \[Function] If[StringMatchQ[s, DigitCharacter ..],
           FromDigits[s],
           Throw[e]],
         (* construct two arguments to convexHull: list of x coordinates, list of y coordinates *)
         {StringSplit[lx, ", "], StringSplit[ly, ", "]},
         {-1} (* at each leaf *)]]]]]]];


(* Valid Tests *)

Print /@ Apply[convexHullMain] /@ {
    {"100, 180, 240", "220, 120, 20"},
    {"100, 140, 320, 480, 280", "240, 60, 40, 200, 300"},
    {"260, 280, 300, 320, 600, 360, 20, 240", 
     "160, 100, 180, 140, 160, 320, 200, 0"}
    };


(* Invalid Tests *)

convexHullMain["100, 180", "240, 60, 40, 200, 300"]
convexHullMain["100, 180, 240", "240, 60, 40, 200, 300"]
convexHullMain["100, 180, 240", ""]
convexHullMain["100, 1A0, 240", "220, 120, 20"]

```

{% endraw %}

Convex Hull in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).