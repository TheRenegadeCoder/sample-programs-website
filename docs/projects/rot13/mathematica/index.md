---
title: Rot13 in Mathematica
layout: default
date: 2023-01-16
featured-image: rot13-in-every-language.jpg
last-modified: 2023-01-16

---

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

(* The actual rotation operating on Mathematica strings: *)

rot13 = s \[Function] StringJoin @@ Function[{c},
      FromCharacterCode @
       Piecewise[(* operate piecewise on the domain of ASCII character codes *)
        Append[{
            Mod[c + 13, 26, First@ToCharacterCode[StringTake[#, 1]]],
            Between[c, ToCharacterCode[#]]} & /@
          {"az", "AZ"},(* specific character intervals to operate on *)
         {c, True}] (* default does nothing *)
        ]] /@ ToCharacterCode[s];

(* The outer function provides the 'user interface': *)

rot13Main = s \[Function]
   Catch[
    rot13[
     If[
      StringQ[s] \[And] \[Not] StringMatchQ[s, ""],
      s,
      Throw["Usage: please provide a string to encrypt"]]]];


(* Valid Tests *)

Print /@ rot13Main /@ {
    "the quick brown fox jumped over the lazy dog",
    "THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG",
    "The quick brown fox jumped. Was it over the lazy dog?"
    };


(* Invalid Tests *)

rot13Main[""]
```

{% endraw %}

[Rot13](https://sampleprograms.io/projects/rot13) in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).