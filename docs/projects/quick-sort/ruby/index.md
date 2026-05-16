---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-14
featured-image: quick-sort-in-every-language.jpg
last-modified: 2026-05-14
layout: default
tags:
- quick-sort
- ruby
title: Quick Sort in Ruby
title1: Quick Sort
title2: in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/quick-sort/ruby/how-to-implement-the-solution.md
- sources/programs/quick-sort/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Quick Sort](https://sampleprograms.io/projects/quick-sort) in [Ruby](https://sampleprograms.io/languages/ruby)! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
# frozen_string_literal: true

def usage!
  abort %(Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5")
end

def parse_input
  raw = ARGV.first
  usage! if raw.nil? || raw.strip.empty?

  numbers = raw.split(",").map { Integer(it.strip) }
  usage! if numbers.length < 2

  numbers
rescue ArgumentError, NoMethodError
  usage!
end

def quicksort!(arr, lo = 0, hi = arr.length - 1)
  return arr if lo >= hi

  p = partition(arr, lo, hi)

  quicksort!(arr, lo, p - 1)
  quicksort!(arr, p + 1, hi)

  arr
end

def partition(arr, lo, hi)
  pivot = arr[hi]
  i = lo

  (lo...hi).each do |j|
    if arr[j] <= pivot
      arr[i], arr[j] = arr[j], arr[i]
      i += 1
    end
  end

  arr[i], arr[hi] = arr[hi], arr[i]
  i
end

numbers = parse_input
puts quicksort!(numbers).join(", ")

```

{% endraw %}

Quick Sort in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).