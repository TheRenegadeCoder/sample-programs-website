---
authors:
- reetansingh
- Ștefan-Iulian Alecu
date: 2025-03-26
featured-image: longest-word-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- longest-word
- ruby
title: Longest Word in Ruby
title1: Longest Word
title2: in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/ruby/how-to-implement-the-solution.md
- sources/programs/longest-word/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
input = ARGV.join(" ").strip

abort("Usage: please provide a string") if input.empty?

puts input.split.map(&:length).max

```

{% endraw %}

Longest Word in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- reetansingh
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).