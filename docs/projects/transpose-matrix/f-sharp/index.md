---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-04-10
featured-image: transpose-matrix-in-every-language.jpg
last-modified: 2026-04-10
layout: default
tags:
- f-sharp
- transpose-matrix
title: Transpose Matrix in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/transpose-matrix/f-sharp/how-to-implement-the-solution.md
- sources/programs/transpose-matrix/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Transpose Matrix](https://sampleprograms.io/projects/transpose-matrix) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
open System

module Matrix =
    let transpose (data: int[,]) =
        let rows = data.GetLength 0
        let cols = data.GetLength 1

        Array2D.init cols rows (fun x y ->
            data.[y, x]
        )

module Helpers =
    let parseInt (s: string) =
        match s.Trim() |> Int32.TryParse with
        | true, v -> Some v
        | _ -> None

    let parseMatrix (s: string) =
        s.Split(',', StringSplitOptions.RemoveEmptyEntries)
        |> Array.choose parseInt
        |> function
            | arr when arr.Length > 0 -> Some arr
            | _ -> None

    let parseArgs (argv: string[]) =
        match argv with
        | [| cStr; rStr; matrixStr |] ->
            match parseInt cStr, parseInt rStr, parseMatrix matrixStr with
            | Some c, Some r, Some values when values.Length = c * r ->
                Ok (c, r, values)

            | _ ->
                Error ()

        | _ ->
            Error ()

    let buildMatrix (c, r, values: int[]) =
        Array2D.init r c (fun i j ->
            values.[i * c + j]
        )

    let handleResult =
        function
        | Ok m ->
            m |> Seq.cast<int> |> Seq.map string |> String.concat ", " |> printfn "%s"
            0

        | Error () ->
            printfn "Usage: please enter the dimension of the matrix and the serialized matrix"
            1


[<EntryPoint>]
let main argv =
    argv
    |> Helpers.parseArgs
    |> Result.map Helpers.buildMatrix
    |> Result.map Matrix.transpose
    |> Helpers.handleResult
```

{% endraw %}

Transpose Matrix in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).