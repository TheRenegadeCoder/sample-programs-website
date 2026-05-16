---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-08
featured-image: file-input-output-in-every-language.jpg
last-modified: 2026-04-08
layout: default
tags:
- f-sharp
- file-input-output
title: File Input Output in F#
title1: File Input
title2: Output in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/f-sharp/how-to-implement-the-solution.md
- sources/programs/file-input-output/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
open System
open System.IO

type FileError =
    | NotFound of string
    | AccessDenied of string
    | IoError of string
    | Unknown of string

    member this.Message =
        match this with
        | NotFound fn -> $"File '{fn}' does not exist."
        | AccessDenied fn -> $"Access denied to file '{fn}'."
        | IoError msg -> $"I/O error occurred: {msg}"
        | Unknown msg -> $"An unexpected error occurred: {msg}"

module FileIO =
    let private toFileError filename (ex: Exception) =
        match ex with
        | :? FileNotFoundException -> NotFound filename
        | :? UnauthorizedAccessException -> AccessDenied filename
        | :? IOException -> IoError ex.Message
        | _ -> Unknown ex.Message

    let private wrapIO filename action =
        try
            action () |> Ok
        with ex ->
            toFileError filename ex |> Error

    let writeTo (filename: string) (contents: string) =
        wrapIO filename (fun () -> File.WriteAllText(filename, contents))

    let readFrom filename =
        wrapIO filename (fun () -> File.ReadLines filename)

let handleResult =
    function
    | Ok() -> 0
    | Error(err: FileError) ->
        eprintfn "%s" err.Message
        1

[<EntryPoint>]
let main _ =
    let filename = "output.txt"

    let contents =
        "I am a string.\n\
         I am also a string.\n\
         F# is fun."

    FileIO.writeTo filename contents
    |> Result.bind (fun () -> FileIO.readFrom filename)
    |> Result.map (Seq.iter (printfn "%s"))
    |> handleResult

```

{% endraw %}

File Input Output in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).