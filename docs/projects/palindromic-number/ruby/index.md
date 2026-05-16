---
authors:
- MSJ
- Ștefan-Iulian Alecu
date: 2024-10-02
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- palindromic-number
- ruby
title: Palindromic Number in Ruby
title1: Palindromic
title2: Number in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/ruby/how-to-implement-the-solution.md
- sources/programs/palindromic-number/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
def usage!
  abort("Usage: please input a non-negative integer")
end

number = Integer(ARGV.first, exception: false)

usage! if number.nil? || number.negative?

puts number.digits == number.digits.reverse

```

{% endraw %}

Palindromic Number in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- MSJ
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).