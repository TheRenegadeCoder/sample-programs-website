---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-08
featured-image: longest-word-in-every-language.jpg
last-modified: 2026-04-08
layout: default
tags:
- f-sharp
- longest-word
title: Longest Word in F#
title1: Longest
title2: Word in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/f-sharp/how-to-implement-the-solution.md
- sources/programs/longest-word/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
﻿open System

module LongestWord =
    let run (s: string) =
        s
        |> Seq.fold
            (fun (maxLen, currLen) ch ->
                if Char.IsWhiteSpace ch then
                    (max maxLen currLen, 0)
                else
                    (maxLen, currLen + 1))
            (0, 0)
        |> fun (maxLen, currLen) -> max maxLen currLen

module Helpers =
    let usage = "Usage: please provide a string"

    let parseArgs argv =
        match argv with
        | [| s |] when not (String.IsNullOrEmpty s) -> Ok s
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
    argv |> Helpers.parseArgs |> Result.map LongestWord.run |> Helpers.handleResult

```

{% endraw %}

Longest Word in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).