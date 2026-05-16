---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-14
featured-image: longest-common-subsequence-in-every-language.jpg
last-modified: 2026-05-14
layout: default
tags:
- longest-common-subsequence
- ruby
title: Longest Common Subsequence in Ruby
title1: Longest Common
title2: Subsequence in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-common-subsequence/ruby/how-to-implement-the-solution.md
- sources/programs/longest-common-subsequence/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Common Subsequence](https://sampleprograms.io/projects/longest-common-subsequence) in [Ruby](https://sampleprograms.io/languages/ruby)! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
# frozen_string_literal: true

USAGE = 'Usage: please provide two lists in the format "1, 2, 3, 4, 5"'

def usage!
  warn USAGE
  exit 1
end

def parse_list(str)
  str.split(",").map { Integer(it.strip) }
rescue ArgumentError, NoMethodError
  usage!
end

def lcs(a, b)
  n = a.size
  m = b.size

  dp = Array.new(n + 1) { Array.new(m + 1, 0) }

  (1..n).each do |i|
    (1..m).each do |j|
      dp[i][j] = if a[i - 1] == b[j - 1]
        dp[i - 1][j - 1] + 1
      else
        [dp[i - 1][j], dp[i][j - 1]].max
      end
    end
  end

  i, j = n, m
  result = []

  while i > 0 && j > 0
    if a[i - 1] == b[j - 1]
      result << a[i - 1]
      i -= 1
      j -= 1
    elsif dp[i - 1][j] >= dp[i][j - 1]
      i -= 1
    else
      j -= 1
    end
  end

  result.reverse
end

a_str, b_str = ARGV
usage! if a_str.nil? || b_str.nil? || a_str.strip.empty? || b_str.strip.empty?

a = parse_list(a_str)
b = parse_list(b_str)

puts lcs(a, b).join(", ")

```

{% endraw %}

Longest Common Subsequence in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).