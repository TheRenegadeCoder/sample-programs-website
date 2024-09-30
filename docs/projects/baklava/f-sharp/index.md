---
authors:
- Parker Johansen
date: 2019-09-12
featured-image: baklava-in-every-language.jpg
last-modified: 2019-09-12
layout: default
tags:
- baklava
- f-sharp
title: Baklava in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/f-sharp/how-to-implement-the-solution.md
- sources/programs/baklava/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
let line space asterisk =
    String.replicate space " "  + String.replicate asterisk "*" + "\n"

let rec baklavaShrink =
    List.fold (fun accum n -> accum + (line n (21 - n * 2))) "" [ 1 .. 10 ]

let rec baklavaGrow =
    List.fold (fun accum n -> accum + (line n (21 - n * 2))) "" [ 10 .. -1 .. 0 ]

let baklava =
    baklavaGrow + baklavaShrink

[<EntryPoint>]
let main argv =
    printfn "%s" <| baklava.TrimEnd()
    0


```

{% endraw %}

Baklava in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).