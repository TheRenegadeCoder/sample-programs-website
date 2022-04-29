---

title: Factorial in Elixir
layout: default
date: 2022-04-28
last-modified: 2022-04-28

---

Welcome to the Factorial in Elixir page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Elixir
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.