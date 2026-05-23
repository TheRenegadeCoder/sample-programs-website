---
authors:
- alope107
date: 2026-05-17
featured-image: linear-search-in-every-language.jpg
last-modified: 2026-05-17
layout: default
tags:
- linear-search
- ocaml
title: Linear Search in OCaml
title1: Linear Search
title2: in OCaml
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/linear-search/ocaml/how-to-implement-the-solution.md
- sources/programs/linear-search/ocaml/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Linear Search](/projects/linear-search) in [OCaml](/languages/ocaml) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ocaml
let ( let* ) = Option.bind
let ( let+ ) f g = Option.map g f

let parse_list list_str =
  let rec aux acc l =
    match l with
    | [] -> Some (List.rev acc)
    | head :: rest ->
        let* num = head |> String.trim |> int_of_string_opt in
        aux (num :: acc) rest
  in
  list_str |> String.split_on_char ',' |> aux []

let parse_args argv =
  match argv with
  | [| _; nums; key |] ->
      let* parsed_nums = parse_list nums in
      let+ parsed_key = int_of_string_opt key in
      (parsed_nums, parsed_key)
  | _ -> None

let () =
  match parse_args Sys.argv with
  | Some (nums, key) -> Printf.printf "%b\n" (List.mem key nums)
  | _ ->
      print_endline
        {|Usage: please provide a list of integers ("1, 4, 5, 11, 12") and the integer to find ("11")|}

```

{% endraw %}

Linear Search in [OCaml](/languages/ocaml) was written by:

- alope107

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).