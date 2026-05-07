---
authors:
- Ahmed
- Ștefan-Iulian Alecu
date: 2025-10-29
featured-image: selection-sort-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- ruby
- selection-sort
title: Selection Sort in Ruby
title1: Selection
title2: Sort in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/selection-sort/ruby/how-to-implement-the-solution.md
- sources/programs/selection-sort/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Selection Sort](https://sampleprograms.io/projects/selection-sort) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
def parse_input(str)
  return if str.to_s.strip.empty?

  nums = str.split(",").map { Integer(it.strip, exception: false) }
  return if nums.any?(nil?) || nums.length < 2

  nums
end

class Array
  def selection_sort
    arr = dup
    sorted = []

    until arr.empty?
      min_index = arr.each_index.min_by { |i| arr[i] }
      sorted << arr.delete_at(min_index)
    end

    sorted
  end
end

USAGE = 'Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"'

input = parse_input(ARGV.first)
abort(USAGE) unless input

puts input.selection_sort.join(", ")

```

{% endraw %}

Selection Sort in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Ahmed
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).