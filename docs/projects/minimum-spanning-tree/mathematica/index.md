---
title: Minimum Spanning Tree in Mathematica
layout: default
date: 2023-01-18
featured-image: minimum-spanning-tree-in-every-language.jpg
last-modified: 2023-01-18

---

Welcome to the [Minimum Spanning Tree](https://sampleprograms.io/projects/minimum-spanning-tree) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* This is easy to do using Mathematica graph operations: *)

minimumSpanningTreeWeight = am \[Function] Module[
    {g = WeightedAdjacencyGraph[am /. 0 -> \[Infinity] (* needed to indicate no edge *)]},
    Total[PropertyValue[
      {g, EdgeList[FindSpanningTree[g, Method -> "Prim"]]},
      EdgeWeight]]];

(* The outer function provides the 'user interface': *)

minimumSpanningTreeWeightMain = l \[Function]
   Module[{e = "Usage: please provide a comma-separated list of integers"},
    Catch[
     minimumSpanningTreeWeight@
        (* convert to square matrix *)
        Partition[#,
         (* compute square dimension *)
         Module[{l = Sqrt[Length[#]]}, 
          If[IntegerQ[l], l, Throw[e]]]] & @
      Map[
       (* convert string to integer, or throw *)
       s \[Function] If[StringMatchQ[s, DigitCharacter ..],
         FromDigits[s],
         Throw[e]],
       (* construct arguments to spanning tree: 
       weighted adjacency matrix *)
       StringSplit[If[StringLength[l] > 0, l, Throw[e]], ", "],
       {-1} (* at each leaf *)]]];


(* Valid Tests *)

minimumSpanningTreeWeightMain["0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0"]


(* Invalid Tests *)

minimumSpanningTreeWeightMain[""]
minimumSpanningTreeWeightMain["1, 0, 3, 0, 5, 1"]
```

{% endraw %}

[Minimum Spanning Tree](https://sampleprograms.io/projects/minimum-spanning-tree) in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).