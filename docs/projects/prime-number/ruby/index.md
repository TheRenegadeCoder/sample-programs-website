---
authors:
- MSJ
date: 2024-10-02
featured-image: prime-number-in-every-language.jpg
last-modified: 2024-10-02
layout: default
tags:
- prime-number
- ruby
title: Prime Number in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/ruby/how-to-implement-the-solution.md
- sources/programs/prime-number/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
# check if input is a valid prime number or a valid composite number
# if number is 0, 1 or even, print composite
#
# begin validations for empty input, non-number and negative number
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
# Begin Edge cases
  if num == 0 || num == 1
    print("composite")
  elsif num == 2
    print("prime")
  elsif num % 2 == 0
    print("composite")
# End Edge cases
  else
  # Logic
  
  i = 3
  is_prime = true
  while i <= Math.sqrt(num)
    if num % i == 0
      is_prime = false
    end
    i += 2
  end
  if is_prime ==true
    print("prime")
  else
    print("composite")
  end
  end
end

```

{% endraw %}

Prime Number in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- MSJ

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).