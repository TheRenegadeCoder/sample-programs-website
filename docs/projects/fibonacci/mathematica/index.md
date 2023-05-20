---
title: Fibonacci in Mathematica
layout: default
date: 2023-01-19
featured-image: fibonacci-in-every-language.jpg
last-modified: 2023-01-19

---

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* It would be easy to simply print these out in a 'for' loop; however, in the spirit
of keeping the mathematical operation separate from the UI I opted to return
the Fibonacci sequence as a list explicitly: *)

fibonacciSequence[0] := {} (* special case *)
fibonacciSequence[1] := {1} (* special case *)
fibonacciSequence[n_] := Nest[Append[#, #[[-2]] + #[[-1]]] &, {1, 1}, n - 2]

(* The outer function provides the 'user interface': *)

fibonacciSequenceMain = Function[n,
   Catch[
    Module[{s},
     s = fibonacciSequence[
       (* convert string to integer, or throw *)
       If[StringMatchQ[n, DigitCharacter ..],
        FromDigits[n],
        Throw[
         "Usage: please input the count of fibonacci numbers to output"]]];
     Do[Print[i, ": ", s[[i]]], {i, Length[s]}]]]];


(* Valid Tests *)

fibonacciSequenceMain /@ {"1", "2", "5", "10"};


(* Invalid Tests *)

fibonacciSequenceMain[""]
fibonacciSequenceMain["word"]
```

{% endraw %}

[Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).