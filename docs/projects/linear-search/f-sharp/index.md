---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-08
featured-image: linear-search-in-every-language.jpg
last-modified: 2026-04-08
layout: default
tags:
- f-sharp
- linear-search
title: Linear Search in F#
title1: Linear
title2: Search in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/linear-search/f-sharp/how-to-implement-the-solution.md
- sources/programs/linear-search/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Linear Search](https://sampleprograms.io/projects/linear-search) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
open System

module LinearSearch =
    let run (numbers: 'a list, target: 'a) =
        numbers
        |> List.exists ((=) target)
        |> Ok


module Helpers =
    let usage =
        "Usage: please provide a list of integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")"

    let private (|Int|_|) (s: string) =
        match s.Trim() |> Int32.TryParse with
        | true, n -> Some n
        | _ -> None

    let private (|IntList|_|) (s: string) =
        s.Split(',', StringSplitOptions.RemoveEmptyEntries)
        |> Array.toList
        |> List.choose (fun x ->
            match x.Trim() with
            | Int n -> Some n
            | _ -> None)
        |> function
            | [] -> None
            | xs -> Some xs


    let parseArgs argv =
        match argv with
        | [| IntList numbers; Int target |] -> Ok(numbers, target)
        | _ -> Error usage

    let handleResult =
        function
        | Ok result ->
            printfn "%b" result
            0
        | Error msg ->
            eprintfn "%s" msg
            1

[<EntryPoint>]
let main argv =
    argv
    |> Helpers.parseArgs
    |> Result.bind LinearSearch.run
    |> Helpers.handleResult

```

{% endraw %}

Linear Search in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).