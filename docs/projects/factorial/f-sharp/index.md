---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-08
featured-image: factorial-in-every-language.jpg
last-modified: 2026-04-08
layout: default
tags:
- f-sharp
- factorial
title: Factorial in F#
title1: Factorial
title2: in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/f-sharp/how-to-implement-the-solution.md
- sources/programs/factorial/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
open System

module Factorial =
    let rec private factorial n acc =
        if n <= 1L then acc else factorial (n - 1L) (acc * n)

    let run n = factorial n 1L |> string

module Helpers =
    let usage = "Usage: please input a non-negative integer"

    let (|NonNegativeInteger|_|) (s: string) =
        match s.Trim() |> Int64.TryParse with
        | true, n when n >= 0L -> Some n
        | _ -> None

    let parseArgs argv =
        match argv with
        | [| NonNegativeInteger n |] -> Ok n
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
    argv |> Helpers.parseArgs |> Result.map Factorial.run |> Helpers.handleResults

```

{% endraw %}

Factorial in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).