---
authors:
- Parker Johansen
- Ștefan-Iulian Alecu
date: 2019-09-12
featured-image: baklava-in-every-language.jpg
last-modified: 2026-04-05
layout: default
tags:
- baklava
- f-sharp
title: Baklava in F#
title1: Baklava
title2: in F#
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
open System

let inline repeat count (char: char) = String(char, count)

let baklava size =
    { -size .. size }
    |> Seq.map (fun y ->
        let padding = abs y
        repeat padding ' ' + repeat (2 * (size - padding) + 1) '*')
    |> String.concat Environment.NewLine

[<EntryPoint>]
let main argv =
    baklava 10 |> printfn "%s"
    0

```

{% endraw %}

Baklava in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Parker Johansen
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).