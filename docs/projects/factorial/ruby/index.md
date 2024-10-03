---
authors:
- MSJ
date: 2024-10-02
featured-image: factorial-in-every-language.jpg
last-modified: 2024-10-02
layout: default
tags:
- factorial
- ruby
title: Factorial in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/ruby/how-to-implement-the-solution.md
- sources/programs/factorial/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
# return factorial of a non-negative number
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
  i = 1
  factorial = 1
  while i <= num
    factorial = factorial * i
    i += 1
  end
  print(factorial)
end  

```

{% endraw %}

Factorial in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- MSJ

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).