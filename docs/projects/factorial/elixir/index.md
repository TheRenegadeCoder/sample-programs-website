---

title: Factorial in Elixir
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Factorial in Elixir page! Here, you'll find the source code for this program as well as a description of how the program works.

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

Factorial in Elixir was written by:

- Parker Johansen
- Jeremy Grifski
- pearl2201

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 16 2019 14:19:14. The solution was first committed on Oct 12 2019 09:32:34. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).