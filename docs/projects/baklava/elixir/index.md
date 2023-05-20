---
title: Baklava in Elixir
layout: default
date: 2019-05-22
featured-image: baklava-in-every-language.jpg
last-modified: 2019-05-22

---

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Elixir](https://sampleprograms.io/languages/elixir) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```elixir
defmodule Baklava do
  @doc """
  Create baklava where the top has 10 spaces and then 1 asterisk.
  """
  @spec baklava() :: String.t()
  def baklava, do: baklava_grow(10, 1)

  @doc """
  Recursively grow the baklava until spaces <= zero.
  """
  @spec baklava_grow(spaces :: integer, asterisks :: integer) :: String.t()
  def baklava_grow(spaces, asterisks) when spaces <= 0 do
    line(0, asterisks) <> "\n" <> baklava_shrink(1, asterisks - 2)
  end

  def baklava_grow(spaces, asterisks) do
    line(spaces, asterisks) <> "\n" <> baklava_grow(spaces - 1, asterisks + 2)
  end

  @doc """
  Recursively shrink the baklava until asterisks <= zero.
  """
  @spec baklava_shrink(spaces :: integer, asterisks :: integer) :: String.t()
  def baklava_shrink(spaces, asterisks) when asterisks <= 1, do: line(spaces, 1)

  def baklava_shrink(spaces, asterisks) do
    line(spaces, asterisks) <> "\n" <> baklava_shrink(spaces + 1, asterisks - 2)
  end

  @doc """
  Return a single line of the baklava.
  """
  @spec line(spaces :: integer, asterisks :: integer) :: String.t()
  def line(spaces, asterisks) do
    String.duplicate(" ", spaces) <> String.duplicate("*", asterisks)
  end
end

Baklava.baklava() |> IO.puts()
```

{% endraw %}

[Baklava](https://sampleprograms.io/projects/baklava) in [Elixir](https://sampleprograms.io/languages/elixir) was written by:

- Oleksii Filonenko

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).