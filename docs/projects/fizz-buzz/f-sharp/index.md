---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-08
featured-image: fizz-buzz-in-every-language.png
last-modified: 2026-04-08
layout: default
tags:
- f-sharp
- fizz-buzz
title: Fizz Buzz in F#
title1: Fizz Buzz
title2: in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/f-sharp/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
module FizzBuzz =
    let (|DivisibleBy|_|) divisor number =
        if number % divisor = 0 then Some() else None

    let fizzBuzzOf number =
        match number with
        | DivisibleBy 3 & DivisibleBy 5 -> "FizzBuzz"
        | DivisibleBy 3 -> "Fizz"
        | DivisibleBy 5 -> "Buzz"
        | _ -> string number

    let printUpTo n =
        Seq.init n (fun i -> i + 1) |> Seq.map fizzBuzzOf |> Seq.iter (printfn "%s")

[<EntryPoint>]
let main _ =
    FizzBuzz.printUpTo 100
    0

```

{% endraw %}

Fizz Buzz in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).