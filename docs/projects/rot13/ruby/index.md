---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-14
featured-image: rot13-in-every-language.jpg
last-modified: 2026-05-14
layout: default
tags:
- rot13
- ruby
title: Rot13 in Ruby
title1: Rot13
title2: in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/ruby/how-to-implement-the-solution.md
- sources/programs/rot13/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
# frozen_string_literal: true

USAGE = "Usage: please provide a string to encrypt"

def usage!
  warn USAGE
  exit 1
end

def rot13(str)
  str.tr("A-Za-z", "N-ZA-Mn-za-m")
end

input = ARGV.first
usage! if input.nil? || input.strip.empty?

puts rot13(input)

```

{% endraw %}

Rot13 in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).