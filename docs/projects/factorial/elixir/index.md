---
authors:
- Jeremy Grifski
- Parker Johansen
- pearl2201
date: 2019-10-12
featured-image: factorial-in-every-language.jpg
last-modified: 2019-10-16
layout: default
tags:
- elixir
- factorial
title: Factorial in Elixir
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/elixir/how-to-implement-the-solution.md
- sources/programs/factorial/elixir/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Elixir](https://sampleprograms.io/languages/elixir) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```elixir
defmodule Factorial do
  def main(args) do
    args
    |> List.first
    |> as_integer
    |> get
    |> IO.puts()
  end

  def get(0, acc) do
    acc
  end

  def get(n, acc) do
    get(n - 1, acc * n)
  end

  def get(n) when not is_integer(n) or n < 0 do
    "Usage: please input a non-negative integer"
  end

  def get(n) do
    get(n, 1)
  end

  def as_integer(n) do
    try do
        String.to_integer(n)
    rescue
        ArgumentError -> -1
    end
  end
end

Factorial.main(System.argv())

```

{% endraw %}

Factorial in [Elixir](https://sampleprograms.io/languages/elixir) was written by:

- Jeremy Grifski
- Parker Johansen
- pearl2201

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).