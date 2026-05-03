---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-10
featured-image: roman-numeral-in-every-language.jpg
last-modified: 2026-04-10
layout: default
tags:
- f-sharp
- roman-numeral
title: Roman Numeral in F#
title1: Roman Numeral
title2: in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/roman-numeral/f-sharp/how-to-implement-the-solution.md
- sources/programs/roman-numeral/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
open System

module Roman =

    let private value =
        function
        | 'I' -> Some 1
        | 'V' -> Some 5
        | 'X' -> Some 10
        | 'L' -> Some 50
        | 'C' -> Some 100
        | 'D' -> Some 500
        | 'M' -> Some 1000
        | _ -> None

    let parse (chars: char[]) =
        let rec loop i acc =
            if i >= chars.Length then acc
            else
                match value chars[i] with
                | None -> acc // unreachable
                | Some v ->
                    if i + 1 < chars.Length then
                        match value chars[i + 1] with
                        | Some v2 when v < v2 ->
                            loop (i + 2) (acc + v2 - v)
                        | _ ->
                            loop (i + 1) (acc + v)
                    else
                        loop (i + 1) (acc + v)

        loop 0 0


module Helpers =

    let private isRomanChar c =
        match c with
        | 'I' | 'V' | 'X' | 'L' | 'C' | 'D' | 'M' -> true
        | _ -> false

    let parseArgs = function
        | [| s |] when s = "" -> Ok [||]
        | [| s |] when s |> Seq.forall isRomanChar -> Ok (s.ToCharArray())
        | [| _ |] -> Error "Error: invalid string of roman numerals"
        | _ -> Error "Usage: please provide a string of roman numerals"

    let handleResult =
        function
        | Ok chars ->
            Roman.parse chars |> printfn "%d"
            0
        | Error msg ->
            printfn "%s" msg
            1

[<EntryPoint>]
let main argv =
    argv
    |> Helpers.parseArgs
    |> Helpers.handleResult
```

{% endraw %}

Roman Numeral in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).