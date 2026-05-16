---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-08
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2026-04-08
layout: default
tags:
- duplicate-character-counter
- f-sharp
title: Duplicate Character Counter in F#
title1: Duplicate Character
title2: Counter in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/f-sharp/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
open System

let usage = "Usage: please provide a string"

module DuplicateCharacterCounter =
    let private getDuplicateCounts =
        Seq.countBy id
        >> Seq.filter (fun (_, count) -> count > 1)
        >> Seq.map (fun (c, count) -> sprintf "%c: %d" c count)
        >> Seq.toList

    let private formatOutput =
        function
        | [] -> "No duplicate characters"
        | items -> String.concat "\n" items

    let run input =
        input |> getDuplicateCounts |> formatOutput |> Ok

module Helpers =
    let (|Empty|NonEmpty|) (s: string) =
        match s.Trim() with
        | "" -> Empty
        | trimmed -> NonEmpty trimmed

    let parseArgs argv =
        match argv with
        | [| Empty |] -> Error usage
        | [| NonEmpty input |] -> Ok input
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
    |> Result.bind DuplicateCharacterCounter.run
    |> Helpers.handleResults

```

{% endraw %}

Duplicate Character Counter in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).