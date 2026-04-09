---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-04-10
featured-image: reverse-string-in-every-language.jpg
last-modified: 2026-04-10
layout: default
tags:
- f-sharp
- reverse-string
title: Reverse String in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/f-sharp/how-to-implement-the-solution.md
- sources/programs/reverse-string/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
open System

module Reverse =
    let run (s: string) =
        let arr = s.ToCharArray()
        Array.Reverse arr
        String arr

module Helpers =

    let parseArgs = function
        | [| s |] -> Some s
        | _ -> None

    let handle = function
        | Some s ->
            s |> Reverse.run |> printfn "%s"
        | None ->
            printfn ""

[<EntryPoint>]
let main argv =
    argv
    |> Helpers.parseArgs
    |> Helpers.handle

    0
```

{% endraw %}

Reverse String in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).