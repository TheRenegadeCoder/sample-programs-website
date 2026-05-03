---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-10
featured-image: quick-sort-in-every-language.jpg
last-modified: 2026-04-10
layout: default
tags:
- f-sharp
- quick-sort
title: Quick Sort in F#
title1: Quick Sort
title2: in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/quick-sort/f-sharp/how-to-implement-the-solution.md
- sources/programs/quick-sort/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Quick Sort](https://sampleprograms.io/projects/quick-sort) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
open System

module QuickSort =
    let rec private sort =
        function
        | [] -> []
        | pivot :: rest ->
            let smaller, greater = rest |> List.partition (fun x -> x <= pivot)

            (sort smaller) @ (pivot :: sort greater)

    let run numbers =
        numbers |> sort |> List.map string |> String.concat ", " |> Ok

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
    argv |> Helpers.parseArgs |> Result.bind QuickSort.run |> Helpers.handleResult

```

{% endraw %}

Quick Sort in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).