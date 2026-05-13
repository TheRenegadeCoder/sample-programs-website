---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-14
featured-image: maximum-array-rotation-in-every-language.jpg
last-modified: 2026-05-14
layout: default
tags:
- maximum-array-rotation
- ruby
title: Maximum Array Rotation in Ruby
title1: Maximum Array
title2: Rotation in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-array-rotation/ruby/how-to-implement-the-solution.md
- sources/programs/maximum-array-rotation/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Array Rotation](https://sampleprograms.io/projects/maximum-array-rotation) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
# frozen_string_literal: true

USAGE = 'Usage: please provide a list of integers (e.g. "8, 3, 1, 2")'

def usage!
  warn USAGE
  exit 1
end

def parse_list(str)
  str.split(",").map { Integer(it.strip) }
rescue ArgumentError, NoMethodError
  usage!
end

def max_rotation_sum(arr)
  n = arr.size
  total_sum = arr.sum
  current = arr.each_with_index.sum { |v, i| i * v }

  max = current

  (1...n).each do |i|
    last = arr[n - i]
    current += total_sum - n * last
    max = current if current > max
  end

  max
end

raw = ARGV.first
usage! if raw.nil? || raw.strip.empty?

arr = parse_list(raw)

puts max_rotation_sum(arr)

```

{% endraw %}

Maximum Array Rotation in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).