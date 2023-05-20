---
title: Transpose Matrix in Mathematica
layout: default
date: 2023-01-17
featured-image: transpose-matrix-in-every-language.jpg
last-modified: 2023-01-17

---

Welcome to the [Transpose Matrix](https://sampleprograms.io/projects/transpose-matrix) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* This is provided by the Mathematica built-in Transpose; so the only code needed is the 'user interface'
   to make it look a little more like a Unix command-line tool: *)

transposeMain = Function[{columns, rows, values},
   Module[{e = "Usage: please enter the dimension of the matrix and the serialized matrix"},
    Catch[
     StringRiffle[
      Flatten @*
        Transpose @*
        (* convert list of values and dimensions into matrix *)
        Function[{c, r, v},
         If[c*r == Length[v], Partition[v, c], Throw[e]]] @@
       Map[
        (* convert string to integer, or throw *)
        s \[Function] If[StringMatchQ[s, DigitCharacter ..],
          FromDigits[s],
          Throw[e]],
        (* construct three arguments to transpose: number of columns, rows, and list of values *)
        {columns, rows, StringSplit[If[StringLength[values] > 0, values, Throw[e]], ", "]},
        {-1} (* at each leaf *)],
      ", "]]]];


(* Valid Tests *)

Print /@ Apply[transposeMain] /@ {
    {"3", "2", "1, 2, 3, 4, 5, 6"}
    };


(* Invalid Tests *)

transposeMain["", "", "1, 2, 3, 4, 5, 6"]
transposeMain["3", "3", ""]
```

{% endraw %}

[Transpose Matrix](https://sampleprograms.io/projects/transpose-matrix) in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).