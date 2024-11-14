---
authors:
- JesseChum
date: 2024-11-14
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2024-11-14
layout: default
tags:
- f-sharp
- remove-all-whitespace
title: Remove All Whitespace in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/f-sharp/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
open System

let removeAllWhitespace (input: string) : string =
    input |> Seq.filter (fun c -> not (Char.IsWhiteSpace(c))) |> String.Concat

[<EntryPoint>]
let main argv : int = 
    let ret = ref 0  

    if argv.Length = 0 then

        printfn "Usage: please provide a string"
        ret := 1
    else
        let input = argv.[0]
        if input = "" then
           
            printfn "Usage: please provide a string"
            ret := 1
        else
            let result = removeAllWhitespace input
            printfn "%s" result  

    !ret  
```

{% endraw %}

Remove All Whitespace in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- JesseChum

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).