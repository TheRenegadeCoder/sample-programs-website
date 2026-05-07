---
authors:
- Jeremy Grifski
- Ștefan-Iulian Alecu
date: 2019-03-20
featured-image: bubble-sort-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- bubble-sort
- ruby
title: Bubble Sort in Ruby
title1: Bubble Sort
title2: in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/bubble-sort/ruby/how-to-implement-the-solution.md
- sources/programs/bubble-sort/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
class Array
  def bubble_sort
    arr = dup
    n = arr.length

    (n - 1).times do |i|
      swapped = false

      (n - i - 1).times do |j|
        next unless arr[j] > arr[j + 1]

        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        swapped = true
      end

      break unless swapped
    end

    arr
  end
end

def parse_input
  raw = ARGV.first
  raise ArgumentError unless raw

  numbers = raw.split(",").map { Integer(it.strip, exception: false) }
  raise ArgumentError if numbers.any?(nil) || numbers.length < 2

  numbers
end

def usage!
  abort %(Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5")
end

begin
  numbers = parse_input
  puts numbers.bubble_sort.join(", ")
rescue ArgumentError
  usage!
end

```

{% endraw %}

Bubble Sort in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Jeremy Grifski
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).