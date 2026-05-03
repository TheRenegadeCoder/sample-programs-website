---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-09
featured-image: maximum-array-rotation-in-every-language.jpg
last-modified: 2026-04-09
layout: default
tags:
- f-sharp
- maximum-array-rotation
title: Maximum Array Rotation in F#
title1: Maximum Array
title2: Rotation in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-array-rotation/f-sharp/how-to-implement-the-solution.md
- sources/programs/maximum-array-rotation/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Array Rotation](https://sampleprograms.io/projects/maximum-array-rotation) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
﻿open System

module MaximumArrayRotation =
    let run (arr: int[]) =
        let n = int64 arr.Length

        if n = 0L then
            0L
        else
            let sumAll = Array.sumBy int64 arr
            let r0 = arr |> Array.indexed |> Array.sumBy (fun (i, v) -> int64 i * int64 v)

            seq { 1 .. int n - 1 }
            |> Seq.scan (fun prevSum i -> prevSum + sumAll - n * int64 arr[int n - i]) r0
            |> Seq.max

module Helpers =
    let usage = "Usage: please provide a list of integers (e.g. \"8, 3, 1, 2\")"

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
    |> Result.map MaximumArrayRotation.run
    |> Helpers.handleResult

```

{% endraw %}

Maximum Array Rotation in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).