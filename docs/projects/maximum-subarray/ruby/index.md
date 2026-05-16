---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-14
featured-image: maximum-subarray-in-every-language.jpg
last-modified: 2026-05-14
layout: default
tags:
- maximum-subarray
- ruby
title: Maximum Subarray in Ruby
title1: Maximum Subarray
title2: in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-subarray/ruby/how-to-implement-the-solution.md
- sources/programs/maximum-subarray/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Subarray](https://sampleprograms.io/projects/maximum-subarray) in [Ruby](https://sampleprograms.io/languages/ruby)! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
# frozen_string_literal: true

USAGE = 'Usage: Please provide a list of integers in the format: "1, 2, 3, 4, 5"'

def usage!
  warn USAGE
  exit 1
end

def parse_list(str)
  str.split(",").map { Integer(it.strip) }
rescue ArgumentError, NoMethodError
  usage!
end

def max_subarray_sum(arr)
  return arr.first if arr.length == 1
  return arr.sum if arr.none?(&:negative?)

  current = max = arr.first

  arr[1..].each do |x|
    current = [x, current + x].max
    max = [max, current].max
  end

  max
end

raw = ARGV.first
usage! if raw.nil? || raw.strip.empty?

arr = parse_list(raw)
usage! if arr.length < 1

puts max_subarray_sum(arr)

```

{% endraw %}

Maximum Subarray in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).