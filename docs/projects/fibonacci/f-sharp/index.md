---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-08
featured-image: fibonacci-in-every-language.jpg
last-modified: 2026-04-08
layout: default
tags:
- f-sharp
- fibonacci
title: Fibonacci in F#
title1: Fibonacci
title2: in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/f-sharp/how-to-implement-the-solution.md
- sources/programs/fibonacci/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
open System

module Fibonacci =
    let run n =
        Seq.unfold (fun (a, b) -> Some(a, (b, a + b))) (1, 1)
        |> Seq.take n
        |> Seq.mapi (fun i v -> sprintf "%d: %d" (i + 1) v)
        |> String.concat "\n"

module Helpers =
    let usage = "Usage: please input the count of fibonacci numbers to output"

    let (|NonNegativeInt|_|) (s: string) =
        match s.Trim() |> Int32.TryParse with
        | true, n when n >= 0 -> Some n
        | _ -> None

    let parseArgs argv =
        match argv with
        | [| NonNegativeInt n |] -> Ok n
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
    argv |> Helpers.parseArgs |> Result.map Fibonacci.run |> Helpers.handleResults

```

{% endraw %}

Fibonacci in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).