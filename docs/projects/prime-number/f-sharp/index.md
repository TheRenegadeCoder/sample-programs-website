---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-10
featured-image: prime-number-in-every-language.jpg
last-modified: 2026-04-10
layout: default
tags:
- f-sharp
- prime-number
title: Prime Number in F#
title1: Prime Number
title2: in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/f-sharp/how-to-implement-the-solution.md
- sources/programs/prime-number/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
open System

module Prime =
    let isPrime n =
        if n < 2 then false
        elif n = 2 then true
        elif n % 2 = 0 then false
        else
            let rec loop d =
                if d * d > n then true
                elif n % d = 0 then false
                else loop (d + 2)
            loop 3

module Helpers =
    let parseArgs =
        function
        | [| input: string |] ->
            match Int32.TryParse input with
            | true, n when n >= 0 -> Ok n
            | _ -> Error "Usage: please input a non-negative integer"
        | _ -> Error "Usage: please input a non-negative integer"

    let handleResult = function
        | Ok true  -> printfn "prime"; 0
        | Ok false -> printfn "composite"; 0
        | Error e  -> eprintfn "%s" e; 1

[<EntryPoint>]
let main argv =
    argv
    |> Helpers.parseArgs
    |> Result.map Prime.isPrime
    |> Helpers.handleResult

```

{% endraw %}

Prime Number in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).