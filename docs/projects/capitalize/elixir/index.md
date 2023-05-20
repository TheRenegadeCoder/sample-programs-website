---
title: Capitalize in Elixir
layout: default
date: 2020-10-06
featured-image: capitalize-in-every-language.jpg
last-modified: 2020-10-06

---

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Elixir](https://sampleprograms.io/languages/elixir) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```elixir
defmodule Capitalize do

    @doc """
    Capitalize the fitst entry of a list of strings and return the list as a single string.
    Return an error-string if the list is empty.

    Three cases of command line arguments:
        1. No argument / empty string -> return error string
        2. Single quoted string -> Assume fist word starts at index 0, capitalize first letter
        3. Multiple strings/words -> capitalize first word
    """
    def main([]) do "Usage: please provide a string" end
    def main([ "" | []]) do "Usage: please provide a string" end

    def main([ head | [] ]) do
        capitalize_word(head)
    end

    def main( [head | tail] ) do
        [ capitalize_word(head) | tail] |> Enum.join(" ") 
    end

    defp capitalize_word(word) do
        first_letter = String.first(word)
        first_letter_up = String.capitalize(first_letter)
        String.replace_prefix(word, first_letter, first_letter_up)
    end
end

Capitalize.main(System.argv()) |> IO.puts
```

{% endraw %}

[Capitalize](https://sampleprograms.io/projects/capitalize) in [Elixir](https://sampleprograms.io/languages/elixir) was written by:

- Jonas Halstrup

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).