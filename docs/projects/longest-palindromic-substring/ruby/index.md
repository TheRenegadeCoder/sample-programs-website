---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-24
featured-image: longest-palindromic-substring-in-every-language.jpg
last-modified: 2026-04-24
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
def expand_from_center(s, left, right)
  while left >= 0 && right < s.length && s[left] == s[right]
    left -= 1
    right += 1
  end
  s[(left + 1)...right]
end

def longest_palindromic_substring(s)
  abort "Usage: please provide a string that contains at least one palindrome" if s.to_s.empty?

  longest = ""

  s.length.times do |i|
    odd  = expand_from_center(s, i, i)
    even = expand_from_center(s, i, i + 1)

    longest = odd  if odd.length  > longest.length
    longest = even if even.length > longest.length
  end

  abort "Usage: please provide a string that contains at least one palindrome" if longest.length <= 1

  puts longest
end

input = ARGV.first
longest_palindromic_substring(input)
```

{% endraw %}

Longest Palindromic Substring in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).