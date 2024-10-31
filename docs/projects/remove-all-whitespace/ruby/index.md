---
authors:
- MSJ
date: 2024-10-31
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2024-10-31
layout: default
tags:
- remove-all-whitespace
- ruby
title: Remove All Whitespace in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/ruby/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
if ARGV.length == 0 || ARGV[0] == ''
  puts 'Usage: please provide a string'
else
  a = ARGV[0].gsub(/ /, '').gsub(/\t/, '').gsub(/\r/, '').gsub(/\n/, '')
  puts a
end

```

{% endraw %}

Remove All Whitespace in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- MSJ

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).