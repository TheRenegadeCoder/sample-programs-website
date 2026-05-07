---
authors:
- Mallikarjuna S J
- Ștefan-Iulian Alecu
date: 2019-10-31
featured-image: even-odd-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- even-odd
- ruby
title: Even Odd in Ruby
title1: Even Odd
title2: in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/ruby/how-to-implement-the-solution.md
- sources/programs/even-odd/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
input = ARGV.first

abort("Usage: please input a number") if input.nil? || input.strip.empty?

begin
  num = Integer(input)
  puts num.even? ? "Even" : "Odd"
rescue ArgumentError
  warn "Usage: please input a number"
end

```

{% endraw %}

Even Odd in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Mallikarjuna S J
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).