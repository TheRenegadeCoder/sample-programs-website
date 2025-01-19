---
authors:
- Zia
date: 2025-01-19
featured-image: fizz-buzz-in-every-language.png
last-modified: 2025-01-19
layout: default
tags:
- fizz-buzz
- ocaml
title: Fizz Buzz in Ocaml
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/ocaml/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/ocaml/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Ocaml](https://sampleprograms.io/languages/ocaml) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ocaml
let fizzbuzz i =
  if i mod 15 == 0
  then "FizzBuzz"
  else if i mod 5 == 0
  then "Buzz"
  else if i mod 3 == 0
  then "Fizz"
  else string_of_int i
;;

for i = 1 to 100 do
  print_string (fizzbuzz(i) ^ "\n")
done;;

```

{% endraw %}

Fizz Buzz in [Ocaml](https://sampleprograms.io/languages/ocaml) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).