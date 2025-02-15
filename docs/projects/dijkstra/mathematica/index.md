---
authors:
- Ben Hekster
date: 2023-01-21
featured-image: dijkstra-in-every-language.jpg
last-modified: 2023-01-21
layout: default
tags:
- dijkstra
- mathematica
title: Dijkstra in Mathematica
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/dijkstra/mathematica/how-to-implement-the-solution.md
- sources/programs/dijkstra/mathematica/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Dijkstra](https://sampleprograms.io/projects/dijkstra) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* This is easy to do using Mathematica graph operations: *)

dijkstra = Function[{am, from, to},
   (* sum the edge weights *)
   Total @  Module[
     {g = WeightedAdjacencyGraph[am /. 0 -> \[Infinity] (* needed to indicate no edge *)]},
     PropertyValue[{ (* find the edge weights *)
       g,
       (* convert the list of path vertices into a list of edges *)
       Apply[UndirectedEdge] /@ Partition[
         (* find shortest path (cheating!) *)
         FindShortestPath[g, from, to, Method -> "Dijkstra"],
         2, 1]},
      EdgeWeight]]];

(* The outer function provides the 'user interface': *)

dijkstraMain = Function[{values, from, to},
   Module[{e = "Usage: please provide three inputs: a serialized matrix, a source node and a destination node"},
    Catch[
     Apply[
       Function[{v, f, t},
        Module[{l = Sqrt[Length[v]], w},
         w = dijkstra[
           Partition[v,(* convert to square matrix *)
            (* compute square dimension *)
            If[IntegerQ[l], l, Throw[e]]],
           If[f < l, 1 + f, Throw[e]],(* Mathematica indices are 1-based *)
           If[t < l, 1 + t, Throw[e]]];
         (* Specifically detect the case where no path was found; 
         note that FindShortestPath just returns zero in this case, 
         which it would also do if the source and destination vertices are the same. *)
         If[w == 0 \[And] f != t, Throw[e], w]]]]@
      Map[
       (* convert string to integer, or throw *)
       s \[Function] If[StringMatchQ[s, DigitCharacter ..],
         FromDigits[s],
         Throw[e]],
       (* construct arguments: list of weights, source node, destination node *)
       {
        StringSplit[If[StringLength[values] > 0, values, Throw[e]], ", "],
        from, to
        },
       {-1} (* at each leaf *)]]]];

(* Valid Tests *)

Print /@ Apply[dijkstraMain] /@ {
    {"0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0", "0", "1"}
    };


(* Invalid Tests *)

dijkstraMain["1, 0, 3, 0, 5, 1", "1", "2"]
dijkstraMain["0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0", "0", ""]
dijkstraMain["0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0", "", ""]
dijkstraMain["0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0", "-1", "2"]
dijkstraMain["0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0", "1", "-2"]
dijkstraMain["0, 2, 0, -6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, -6, 8, 0, 0, 9, 0, 5, 7, 9, 0", "1", "2"]
dijkstraMain["0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0", "1", "10"]
dijkstraMain["0, 0, 0, 0", "0", "1"]

```

{% endraw %}

Dijkstra in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).