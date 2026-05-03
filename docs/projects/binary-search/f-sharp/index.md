---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-06
featured-image: binary-search-in-every-language.jpg
last-modified: 2026-04-06
layout: default
tags:
- binary-search
- f-sharp
title: Binary Search in F#
title1: Binary
title2: Search in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/binary-search/f-sharp/how-to-implement-the-solution.md
- sources/programs/binary-search/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Binary Search](https://sampleprograms.io/projects/binary-search) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
open System

module BinarySearch =
    let private search (haystack: int array) (needle: int) =
        let len = haystack.Length

        if needle < haystack.[0] || needle > haystack.[len - 1] then
            false
        else
            let rec loop lo hi =
                if lo > hi then
                    false
                else
                    let mid = lo + (hi - lo) / 2

                    match compare needle haystack.[mid] with
                    | 0 -> true
                    | c when c < 0 -> loop lo (mid - 1)
                    | _ -> loop (mid + 1) hi

            loop 0 (len - 1)

    let find haystack needle = search haystack needle

module Helpers =

    let private isSorted itemList =
        itemList |> Seq.pairwise |> Seq.forall (fun (a, b) -> a <= b)

    let private (|Int|_|) (s: string) =
        match Int32.TryParse(s.Trim()) with
        | true, n -> Some n
        | _ -> None

    let private (|SortedIntList|_|) (s: string) =
        if String.IsNullOrWhiteSpace(s) then
            None
        else
            let parts = s.Split([| ',' |], StringSplitOptions.RemoveEmptyEntries)

            let parsed =
                parts
                |> Array.choose (
                    function
                    | Int n -> Some n
                    | _ -> None
                )

            if not (Array.isEmpty parsed) && parsed.Length = parts.Length && isSorted parsed then
                Some parsed
            else
                None

    let parseArgs argv =
        match argv with
        | [| SortedIntList numbers; Int target |] -> Ok(numbers, target)
        | _ ->
            Error
                "Usage: please provide a list of sorted integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")"

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
    let okBool (b: bool) = if b then Ok "true" else Ok "false"

    argv
    |> Helpers.parseArgs
    |> Result.bind (fun (numbers, target) -> BinarySearch.find numbers target |> okBool)
    |> Helpers.handleResult

```

{% endraw %}

Binary Search in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).