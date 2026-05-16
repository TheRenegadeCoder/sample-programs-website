---
authors:
- MSJ
- Ștefan-Iulian Alecu
date: 2024-10-31
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- duplicate-character-counter
- ruby
title: Duplicate Character Counter in Ruby
title1: Duplicate Character
title2: Counter in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/ruby/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
input = ARGV.first.to_s

abort("Usage: please provide a string") if input.empty?

duplicates = input.each_char.tally.select { _2 > 1 }

if duplicates.empty?
  puts "No duplicate characters"
  return
end

duplicates.each { |char, count| puts "#{char}: #{count}" }

```

{% endraw %}

Duplicate Character Counter in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- MSJ
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).