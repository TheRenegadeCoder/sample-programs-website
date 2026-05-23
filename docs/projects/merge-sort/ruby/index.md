---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-14
featured-image: merge-sort-in-every-language.jpg
last-modified: 2026-05-14
layout: default
tags:
- merge-sort
- ruby
title: Merge Sort in Ruby
title1: Merge Sort
title2: in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/merge-sort/ruby/how-to-implement-the-solution.md
- sources/programs/merge-sort/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Merge Sort](/projects/merge-sort) in [Ruby](/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

def merge_sort(arr)
  return arr if arr.length <= 1

  mid = arr.length / 2
  left = merge_sort(arr[0...mid])
  right = merge_sort(arr[mid..])

  merge(left, right)
end

def merge(left, right)
  i = 0
  j = 0
  result = []

  while i < left.length && j < right.length
    if left[i] <= right[j]
      result << left[i]
      i += 1
    else
      result << right[j]
      j += 1
    end
  end

  result.concat(left[i..] || [])
  result.concat(right[j..] || [])
  result
end

numbers = parse_input
puts merge_sort(numbers).join(", ")

```

{% endraw %}

Merge Sort in [Ruby](/languages/ruby) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).