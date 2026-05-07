---
authors:
- Tyler Gilmore
- Ștefan-Iulian Alecu
date: 2024-11-09
featured-image: binary-search-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- binary-search
- ruby
title: Binary Search in Ruby
title1: Binary Search
title2: in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/binary-search/ruby/how-to-implement-the-solution.md
- sources/programs/binary-search/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Binary Search](https://sampleprograms.io/projects/binary-search) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
module Enumerable
  def sorted?
    each_cons(2).all? { |a, b| (a <=> b) <= 0 }
  end
end

def parse_args
  list, key = ARGV
  raise ArgumentError unless list && key

  parts = list.split(",").map(&:strip)
  raise ArgumentError if parts.empty? || parts.any?(&:empty?)

  numbers = parts.map { Integer(it, exception: false) }
  raise ArgumentError if numbers.any?(nil)

  key = Integer(key, exception: false)
  raise ArgumentError if key.nil?

  raise ArgumentError unless numbers.sorted?

  [numbers, key]
end

begin
  numbers, key = parse_args
  puts !numbers.bsearch { key <=> it }.nil?
rescue ArgumentError
  warn 'Usage: please provide a list of sorted integers ("1, 4, 5, 11, 12") and the integer to find ("11")'
end

```

{% endraw %}

Binary Search in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Tyler Gilmore
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).