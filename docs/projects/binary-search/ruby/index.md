---
authors:
- Tyler Gilmore
date: 2024-11-09
featured-image: binary-search-in-every-language.jpg
last-modified: 2024-11-09
layout: default
tags:
- binary-search
- ruby
title: Binary Search in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/binary-search/ruby/how-to-implement-the-solution.md
- sources/programs/binary-search/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Binary Search](https://sampleprograms.io/projects/binary-search) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
def binary_search(array, key)
    left = 0
    right = array.length - 1

    while (left <= right)
        mid = (left + right) / 2

        if (array[mid] == key)
            return "true"
        elsif(array[mid] < key)
            left = mid + 1
        else
            right = mid - 1
        end
    end
    return "false"
end

# Validation of inputs
if ARGV.length != 2 || ARGV[0].empty? || ARGV[1].empty?
    puts 'Usage: please provide a list of sorted integers ("1, 4, 5, 11, 12") and the integer to find ("11")'
else
    array = ARGV[0].split(',').map(&:strip).map(&:to_i)
    key = ARGV[1].to_i
    
    if array != array.sort
        puts 'Usage: please provide a list of sorted integers ("1, 4, 5, 11, 12") and the integer to find ("11")'
    else
        puts binary_search(array, key)
    end
end
```

{% endraw %}

Binary Search in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Tyler Gilmore

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).