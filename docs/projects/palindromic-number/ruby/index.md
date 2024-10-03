---
authors:
- MSJ
date: 2024-10-02
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2024-10-02
layout: default
tags:
- palindromic-number
- ruby
title: Palindromic Number in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/ruby/how-to-implement-the-solution.md
- sources/programs/palindromic-number/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
# print true, if input is a non-negative palindrome number
if ARGV.empty?
  puts "Usage: please input a non-negative integer"
  exit
else
  begin
    string1 = ARGV[0]
    num = Integer(string1)
    rescue ArgumentError
    puts "Usage: please input a non-negative integer"
    exit
  end
  if num < 0
    puts "Usage: please input a non-negative integer"
    exit    
  end
# end validations for empty input, non-number and negative number
  reverse_no = 0
  save = num 
  while (save > 0)

      last_digit = save % 10 
      reverse_no = (reverse_no *10) + last_digit
      save /=10     
  end
  if num == reverse_no
      print("true")
  else
      print("false")
  end

end

```

{% endraw %}

Palindromic Number in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- MSJ

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).