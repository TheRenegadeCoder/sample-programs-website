---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-30
featured-image: sleep-sort-in-every-language.jpg
last-modified: 2026-04-30
layout: default
tags:
- mathematica
- sleep-sort
title: Sleep Sort in Mathematica
title1: Sleep Sort in
title2: Mathematica
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/sleep-sort/mathematica/how-to-implement-the-solution.md
- sources/programs/sleep-sort/mathematica/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Sleep Sort](https://sampleprograms.io/projects/sleep-sort) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
ClearAll[sleepSortMain, sleepSort];

sleepSort[l_List, t_: 0.1] := 
    Flatten[Last[Reap[Map[(Pause[t #]; Sow[#]) &, l]]]];

$usage = "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"";

sleepSortMain[str_String] := Module[{nums},
  nums = Quiet @ ToExpression["{" <> str <> "}"];
  
  If[MatchQ[nums, {__Integer}] && Length[nums] >= 2,
    StringRiffle[ToString /@ sleepSort[nums], ", "],
    $usage
  ]
];

sleepSortMain[___] := $usage;

Print /@ sleepSortMain /@ {
  (* Valid cases *)
  "4, 5, 3, 1, 2",
  "4, 5, 3, 1, 4, 2",
  "1, 2, 3, 4, 5",
  "9, 8, 7, 6, 5, 4, 3, 2, 1",

  (* Invalid cases*)
  "", 
  "1", 
  "4 5 3"
};

Print[sleepSortMain[]]
```

{% endraw %}

Sleep Sort in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).