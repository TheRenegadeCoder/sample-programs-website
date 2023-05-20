---
title: Roman Numeral in Mathematica
layout: default
date: 2023-01-16
featured-image: roman-numeral-in-every-language.jpg
last-modified: 2023-01-16

---

Welcome to the [Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* The actual Roman numeral converter operating on Mathematica strings: *)

romanNumerals = s \[Function] Fold[
    (* conversion operating on pairs of subsequent values*)
    Function[{a, ii}, If[GreaterEqual @@ ii, a + First[ii], a - First[ii]]],
    0,
    Partition[(* pairs of subsequent values*)
     Append[ (* append zero so the last value still forms a pair *)
      ReplaceAll[Characters[s], (* convert to list of decimal values *)
       {"I" -> 1, "V" -> 5, "X" -> 10, "L" -> 50, "C" -> 100, "D" -> 500, "M" -> 1000}],
      0],
     2, 1]];

(* The outer function provides the 'user interface': *)

romanNumeralsMain = s \[Function]
   Catch[
    romanNumerals[
     If[
      StringQ[s] \[And] StringMatchQ[s, ("I" | "V" | "X" | "L" | "C" | "D" | "M") ...],
      s,
      Throw["Error: invalid string of roman numerals"]]]];


(* Valid Tests *)

Print /@ romanNumeralsMain /@ {
    "", "I", "V", "X", "L", "C", "D", "M", "XXV", "XIV"
    };


(* Invalid Tests *)

romanNumeralsMain["XT"]
```

{% endraw %}

[Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).