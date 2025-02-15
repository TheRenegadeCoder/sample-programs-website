---
authors:
- Ben Hekster
date: 2023-01-21
featured-image: job-sequencing-in-every-language.jpg
last-modified: 2023-01-21
layout: default
tags:
- job-sequencing
- mathematica
title: Job Sequencing in Mathematica
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/job-sequencing/mathematica/how-to-implement-the-solution.md
- sources/programs/job-sequencing/mathematica/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Job Sequencing](https://sampleprograms.io/projects/job-sequencing) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* The actual job scheduler which takes a Mathematica list of job tuples (value, deadline): *)

schedule = jobs \[Function] 
   Total[Part[(* sum the values of the scheduled jobs *)
     (* keep removing jobs until all the deadlines can be met *)
     FixedPoint[
      (* remove a single job *)
      l \[Function] Module[
        (* find the position 'i' of the first job that fails to meet its deadline *)
        {i = SelectFirst[Range[Length[l]], # > l[[#, 2]] &]},
        If[MissingQ[i],
         l,(* all deadlines are met *)
         (* else, delete the lowest-value job at or before that position 'i' *)
         Delete[l, First[MinimalBy[Range[i], l[[#, 1]] &]]]]],
      (* sort jobs by increasing deadline *)
      SortBy[jobs, job \[Function] job[[2]]]],
     All, 1]];

(* The outer function provides the 'user interface': *)

scheduleMain = Function[{values, deadlines},
   Module[{e = "Usage: please provide a list of profits and a list of deadlines"},
    Catch[
     schedule[
      Map[
       (* convert string to integer, or throw *)
       s \[Function] If[StringMatchQ[s, DigitCharacter ..],
         FromDigits[s],
         Throw[e]],
       (* construct argument to scheduler: list of job tuples *)
       Module[{
         vs = StringSplit[values, ", "],
         ds = StringSplit[deadlines, ", "]
         },
        If[Length[vs] == Length[ds] \[And] Length[vs] > 0, Transpose[{vs, ds}], Throw[e]]],
       {-1} (* at each leaf *)]]]]];


(* Valid Tests *)

Print /@ Apply[scheduleMain] /@ {
    {"25, 15, 10, 5", "3, 1, 2, 2"},
    {"20, 15, 10, 5, 1", "2, 2, 1, 3, 3"}
    };


(* Invalid Tests *)

scheduleMain["", ""]
scheduleMain["25, 15, 10, 5", ""]
scheduleMain["1, 2, 3, 4", "1, 2, 3, 4, 5"]

```

{% endraw %}

Job Sequencing in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).