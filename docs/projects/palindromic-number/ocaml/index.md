---
authors:
- alope107
date: 2026-05-17
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2026-05-17
layout: default
tags:
- ocaml
- palindromic-number
title: Palindromic Number in OCaml
title1: Palindromic
title2: Number in OCaml
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/ocaml/how-to-implement-the-solution.md
- sources/programs/palindromic-number/ocaml/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](/projects/palindromic-number) in [OCaml](/languages/ocaml) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ocaml
let ( let* ) = Option.bind

let palindrome str =
  let rec aux lo hi =
    lo >= hi || (str.[lo] = str.[hi] && (aux [@tailcall]) (lo + 1) (hi - 1))
  in
  aux 0 (String.length str - 1)

let validate_arg = function
  | [| _; n |] ->
      let* num = int_of_string_opt n in
      if num >= 0 then
        (* Converting back and forth normalizes the number 
           - allows for checking things like "+323" based on the actual numerical value *)
        (* Problem statement is underspecified, so going to follow Postel's law and be permissive :) *)
        Some (string_of_int num)
      else None
  | _ -> None

let () =
  match validate_arg Sys.argv with
  | Some n -> Printf.printf "%b\n" (palindrome n)
  | None -> print_endline "Usage: please input a non-negative integer"

```

{% endraw %}

Palindromic Number in [OCaml](/languages/ocaml) was written by:

- alope107

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).