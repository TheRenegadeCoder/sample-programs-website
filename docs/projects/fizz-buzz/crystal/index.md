---
authors:
- Noah Nichols
date: 2018-09-26
featured-image: fizz-buzz-in-every-language.png
last-modified: 2018-09-26
layout: default
tags:
- crystal
- fizz-buzz
title: Fizz Buzz in Crystal
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/crystal/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/crystal/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Crystal](https://sampleprograms.io/languages/crystal) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```crystal
i = 1
while i < 101
  if i % 3 == 0 && i % 5 == 0
    puts "FizzBuzz"
  elsif i % 3 == 0
    puts "Fizz"
  elsif i % 5 == 0
    puts "Buzz"
  else
    puts i
  end
  i = i + 1
end
```

{% endraw %}

Fizz Buzz in [Crystal](https://sampleprograms.io/languages/crystal) was written by:

- Noah Nichols

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).