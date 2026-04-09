---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-04-10
featured-image: rot13-in-every-language.jpg
last-modified: 2026-04-10
layout: default
tags:
- f-sharp
- rot13
title: Rot13 in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/f-sharp/how-to-implement-the-solution.md
- sources/programs/rot13/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
open System

module Rot13 =
    let private rot13Char c =
        let shift baseLetter =
            char (((int c - int baseLetter + 13) % 26) + int baseLetter)

        if c >= 'a' && c <= 'z' then shift 'a'
        elif c >= 'A' && c <= 'Z' then shift 'A'
        else c

    let run = String.map rot13Char

module Helpers =
    let parseArgs =
        function
        | [| s |] when s <> "" -> Ok s
        | _ -> Error "Usage: please provide a string to encrypt"

    let handleResult =
        function
        | Ok s ->
            s |> Rot13.run |> printfn "%s"
            0
        | Error msg ->
            printfn "%s" msg
            1

[<EntryPoint>]
let main argv =
    argv |> Helpers.parseArgs |> Helpers.handleResult

```

{% endraw %}

Rot13 in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).