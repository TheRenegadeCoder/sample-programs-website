---
authors:
- alope107
date: 2026-05-17
featured-image: fibonacci-in-every-language.jpg
last-modified: 2026-05-17
layout: default
tags:
- fibonacci
- ocaml
title: Fibonacci in OCaml
title1: Fibonacci
title2: in OCaml
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/ocaml/how-to-implement-the-solution.md
- sources/programs/fibonacci/ocaml/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [OCaml](https://sampleprograms.io/languages/ocaml) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ocaml
let fib n =
  let rec help current max out =
    if current > max then List.rev out
    else
      match out with
      | prev :: prevprev :: _ ->
          help (current + 1) max ((prev + prevprev) :: out)
      | _ -> help (current + 1) max (1 :: out)
  in
  help 1 n []

let fib_table n =
  List.iteri (fun i e -> Printf.printf "%d: %d\n" (i + 1) e) (fib n)

let parse_args argv =
  match argv with [| _; n |] -> int_of_string_opt n | _ -> None

let () =
  match parse_args Sys.argv with
  | Some num when num >= 0 -> fib_table num
  | _ ->
      print_endline
        "Usage: please input the count of fibonacci numbers to output"

```

{% endraw %}

Fibonacci in [OCaml](https://sampleprograms.io/languages/ocaml) was written by:

- alope107

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).