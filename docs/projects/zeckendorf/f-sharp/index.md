---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-10
featured-image: zeckendorf-in-every-language.png
last-modified: 2026-04-10
layout: default
tags:
- f-sharp
- zeckendorf
title: Zeckendorf in F#
title1: Zeckendorf
title2: in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/zeckendorf/f-sharp/how-to-implement-the-solution.md
- sources/programs/zeckendorf/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Zeckendorf](https://sampleprograms.io/projects/zeckendorf) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
open System

module Zeckendorf =

    let getDescendingFibs n =
        let rec loop a b acc =
            if a > n then acc
            else loop b (a + b) (a :: acc)
        
        loop 1 2 []

    let compute n =
        if n = 0 then []
        else
            let rec go remaining fibs acc =
                match remaining, fibs with
                | 0, _ -> List.rev acc
                | _, [] -> List.rev acc
                | r, f :: tail ->
                    if f <= r then
                        go (r - f) tail (f :: acc)
                    else
                        go r tail acc

            go n (getDescendingFibs n) []

    let run n =
        match compute n with
        | [] -> ""
        | fibs -> String.concat ", " (List.map string fibs)

module Helpers =

    let usage = "Usage: please input a non-negative integer"

    let (|NonNegativeInt|_|) (s: string) =
        match Int32.TryParse(s.Trim()) with
        | true, n when n >= 0 -> Some n
        | _ -> None

    let parseArgs =
        function
        | [| NonNegativeInt n |] -> Ok n
        | _ -> Error usage

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
    |> Result.map Zeckendorf.run
    |> Helpers.handleResult
```

{% endraw %}

Zeckendorf in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).