---

title: Fizz Buzz in Elixir
layout: default
date: 2022-04-28
last-modified: 2022-05-10

---

Welcome to the Fizz Buzz in Elixir page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).