---
authors:
- alope107
date: 2026-05-21
featured-image: prime-number-in-every-language.jpg
last-modified: 2026-05-21
layout: default
tags:
- ocaml
- prime-number
title: Prime Number in OCaml
title1: Prime Number
title2: in OCaml
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/ocaml/how-to-implement-the-solution.md
- sources/programs/prime-number/ocaml/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [OCaml](https://sampleprograms.io/languages/ocaml) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ocaml
let has_odd_divisor_under_sqrt n =
  let rec aux k = k <= n / k && (n mod k = 0 || aux (k + 2)) in
  aux 3 (* Assumes n > 3. All other cases will be caught elsewhere *)

let prime = function
  | 0 | 1 -> false
  | 2 | 3 -> true
  | n when n mod 2 = 0 -> false
  | n -> not (has_odd_divisor_under_sqrt n)

let parse_args argv =
  match argv with [| _; n |] -> int_of_string_opt n | _ -> None

let () =
  print_endline
    (match parse_args Sys.argv with
    | Some num when num >= 0 -> if prime num then "Prime" else "Composite"
    | _ -> "Usage: please input a non-negative integer")

```

{% endraw %}

Prime Number in [OCaml](https://sampleprograms.io/languages/ocaml) was written by:

- alope107

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).