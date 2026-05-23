---
authors:
- alope107
date: 2026-05-20
featured-image: reverse-string-in-every-language.jpg
last-modified: 2026-05-20
layout: default
tags:
- ocaml
- reverse-string
title: Reverse String in OCaml
title1: Reverse String
title2: in OCaml
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/ocaml/how-to-implement-the-solution.md
- sources/programs/reverse-string/ocaml/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](/projects/reverse-string) in [OCaml](/languages/ocaml) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ocaml
let reverse s =
  let len = String.length s in
  String.init len (fun i -> s.[len - i - 1])

let () =
  print_endline
    (match Sys.argv with [||] | [| _ |] -> "" | args -> reverse args.(1))
(* Any additional arguments are ignored, following the example of other samples in this repo *)

```

{% endraw %}

Reverse String in [OCaml](/languages/ocaml) was written by:

- alope107

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).