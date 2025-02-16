---
authors:
- HunterYates
date: 2025-02-16
featured-image: factorial-in-every-language.jpg
last-modified: 2025-02-16
layout: default
tags:
- crystal
- factorial
title: Factorial in Crystal
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/crystal/how-to-implement-the-solution.md
- sources/programs/factorial/crystal/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Crystal](https://sampleprograms.io/languages/crystal) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```crystal
begin
  if ARGV.empty?
    raise "Usage: please input a non-negative integer"
  end

  input = ARGV[0].to_i?

  if input.nil?
    raise "Usage: please input a non-negative integer"
  end

  input = input.not_nil!

  if input >= 0 && input <= 12
    puts factorial(input)
  elsif input > 12
    raise "#{input} is out of the reasonable bounds for calculation."
  else
    raise "Usage: please input a non-negative integer"
  end

rescue e
  puts e.message
end

def factorial(n)
  return 1 if n == 0
  n * factorial(n - 1)
end
```

{% endraw %}

Factorial in [Crystal](https://sampleprograms.io/languages/crystal) was written by:

- HunterYates

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).