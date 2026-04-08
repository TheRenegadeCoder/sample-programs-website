---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-04-08
featured-image: josephus-problem-in-every-language.jpg
last-modified: 2026-04-08
layout: default
tags:
- f-sharp
- josephus-problem
title: Josephus Problem in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/josephus-problem/f-sharp/how-to-implement-the-solution.md
- sources/programs/josephus-problem/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Josephus Problem](https://sampleprograms.io/projects/josephus-problem) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
open System

module Josephus =
    let run (n, k) =
        if n = 1 then
            Ok 1
        elif k = 1 then
            Ok n
        elif k = 2 then
            // fast formula for k = 2
            let mutable p = 1

            while p <= n do
                p <- p <<< 1

            Ok(2 * (n - (p >>> 1)) + 1)
        else
            // general k > 2 using iterative approach
            let mutable survivor = 0

            for i in 2..n do
                survivor <- (survivor + k) % i

            Ok(survivor + 1)

module Helpers =
    let usage =
        "Usage: please input the total number of people and number of people to skip."

    let private (|Int|_|) (s: string) =
        match s.Trim() |> Int32.TryParse with
        | true, n -> Some n
        | false, _ -> None

    let parseArgs argv =
        match argv with
        | [| Int n; Int k |] when n > 0 && k > 0 -> Ok(n, k)
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
    argv |> Helpers.parseArgs |> Result.bind Josephus.run |> Helpers.handleResult

```

{% endraw %}

Josephus Problem in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).