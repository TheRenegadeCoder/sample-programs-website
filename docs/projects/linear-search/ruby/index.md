---
authors:
- Elvin Hrytsyuk
date: 2025-10-29
featured-image: linear-search-in-every-language.jpg
last-modified: 2025-10-29
layout: default
tags:
- linear-search
- ruby
title: Linear Search in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/linear-search/ruby/how-to-implement-the-solution.md
- sources/programs/linear-search/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Linear Search](https://sampleprograms.io/projects/linear-search) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
USAGE = 'Usage: please provide a list of integers ("1, 4, 5, 11, 12") and the integer to find ("11")'


    if ARGV.length < 2
        puts USAGE
        return
    end
    
    # the first input (list of numbers)
    list_input = ARGV[0]
    #second input (number to find)
    target_input = ARGV[1]

    #check if the input is empty
    if list_input.strip.empty? || target_input.strip.empty?
        puts USAGE
        return
    end

    begin
        #split list by the commas, trim the spaces, then turn into intgers
        numbers = list_input.split(',').map { |s| s.strip.to_i }

        #convert second number to integer
        target = Integer(target_input)
    rescue ArgumentError
        # if conversion fails we show the usage message
        puts USAGE
        return
    end

    #track if we find the number
    found = false

    # go through each number in the list
    numbers.each do |n|
        if n == target
            found = true
            # stop searching once we find it
            break
        end
    end

    # print result as true or false
    if found
        puts "true"
    else
        puts "false"
    end





```

{% endraw %}

Linear Search in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Elvin Hrytsyuk

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).