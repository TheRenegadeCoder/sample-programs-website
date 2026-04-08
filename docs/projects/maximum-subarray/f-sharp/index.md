---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-04-09
featured-image: maximum-subarray-in-every-language.jpg
last-modified: 2026-04-09
layout: default
tags:
- f-sharp
- maximum-subarray
title: Maximum Subarray in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-subarray/f-sharp/how-to-implement-the-solution.md
- sources/programs/maximum-subarray/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Subarray](https://sampleprograms.io/projects/maximum-subarray) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
﻿open System

module MaximumSubarray =
    let run =
        Array.fold (fun (currentMax, globalMax) x ->
            let x = int64 x
            let newCurrent = max x (currentMax + x)
            (newCurrent, max globalMax newCurrent)
        ) (0L, Int64.MinValue)
        >> snd

module Helpers =
    let usage =
        "Usage: Please provide a list of integers in the format: \"1, 2, 3, 4, 5\""

    let private (|IntArray|_|) (s: string) =
        let parts = s.Split(',', StringSplitOptions.RemoveEmptyEntries)

        let rec parseAll i acc =
            if i = parts.Length then
                List.rev acc |> List.toArray |> Some
            else
                match parts[i] |> _.Trim() |> Int32.TryParse with
                | true, n -> parseAll (i + 1) (n :: acc)
                | false, _ -> None

        if parts.Length = 0 then None else parseAll 0 []

    let parseArgs argv =
        match argv with
        | [| IntArray numbers |] -> Ok(numbers)
        | _ -> Error usage

    let handleResult =
        function
        | Ok result ->
            printfn "%d" result
            0
        | Error msg ->
            eprintfn "%s" msg
            1

[<EntryPoint>]
let main argv =
    argv
    |> Helpers.parseArgs
    |> Result.map MaximumSubarray.run
    |> Helpers.handleResult
```

{% endraw %}

Maximum Subarray in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).