---
authors:
- alope107
date: 2026-05-17
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2026-05-17
layout: default
tags:
- duplicate-character-counter
- ocaml
title: Duplicate Character Counter in OCaml
title1: Duplicate Character
title2: Counter in OCaml
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/ocaml/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/ocaml/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [OCaml](https://sampleprograms.io/languages/ocaml) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ocaml
module CharMap = Map.Make (Char)

let increment_map (counts, seen) k =
  match CharMap.find_opt k counts with
  | Some n -> (CharMap.add k (n + 1) counts, seen)
  | None -> (CharMap.add k 1 counts, k :: seen)

let count_chars str =
  str |> String.to_seq |> Seq.fold_left increment_map (CharMap.empty, [])

let dupes str =
  let counts, seen = count_chars str in
  seen |> List.rev
  |> List.filter_map (fun c ->
      let count = CharMap.find c counts in
      if count > 1 then Some (c, count) else None)

let print_dupes str =
  match dupes str with
  | [] -> print_endline "No duplicate characters"
  | counts ->
      List.iter (fun (c, count) -> Printf.printf "%c: %d\n" c count) counts

let get_arg argv =
  match argv with [| _; "" |] -> None | [| _; str |] -> Some str | _ -> None

let () =
  match get_arg Sys.argv with
  | Some str -> print_dupes str
  | None -> print_endline "Usage: please provide a string"

```

{% endraw %}

Duplicate Character Counter in [OCaml](https://sampleprograms.io/languages/ocaml) was written by:

- alope107

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).