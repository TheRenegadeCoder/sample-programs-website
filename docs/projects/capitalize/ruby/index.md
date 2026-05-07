---
authors:
- Couraxe
- Ștefan-Iulian Alecu
date: 2020-10-08
featured-image: capitalize-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- capitalize
- ruby
title: Capitalize in Ruby
title1: Capitalize
title2: in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/ruby/how-to-implement-the-solution.md
- sources/programs/capitalize/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
def capitalize_str(str)
  return str if str.empty?

  str[0].upcase + str[1..]
end

input = ARGV.first.to_s

if input.strip.empty?
  warn "Usage: please provide a string"
else
  puts capitalize_str(input)
end

```

{% endraw %}

Capitalize in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Couraxe
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).