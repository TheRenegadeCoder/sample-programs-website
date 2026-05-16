---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-06
featured-image: base64-encode-decode-in-every-language.png
last-modified: 2026-04-06
layout: default
tags:
- base64-encode-decode
- f-sharp
title: Base64 Encode Decode in F#
title1: Base64 Encode
title2: Decode in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/base64-encode-decode/f-sharp/how-to-implement-the-solution.md
- sources/programs/base64-encode-decode/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Base64 Encode Decode](https://sampleprograms.io/projects/base64-encode-decode) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
open System
open System.Text

let usage = "Usage: please provide a mode and a string to encode/decode"

module Base64 =
    let private (|Encode|Decode|InvalidMode|) (s: string) =
        match s.Trim().ToLowerInvariant() with
        | "encode" -> Encode
        | "decode" -> Decode
        | _ -> InvalidMode

    let private (|NonEmpty|Empty|) (s: string) =
        if String.IsNullOrWhiteSpace s then Empty else NonEmpty s

    let encode =
        function
        | NonEmpty s -> s |> Encoding.UTF8.GetBytes |> Convert.ToBase64String |> Ok
        | Empty -> Error usage

    let decode =
        function
        | NonEmpty s ->
            try
                Convert.FromBase64String s |> Encoding.UTF8.GetString |> Ok
            with _ ->
                Error usage
        | Empty -> Error usage

    let choose =
        function
        | Encode -> Ok encode
        | Decode -> Ok decode
        | InvalidMode -> Error usage

    let run (mode, input) = choose mode |> Result.bind (fun f -> f input)

module Helpers =
    let parseArgs argv =
        match argv with
        | [| mode; input |] -> Ok (mode, input)
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
    |> Result.bind Base64.run
    |> Helpers.handleResult

```

{% endraw %}

Base64 Encode Decode in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).