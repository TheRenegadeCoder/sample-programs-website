---
authors:
- Noah Nichols
- Ștefan-Iulian Alecu
date: 2018-10-14
featured-image: fibonacci-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- fibonacci
- ruby
title: Fibonacci in Ruby
title1: Fibonacci
title2: in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/ruby/how-to-implement-the-solution.md
- sources/programs/fibonacci/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
def usage!
  abort("Usage: please input the count of fibonacci numbers to output")
end

def fibonacci(n)
  a, b = 1, 1

  n.times do |i|
    puts "#{i + 1}: #{a}"
    a, b = b, a + b
  end
end

input = ARGV.first
usage! if input.nil? || input.strip.empty?

begin
  num = Integer(input)
rescue ArgumentError
  usage!
end

usage! if num.negative?

fibonacci(num)

```

{% endraw %}

Fibonacci in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Noah Nichols
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).