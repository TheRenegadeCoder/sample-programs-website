---
authors:
- rzuckerm
date: 2025-01-06
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-06
layout: default
tags:
- baklava
- f-star
title: Baklava in F*
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/f-star/how-to-implement-the-solution.md
- sources/programs/baklava/f-star/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [F\*](https://sampleprograms.io/languages/f-star) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f\*
module Baklava

open FStar.IO
open FStar.Math.Lib
open FStar.Mul

let baklava_line (n:nat {n <= 20}) : string =
  let num_spaces:nat = (abs (n - 10)) in
  let num_stars:nat = 21 - 2 * num_spaces in
  (String.make num_spaces ' ') ^ (String.make num_stars '*') ^ "\n"

let rec baklava (lines:string) (n:nat {n <= 20}) : string =
  match n with
  | 0 -> lines ^ (baklava_line 0)
  | _ -> lines ^ (baklava_line n) ^ (baklava lines (n - 1))

let main = print_string (baklava "" 20)

```

{% endraw %}

Baklava in [F\*](https://sampleprograms.io/languages/f-star) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).