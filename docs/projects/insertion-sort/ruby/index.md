---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-14
featured-image: insertion-sort-in-every-language.jpg
last-modified: 2026-05-14
layout: default
tags:
- insertion-sort
- ruby
title: Insertion Sort in Ruby
title1: Insertion
title2: Sort in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/insertion-sort/ruby/how-to-implement-the-solution.md
- sources/programs/insertion-sort/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Insertion Sort](/projects/insertion-sort) in [Ruby](/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
# frozen_string_literal: true

class Array
  def insertion_sort!
    (1...length).each do |i|
      value = self[i]
      j = i - 1

      while j >= 0 && self[j] > value
        self[j + 1] = self[j]
        j -= 1
      end

      self[j + 1] = value
    end

    self
  end
end

def usage!
  abort %(Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5")
end

def parse_input
  raw = ARGV.first
  usage! if raw.nil? || raw.strip.empty?

  numbers = raw.split(",").map { Integer(it.strip) }
  usage! if numbers.length < 2

  numbers
rescue ArgumentError
  usage!
end

puts parse_input.insertion_sort!.join(", ")

```

{% endraw %}

Insertion Sort in [Ruby](/languages/ruby) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).