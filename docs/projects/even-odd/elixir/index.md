---
title: Even Odd in Elixir
layout: default
date: 2020-10-03
featured-image: even-odd-in-every-language.jpg
last-modified: 2020-10-03

---

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Elixir](https://sampleprograms.io/languages/elixir) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```elixir
defmodule EvenOdd do
    require Integer

    @doc """
    Determine whether a supplied number is Even or Odd.
    Return an error-string if the argument is missing or invalid. 
    """
    @spec main(argv :: list( String.t())) :: String.t()
    def main(argv) do
        if length(argv) != 1 do
            "Usage: please input a number"
        else 
            case argv |> List.first |> Integer.parse do
                {number, ""} -> even_odd_string(number)
                {_, _rest} -> "Usage: please input a number"
                :error -> "Usage: please input a number"
            end
        end
    end

    @spec even_odd_string(number :: integer) :: String.t()
    defp even_odd_string(number) do
        case Integer.is_even(number) do
            true -> "Even"
            false -> "Odd"
        end
    end
end

EvenOdd.main(System.argv()) |> IO.puts
```

{% endraw %}

[Even Odd](https://sampleprograms.io/projects/even-odd) in [Elixir](https://sampleprograms.io/languages/elixir) was written by:

- Zapnuk

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 04 2020 23:28:49. The solution was first committed on Oct 03 2020 02:22:00. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).