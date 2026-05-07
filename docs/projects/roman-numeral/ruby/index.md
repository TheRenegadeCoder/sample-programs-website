---
authors:
- Allan Klaus
- Ștefan-Iulian Alecu
date: 2020-10-06
featured-image: roman-numeral-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- roman-numeral
- ruby
title: Roman Numeral in Ruby
title1: Roman Numeral
title2: in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/roman-numeral/ruby/how-to-implement-the-solution.md
- sources/programs/roman-numeral/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
ROMAN = {
  "I" => 1, "V" => 5, "X" => 10, "L" => 50,
  "C" => 100, "D" => 500, "M" => 1000
}.freeze

USAGE = "Usage: please provide a string of roman numerals"
ERROR = "Error: invalid string of roman numerals"

def valid_roman?(s)
  return false unless s.match?(/\A[IVXLCDM]+\z/)

  # no more than 3 repeats
  return false if s.match?(/(.)\1{3,}/)

  # invalid repeatables
  %w[V L D].each { |ch| return false if s.include?(ch * 2) }

  true
end

def roman_to_int(s)
  return USAGE if s.nil?

  s = s.upcase
  return 0 if s.empty?
  return ERROR unless valid_roman?(s)

  total = 0

  s.chars.each_cons(2) do |a, b|
    total += (ROMAN[a] < ROMAN[b]) ? -ROMAN[a] : ROMAN[a]
  end

  total + ROMAN[s[-1]]
end

puts roman_to_int(ARGV.first)

```

{% endraw %}

Roman Numeral in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Allan Klaus
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).