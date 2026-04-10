---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-04-10
featured-image: minimum-spanning-tree-in-every-language.jpg
last-modified: 2026-04-10
layout: default
tags:
- f-sharp
- minimum-spanning-tree
title: Minimum Spanning Tree in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/minimum-spanning-tree/f-sharp/how-to-implement-the-solution.md
- sources/programs/minimum-spanning-tree/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Minimum Spanning Tree](https://sampleprograms.io/projects/minimum-spanning-tree) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
open System

module DSU =
    type t = { parent: int[]; rank: int[] }

    let create n =
        { parent = Array.init n id
          rank = Array.zeroCreate n }

    let find (dsu: t) x =
        let mutable i = x

        while dsu.parent.[i] <> i do
            dsu.parent.[i] <- dsu.parent.[dsu.parent.[i]]
            i <- dsu.parent.[i]

        i

    let union (dsu: t) x y =
        let rx = find dsu x
        let ry = find dsu y

        if rx = ry then
            false
        else
            match compare dsu.rank.[rx] dsu.rank.[ry] with
            | -1 ->
                dsu.parent.[rx] <- ry
                true
            | 1 ->
                dsu.parent.[ry] <- rx
                true
            | _ ->
                dsu.parent.[ry] <- rx
                dsu.rank.[rx] <- dsu.rank.[rx] + 1
                true


module MST =
    type t = { u: int; v: int; w: int }

    let edgesFromMatrix n (values: int[]) =
        seq {
            for i in 0 .. n - 1 do
                let baseRow = i * n

                for j in i + 1 .. n - 1 do
                    let w = values.[baseRow + j]

                    if w <> 0 then
                        { u = i; v = j; w = w }
        }

    let kruskal (n: int) (edges: seq<t>) =
        let dsu = DSU.create n

        edges
        |> Seq.sortBy (fun e -> e.w)
        |> Seq.fold
            (fun (cost, used) e ->
                if used = n - 1 then cost, used
                elif DSU.union dsu e.u e.v then cost + e.w, used + 1
                else cost, used)
            (0, 0)
        |> fst


    let run (values: int[]) (n: int) =
        values |> edgesFromMatrix n |> kruskal n

module Helpers =
    let usage = "Usage: please provide a comma-separated list of integers"

    let (|IntList|_|) (s: string) =
        let parsed =
            s.Split(',', StringSplitOptions.RemoveEmptyEntries)
            |> Array.choose (fun x ->
                match Int32.TryParse(x.Trim()) with
                | true, v -> Some v
                | _ -> None)

        if parsed.Length = 0 then None else Some parsed

    let trySquare (values: int[]) =
        let n = values.Length
        let r = int (sqrt (float n))
        if r * r = n then Some(values, r) else None

    let parseArgs =
        function
        | [| IntList values |] ->
            match trySquare values with
            | Some v -> Ok v
            | None -> Error usage
        | _ -> Error usage

    let handleResult =
        function
        | Ok result ->
            printfn "%d" result
            0
        | Error msg ->
            printfn "%s" msg
            1

[<EntryPoint>]
let main argv =
    argv
    |> Helpers.parseArgs
    |> Result.map (fun (v, n) -> MST.run v n)
    |> Helpers.handleResult

```

{% endraw %}

Minimum Spanning Tree in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).