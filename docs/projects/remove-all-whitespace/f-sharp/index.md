---
authors:
- JesseChum
- Ștefan-Iulian Alecu
date: 2024-11-14
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2026-04-05
layout: default
tags:
- f-sharp
- remove-all-whitespace
title: Remove All Whitespace in F#
title1: Remove All
title2: Whitespace in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/f-sharp/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
open System

let removeAllWhitespace = String.filter (Char.IsWhiteSpace >> not)

[<EntryPoint>]
let main argv =
    match argv with
    | [| input |] when not (String.IsNullOrEmpty input) ->
        input |> removeAllWhitespace |> printfn "%s"
        0
    | _ ->
        printfn "Usage: please provide a string"
        1

```

{% endraw %}

Remove All Whitespace in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- JesseChum
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).