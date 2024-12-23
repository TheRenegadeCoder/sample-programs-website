---
authors:
- rzuckerm
date: 2024-12-23
featured-image: baklava-in-every-language.jpg
last-modified: 2024-12-23
layout: default
tags:
- baklava
- ocaml
title: Baklava in Ocaml
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/ocaml/how-to-implement-the-solution.md
- sources/programs/baklava/ocaml/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Ocaml](https://sampleprograms.io/languages/ocaml) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ocaml
(** https://rosettacode.org/wiki/Repeat_a_string#OCaml **)
let string_repeat n s =
  String.concat "" (Array.to_list (Array.make n s));;

for n = -10 to 10 do
  let num_spaces = abs n in
  let num_stars = 21 - 2 * num_spaces in
  Printf.printf "%s%s\n" (string_repeat num_spaces " ") (string_repeat num_stars "*");
done

```

{% endraw %}

Baklava in [Ocaml](https://sampleprograms.io/languages/ocaml) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).