---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-04-08
featured-image: even-odd-in-every-language.jpg
last-modified: 2026-04-08
layout: default
tags:
- even-odd
- f-sharp
title: Even Odd in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/f-sharp/how-to-implement-the-solution.md
- sources/programs/even-odd/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
open System

let usage = "Usage: please input a number"

module EvenOdd =
    let run n = if n % 2 = 0 then "Even" else "Odd"

module Helpers =
    let (|Int|_|) (s: string) =
        match s.Trim() |> Int32.TryParse with
        | true, n -> Some n
        | false, _ -> None

    let parseArgs argv =
        match argv with
        | [| Int n |] -> Ok n 
        | _ -> Error usage

    let handleResults =
        function
        | Ok result ->
            printfn "%s" result
            0
        | Error msg ->
            eprintfn "%s" msg
            1

[<EntryPoint>]
let main argv =
    argv
    |> Helpers.parseArgs
    |> Result.map EvenOdd.run
    |> Helpers.handleResults
```

{% endraw %}

Even Odd in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).