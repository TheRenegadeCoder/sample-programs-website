---
authors:
- alope107
date: 2026-05-17
featured-image: factorial-in-every-language.jpg
last-modified: 2026-05-17
layout: default
tags:
- factorial
- ocaml
title: Factorial in OCaml
title1: Factorial
title2: in OCaml
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/ocaml/how-to-implement-the-solution.md
- sources/programs/factorial/ocaml/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [OCaml](https://sampleprograms.io/languages/ocaml) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ocaml
let factorial n =
  (* Use accumulator so OCaml can do tail call recursion *)
  let rec helper acc n =
    match n with 0 | 1 -> acc | n -> helper (acc * n) (n - 1)
  in
  helper 1 n

let parse_args argv =
  match argv with [| _; n |] -> int_of_string_opt n | _ -> None

let () =
  print_endline
    (match parse_args Sys.argv with
    | Some num when num >= 0 -> num |> factorial |> string_of_int
    | _ -> "Usage: please input a non-negative integer")

```

{% endraw %}

Factorial in [OCaml](https://sampleprograms.io/languages/ocaml) was written by:

- alope107

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).