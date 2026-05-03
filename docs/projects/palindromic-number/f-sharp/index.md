---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-10
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2026-04-10
layout: default
tags:
- f-sharp
- palindromic-number
title: Palindromic Number in F#
title1: Palindromic
title2: Number in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/f-sharp/how-to-implement-the-solution.md
- sources/programs/palindromic-number/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
open System

module Palindrome =
    let isPalindrome (n: int) =
        if n < 0 then
            false
        elif n % 10 = 0 && n <> 0 then
            false
        else
            let rec loop x rev =
                if x <= rev then
                    x = rev || x = rev / 10
                else
                    loop (x / 10) (rev * 10 + x % 10)

            loop n 0

module Helpers =
    let parseArgs =
        function
        | [| input: string |] ->
            match Int32.TryParse input with
            | true, n when n >= 0 -> Ok n
            | _ -> Error "Usage: please input a non-negative integer"
        | _ -> Error "Usage: please input a non-negative integer"

    let handleResult =
        function
        | Ok result ->
            printfn "%b" result
            0
        | Error msg ->
            eprintfn "%s" msg
            1

[<EntryPoint>]
let main argv =
    argv
    |> Helpers.parseArgs
    |> Result.map Palindrome.isPalindrome
    |> Helpers.handleResult

```

{% endraw %}

Palindromic Number in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).