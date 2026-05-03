---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-08
featured-image: fraction-math-in-every-language.jpg
last-modified: 2026-04-08
layout: default
tags:
- f-sharp
- fraction-math
title: Fraction Math in F#
title1: Fraction
title2: Math in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fraction-math/f-sharp/how-to-implement-the-solution.md
- sources/programs/fraction-math/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fraction Math](https://sampleprograms.io/projects/fraction-math) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
open System

[<Struct; CustomEquality; CustomComparison>]
type Fraction =
    private
        { n: int64
          d: int64 }

    static member Raw(n, d) =
        if d = 0L then
            invalidArg "d" "Denominator cannot be zero"

        let rec gcd x y = if y = 0L then abs x else gcd y (x % y)

        let sign = if d < 0L then -1L else 1L
        let nn = n * int64 sign
        let dd = abs d

        let g = gcd nn dd
        { n = nn / g; d = dd / g }

    static member Create(n, d) =
        if d = 0L then
            Error "Division by zero"
        else
            Ok(Fraction.Raw(n, d))

    override x.ToString() =
        if x.d = 1L then $"{x.n}" else $"{x.n}/{x.d}"

    override x.Equals o =
        match o with
        | :? Fraction as f -> x.n = f.n && x.d = f.d
        | _ -> false

    override x.GetHashCode() = hash (x.n, x.d)

    interface IComparable with
        member x.CompareTo o =
            match o with
            | :? Fraction as f -> compare (x.n * f.d) (f.n * x.d)
            | _ -> 0

    static member (+)(a, b) =
        Fraction.Raw(a.n * b.d + b.n * a.d, a.d * b.d)

    static member (-)(a, b) =
        Fraction.Raw(a.n * b.d - b.n * a.d, a.d * b.d)

    static member (*)(a, b) = Fraction.Raw(a.n * b.n, a.d * b.d)

    static member TryDiv(a, b) =
        if b.n = 0L then
            Error "Division by zero"
        else
            Ok(Fraction.Raw(a.n * b.d, a.d * b.n))

module Calculator =
    let (|Int|_|) (s: string) =
        match Int64.TryParse s with
        | true, n -> Some n
        | _ -> None

    let (|Fraction|_|) (s: string) =
        match s.Split('/') with
        | [| Int n; Int d |] -> Fraction.Create(n, d) |> Result.toOption
        | [| Int n |] -> Some(Fraction.Raw(n, 1L))
        | _ -> None

    let (|Arith|_|) =
        function
        | "+" -> Some (+)
        | "-" -> Some (-)
        | "*" -> Some (*)
        | "/" ->
            Some(fun a b ->
                Fraction.TryDiv(a, b)
                |> Result.defaultWith (fun _ -> failwith "Division by zero"))
        | _ -> None

    let (|Logic|_|) =
        function
        | "==" -> Some (=)
        | "!=" -> Some (<>)
        | ">" -> Some (>)
        | "<" -> Some (<)
        | ">=" -> Some (>=)
        | "<=" -> Some (<=)
        | _ -> None

    let run f1 opStr f2 =
        match opStr with
        | Arith f -> Ok(string (f f1 f2))
        | Logic f -> Ok(if f f1 f2 then "1" else "0")
        | _ -> Error $"Invalid operator: {opStr}"

module Helpers =
    open Calculator
    let usage = "Usage: ./fraction-math operand1 operator operand2"

    let parseArgs argv =
        match argv with
        | [| Fraction f1; op; Fraction f2 |] -> Ok(f1, op, f2)
        | _ -> Error usage

    let handleResult =
        function
        | Ok r ->
            printfn "%s" r
            0
        | Error m ->
            eprintfn "%s" m
            1

[<EntryPoint>]
let main argv =
    argv
    |> Helpers.parseArgs
    |> Result.bind (fun (f1, op, f2) -> Calculator.run f1 op f2)
    |> Helpers.handleResult

```

{% endraw %}

Fraction Math in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).