---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-14
featured-image: zeckendorf-in-every-language.png
last-modified: 2026-05-14
layout: default
tags:
- ruby
- zeckendorf
title: Zeckendorf in Ruby
title1: Zeckendorf
title2: in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/zeckendorf/ruby/how-to-implement-the-solution.md
- sources/programs/zeckendorf/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Zeckendorf](/projects/zeckendorf) in [Ruby](/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
# frozen_string_literal: true

USAGE = "Usage: please input a non-negative integer"

def usage!
  warn USAGE
  exit 1
end

def parse_input(str)
  usage! if str.nil? || str.strip.empty?

  n = Integer(str)
  usage! if n < 0

  n
rescue ArgumentError, NoMethodError
  usage!
end

def fibs_upto(n)
  fibs = [1, 2]
  fibs << fibs[-1] + fibs[-2] while fibs[-1] <= n
  fibs.pop if fibs[-1] > n
  fibs
end

def zeckendorf(n)
  return [] if n == 0

  fibs = fibs_upto(n)
  result = []

  i = fibs.length - 1

  while n > 0
    if fibs[i] <= n
      result << fibs[i]
      n -= fibs[i]
      i -= 2
    else
      i -= 1
    end
  end

  result
end

input = ARGV.first
n = parse_input(input)

puts zeckendorf(n).join(", ")

```

{% endraw %}

Zeckendorf in [Ruby](/languages/ruby) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).