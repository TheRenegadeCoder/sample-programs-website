---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: factorial-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- factorial
- ruby
title: Factorial in Ruby
title1: Factorial
title2: in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/ruby/how-to-implement-the-solution.md
- sources/programs/factorial/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
def usage!
  abort("Usage: please input a non-negative integer")
end

input = ARGV.first

usage! if input.nil? || input.strip.empty?

begin
  num = Integer(input)
rescue ArgumentError
  usage!
end

usage! if num.negative?

puts (1..num).reduce(1, :*)

```

{% endraw %}

Factorial in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).