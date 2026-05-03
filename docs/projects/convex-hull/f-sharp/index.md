---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-08
featured-image: convex-hull-in-every-language.jpg
last-modified: 2026-04-08
layout: default
tags:
- convex-hull
- f-sharp
title: Convex Hull in F#
title1: Convex
title2: Hull in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/convex-hull/f-sharp/how-to-implement-the-solution.md
- sources/programs/convex-hull/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Convex Hull](https://sampleprograms.io/projects/convex-hull) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
open System

[<Struct>]
type Point =
    { X: int
      Y: int }

    static member Create x y = { X = x; Y = y }
    static member ToDisplay p = sprintf "(%d, %d)" p.X p.Y

module ConvexHull =
    let private cross a b c =
        int64 (b.X - a.X) * int64 (c.Y - a.Y) - int64 (b.Y - a.Y) * int64 (c.X - a.X)

    let private buildHalf (pts: Point seq) =
        let hull = ResizeArray<Point>()

        for p in pts do
            while hull.Count >= 2 && cross hull.[hull.Count - 2] hull.[hull.Count - 1] p < 0L do
                hull.RemoveAt(hull.Count - 1)

            hull.Add(p)

        hull

    let convexHull (points: Point array) =
        let sorted = points |> Array.distinct |> Array.sortBy (fun p -> p.X, p.Y)

        if sorted.Length < 3 then
            sorted
        else
            let lower = buildHalf sorted
            let upper = buildHalf (sorted |> Seq.rev)

            let result = Array.zeroCreate (lower.Count + upper.Count - 2)
            lower.CopyTo(0, result, 0, lower.Count - 1)
            upper.CopyTo(0, result, lower.Count - 1, upper.Count - 1)
            result

    let run (points: Point array) =
        points |> convexHull |> Array.map Point.ToDisplay |> String.concat "\n" |> Ok


module Helpers =
    let usage =
        "Usage: please provide at least 3 x and y coordinates as separate lists (e.g. \"100, 440, 210\")"

    let private (|IntList|_|) (s: string) =
        if String.IsNullOrWhiteSpace s then
            None
        else
            let parts = s.Split(',', StringSplitOptions.RemoveEmptyEntries)
            let parsed = Array.zeroCreate parts.Length
            let mutable allValid = true
            let mutable i = 0

            while allValid && i < parts.Length do
                match Int32.TryParse(parts.[i].Trim()) with
                | true, n ->
                    parsed.[i] <- n
                    i <- i + 1
                | _ -> allValid <- false

            if allValid && parsed.Length >= 2 then Some parsed else None

    let private (|Points|_|) (args: string array) =
        match args with
        | [| IntList xs; IntList ys |] when xs.Length = ys.Length && xs.Length >= 3 ->
            Array.map2 Point.Create xs ys |> Some
        | _ -> None

    let parseArgs argv =
        match argv with
        | Points pts -> Ok pts
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
    argv |> Helpers.parseArgs |> Result.bind ConvexHull.run |> Helpers.handleResult

```

{% endraw %}

Convex Hull in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).