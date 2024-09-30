---
authors:
- Jeremy Grifski
date: 2019-04-25
featured-image: fizz-buzz-in-every-language.png
last-modified: 2019-04-25
layout: default
tags:
- elixir
- fizz-buzz
title: Fizz Buzz in Elixir
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/elixir/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/elixir/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Elixir](https://sampleprograms.io/languages/elixir) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```elixir
1..100
|> Enum.map(fn
  n when rem(n, 3) == 0 and rem(n, 5) == 0 -> "FizzBuzz"
  n when rem(n, 3) == 0 -> "Fizz"
  n when rem(n, 5) == 0 -> "Buzz"
  n -> Integer.to_string(n)
end)
|> Enum.each(&IO.puts/1)

```

{% endraw %}

Fizz Buzz in [Elixir](https://sampleprograms.io/languages/elixir) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).