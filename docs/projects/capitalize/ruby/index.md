---
authors:
- Couraxe
date: 2020-10-08
featured-image: capitalize-in-every-language.jpg
last-modified: 2020-10-08
layout: default
tags:
- capitalize
- ruby
title: Capitalize in Ruby
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
    s = str.split(' ')
    s[0][0] = s[0][0].upcase
    s.join(' ')
end

if ARGV.length == 0 || ARGV[0] == ''
    puts 'Usage: please provide a string'
else
    puts capitalize_str(ARGV[0])
end

```

{% endraw %}

Capitalize in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Couraxe

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).