---
authors:
- MSJ
- Ștefan-Iulian Alecu
date: 2024-10-02
featured-image: prime-number-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- prime-number
- ruby
title: Prime Number in Ruby
title1: Prime Number
title2: in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/ruby/how-to-implement-the-solution.md
- sources/programs/prime-number/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
require "prime"

def usage!
  abort("Usage: please input a non-negative integer")
end

number = Integer(ARGV.first, exception: false)

usage! if number.nil? || number.negative?

puts Prime.prime?(number) ? "prime" : "composite"

```

{% endraw %}

Prime Number in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- MSJ
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).