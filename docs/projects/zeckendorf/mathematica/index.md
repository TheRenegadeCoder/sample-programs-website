---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-04-30
featured-image: zeckendorf-in-every-language.png
last-modified: 2026-04-30
layout: default
tags:
- mathematica
- zeckendorf
title: Zeckendorf in Mathematica
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/zeckendorf/mathematica/how-to-implement-the-solution.md
- sources/programs/zeckendorf/mathematica/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Zeckendorf](https://sampleprograms.io/projects/zeckendorf) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
ClearAll[zeckendorfMain, nf, zeckendorf];

nf[n_] := Fibonacci @ Floor @ Log[GoldenRatio, n * Sqrt[5] + 1/2];
zeckendorf[n_Integer?Positive] := -Differences[NestWhileList[# - nf[#] &, n, # != 0 &]];

$usage = "Usage: please input a non-negative integer";

zeckendorfMain[s_String /; StringMatchQ[s, DigitCharacter ..]] := 
  With[{n = FromDigits[s]},
    Which[
      n == 0, "",
      n > 0, StringRiffle[ToString /@ zeckendorf[n], ", "]
    ]
  ];

zeckendorfMain[___] := $usage;

Print /@ zeckendorfMain /@ {
    (* Valid cases *)
    "0",
    "55",
    "67",
    "10946",
    "16383",

    (* Invalid cases*)
    "",
    "-2",
    "2.6",
    "bad"
};

Print[zeckendorfMain[]]
```

{% endraw %}

Zeckendorf in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).