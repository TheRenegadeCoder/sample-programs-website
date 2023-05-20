---
title: Depth First Search in Mathematica
layout: default
date: 2023-01-21
featured-image: depth-first-search-in-every-language.jpg
last-modified: 2023-01-21

---

Welcome to the [Depth First Search](https://sampleprograms.io/projects/depth-first-search) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* Depth-first search option depthFirstSearch1 is based on the built-in DepthFirstScan: *)

depthFirstSearch1 = Function[{ag, p, v},
   Module[{found = False},
    DepthFirstScan[
     AdjacencyGraph[p, ag],
     "PrevisitVertex" -> Function[{u}, If[u == v, found = True]]
     ];
    found]];

(* If that is considered cheating, then option depthFirstSearch2 implements it directly: *)

depthFirstSearch2 = Function[{ag, p, v},
   Module[{f},
    f = Function[i,
      p[[i]] == v \[Or] AnyTrue[
        Select[Range[i, Length[ag]], Positive[ag][[i, #]] &],
        f]];
    f[1] (* start search at first node *) ]];

(* The outer function does the string parsing: *)

depthFirstSearchMain = Function[{am, vs, v},
   Module[{e = "Usage: please provide a tree in an adjacency matrix form (\"0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, \
0\") together with a list of vertex values (\"1, 3, 5, 2, 4\") and the integer to find (\"4\")"},
    Catch[
     depthFirstSearch2 @@
      Map[
       (* convert string to integer, or throw *)
       s \[Function] If[StringMatchQ[s, DigitCharacter ..],
         FromDigits[s],
         Throw[e]],
       (* construct arguments to depth-first search *) {
        If[Length[#] > 0, Partition[#, Sqrt[Length[#]]], Throw[e]] &[StringSplit[am, ", "]],
        If[Length[#] > 0, #, Throw[e]] &[StringSplit[vs, ", "]],
        If[StringLength[v] > 0, v, Throw[e]]},
       {-1} (* at each leaf *)]]]];


(* Valid Tests *)

Print /@ Apply[depthFirstSearchMain] /@ {
    {"0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0", "1, 3, 5, 2, 4", "1"},
    {"0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0", "1, 3, 5, 2, 4", "4"},
    {"0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0", "1, 3, 5, 2, 4", "5"},
    {"0", "1", "1"},
    {"0", "1", "6"},
    {"0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0", "1, 3, 5, 2, 4", "7"}
    };


(* Invalid Tests *)

depthFirstSearchMain["", "1, 3, 5, 2, 4", "4"]
depthFirstSearchMain["0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0", "", "1"]
depthFirstSearchMain["0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0", "1, 3, 5, 2, 4", ""]
```

{% endraw %}

[Depth First Search](https://sampleprograms.io/projects/depth-first-search) in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).