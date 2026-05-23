---
authors:
- alope107
date: 2026-05-16
featured-image: capitalize-in-every-language.jpg
last-modified: 2026-05-16
layout: default
tags:
- capitalize
- ocaml
title: Capitalize in OCaml
title1: Capitalize
title2: in OCaml
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/ocaml/how-to-implement-the-solution.md
- sources/programs/capitalize/ocaml/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](/projects/capitalize) in [OCaml](/languages/ocaml) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ocaml
let () = print_endline (
  match Array.to_list Sys.argv with
  | [] | [_] | [_; ""] -> "Usage: please provide a string"
  | _::args -> args |> String.concat " " |> String.capitalize_ascii)
```

{% endraw %}

Capitalize in [OCaml](/languages/ocaml) was written by:

- alope107

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).