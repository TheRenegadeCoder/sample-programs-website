---
authors:
- AAshGray
- Ștefan-Iulian Alecu
date: 2025-02-15
featured-image: josephus-problem-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- josephus-problem
- ruby
title: Josephus Problem in Ruby
title1: Josephus Problem
title2: in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/josephus-problem/ruby/how-to-implement-the-solution.md
- sources/programs/josephus-problem/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Josephus Problem](https://sampleprograms.io/projects/josephus-problem) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
def josephus(n, k)
  (1..n).reduce(0) { |acc, i| (acc + k) % i } + 1
end

def usage!
  abort("Usage: please input the total number of people and number of people to skip.")
end

n, k = ARGV

usage! unless n && k
usage! unless n.match?(/\A\d+\z/) && k.match?(/\A\d+\z/)

n = n.to_i
k = k.to_i

puts josephus(n, k)

```

{% endraw %}

Josephus Problem in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- AAshGray
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).