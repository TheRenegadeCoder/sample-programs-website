---
authors:
- Ann
- Jeremy Grifski
date: 2019-10-14
featured-image: longest-common-subsequence-in-every-language.jpg
last-modified: 2019-10-16
layout: default
tags:
- elixir
- longest-common-subsequence
title: Longest Common Subsequence in Elixir
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-common-subsequence/elixir/how-to-implement-the-solution.md
- sources/programs/longest-common-subsequence/elixir/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Common Subsequence](https://sampleprograms.io/projects/longest-common-subsequence) in [Elixir](https://sampleprograms.io/languages/elixir) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```elixir
defmodule LongestCommonSubsequence do
  def main() do
    lcs = solve(System.argv())
    IO.puts("#{lcs}")
  end

  def solve([as, bs]) when is_bitstring(as) and is_bitstring(bs) do
    lcs(parse_string_to_list_integer(as), parse_string_to_list_integer(bs)) |> Enum.join(", ")
  end

  def solve(_) do
    print_usage()
  end

  def print_usage() do
    ~s(Usage: please provide two lists in the format "1, 2, 3, 4, 5")
  end

  def lcs([], _) do
    []
  end

  def lcs(_, []) do
    []
  end

  def lcs([a | as], [b | bs]) when a == b do
    [a] ++ lcs(as, bs)
  end

  def lcs([a | as], [b | bs]) do
    longest(lcs(as, [b | bs]), lcs([a | as], bs))
  end

  def longest(l1, l2) do
    if Enum.count(l1) > Enum.count(l2) do
      l1
    else
      l2
    end
  end

  def parse_string_to_list_integer(xs) do
    xs
    |> String.trim()
    |> String.split(",")
    |> Enum.map(&String.to_integer(String.trim(&1)))
  end
end

LongestCommonSubsequence.main()

```

{% endraw %}

Longest Common Subsequence in [Elixir](https://sampleprograms.io/languages/elixir) was written by:

- Ann
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).