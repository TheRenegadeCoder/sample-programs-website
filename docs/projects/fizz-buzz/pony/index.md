---
authors:
- Zia
date: 2025-01-19
featured-image: fizz-buzz-in-every-language.png
last-modified: 2025-01-19
layout: default
tags:
- fizz-buzz
- pony
title: Fizz Buzz in Pony
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/pony/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/pony/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Pony](https://sampleprograms.io/languages/pony) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pony
use "collections"

actor Main
  new create(env: Env) =>
    for i in Range[I32](1, 101) do
      env.out.print(fizzbuzz(i))
    end

  fun fizzbuzz(n: I32): String =>
    if (n % 15) == 0 then
      "FizzBuzz"
    elseif (n % 5) == 0 then
      "Buzz"
    elseif (n % 3) == 0 then
      "Fizz"
    else
      n.string()
    end

```

{% endraw %}

Fizz Buzz in [Pony](https://sampleprograms.io/languages/pony) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).