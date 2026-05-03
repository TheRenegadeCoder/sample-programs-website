---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-08
featured-image: insertion-sort-in-every-language.jpg
last-modified: 2026-04-08
layout: default
tags:
- f-sharp
- insertion-sort
title: Insertion Sort in F#
title1: Insertion
title2: Sort in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/insertion-sort/f-sharp/how-to-implement-the-solution.md
- sources/programs/insertion-sort/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
open System

module InsertionSort =
    let rec private insert sorted x =
        match sorted with
        | [] -> [ x ]                                // Insert at end
        | head :: tail when x <= head -> x :: sorted // Found spot
        | head :: tail -> head :: insert tail x      // Keep traversing

    let run numbers =
        numbers |> List.fold insert [] |> List.map string |> String.concat ", " |> Ok

module Result =
    let toOption =
        function
        | Ok x -> Some x
        | Error _ -> None

module Helpers =
    let private (|IntList|_|) (s: string) =
        let ns =
            s.Split(',', StringSplitOptions.RemoveEmptyEntries)
            |> Array.toList
            |> List.map (fun p ->
                match Int32.TryParse(p.Trim()) with
                | true, n -> Ok n
                | false, _ -> Error $"Invalid integer: '{p}'")
            |> List.choose Result.toOption

        if ns.Length >= 2 then Some ns else None

    let parseArgs argv =
        match argv with
        | [| IntList numbers |] -> Ok numbers
        | _ -> Error "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\""

    let handleResult =
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
    |> Result.bind InsertionSort.run
    |> Helpers.handleResult

```

{% endraw %}

Insertion Sort in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).