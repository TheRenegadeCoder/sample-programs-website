---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-24
featured-image: longest-palindromic-substring-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- longest-palindromic-substring
- ruby
title: Longest Palindromic Substring in Ruby
title1: Longest Palindromic
title2: Substring in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-palindromic-substring/ruby/how-to-implement-the-solution.md
- sources/programs/longest-palindromic-substring/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Palindromic Substring](https://sampleprograms.io/projects/longest-palindromic-substring) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
def expand(s, l, r)
  while l >= 0 && r < s.length && s[l] == s[r]
    l -= 1
    r += 1
  end

  [l + 1, r - l - 1] # start, length
end

def longest_palindromic_substring(s)
  return if s.to_s.empty?

  best_start = 0
  best_len = 1

  s.length.times do |i|
    start1, len1 = expand(s, i, i)
    start2, len2 = expand(s, i, i + 1)

    start, len = (len1 > len2) ? [start1, len1] : [start2, len2]

    if len > best_len
      best_start, best_len = start, len
    end
  end

  s.slice(best_start, best_len)
end

input = ARGV.first
result = longest_palindromic_substring(input)

abort("Usage: please provide a string that contains at least one palindrome") if result.nil? || result.length <= 1

puts result

```

{% endraw %}

Longest Palindromic Substring in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).