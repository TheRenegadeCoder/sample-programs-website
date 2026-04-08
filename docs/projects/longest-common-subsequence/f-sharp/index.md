---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-04-09
featured-image: longest-common-subsequence-in-every-language.jpg
last-modified: 2026-04-09
layout: default
tags:
- f-sharp
- longest-common-subsequence
title: Longest Common Subsequence in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-common-subsequence/f-sharp/how-to-implement-the-solution.md
- sources/programs/longest-common-subsequence/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Common Subsequence](https://sampleprograms.io/projects/longest-common-subsequence) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
﻿open System

module LCS =
    let private buildTable (s1: int[]) (s2: int[]) =
        let m, n = s1.Length, s2.Length
        let dp = Array2D.zeroCreate (m + 1) (n + 1)

        for i = 1 to m do
            for j = 1 to n do
                dp[i, j] <-
                    if s1[i - 1] = s2[j - 1] then
                        dp[i - 1, j - 1] + 1
                    else
                        max dp[i - 1, j] dp[i, j - 1]

        dp

    let private backtrack (s1: int[]) (s2: int[]) (dp: int[,]) =
        let rec loop i j acc =
            match i, j with
            | 0, _ | _, 0                         -> acc
            | _ when s1[i - 1] = s2[j - 1]        -> loop (i - 1) (j - 1) (s1[i - 1] :: acc)
            | _ when dp[i - 1, j] >= dp[i, j - 1] -> loop (i - 1) j acc
            | _                                   -> loop i (j - 1) acc

        loop s1.Length s2.Length [] |> List.toArray

    let run (a: int[], b: int[]) =
        let dp = buildTable a b
        backtrack a b dp


module Helpers =
    let usage = "Usage: please provide two lists in the format \"1, 2, 3, 4, 5\""

    let private (|IntArray|_|) (s: string) =
        let parts = s.Split(',', StringSplitOptions.RemoveEmptyEntries)

        let rec parseAll i acc =
            if i = parts.Length then
                Some(List.rev acc |> List.toArray)
            else
                match Int32.TryParse(parts[i].Trim()) with
                | true, n -> parseAll (i + 1) (n :: acc)
                | false, _ -> None

        if parts.Length = 0 then None else parseAll 0 []

    let parseArgs argv =
        match argv with
        | [| IntArray numbers; IntArray target |] -> Ok(numbers, target)
        | _ -> Error usage

    let handleResult =
        function
        | Ok result ->
            let output = result |> Array.map string |> String.concat ", "
            printfn "%s" output
            0
        | Error msg ->
            eprintfn "%s" msg
            1

[<EntryPoint>]
let main argv =
    argv |> Helpers.parseArgs |> Result.map LCS.run |> Helpers.handleResult

```

{% endraw %}

Longest Common Subsequence in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).