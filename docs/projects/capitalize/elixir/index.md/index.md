# Capitalize in Elixir

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Elixir
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.