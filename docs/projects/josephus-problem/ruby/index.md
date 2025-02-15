---
authors:
- AAshGray
date: 2025-02-15
featured-image: josephus-problem-in-every-language.jpg
last-modified: 2025-02-15
layout: default
tags:
- josephus-problem
- ruby
title: Josephus Problem in Ruby
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
def josephus_problem(array, k, start)
    if (array.length == 1)
      # if the array is one item left, return the survivor value
      puts array[0]
    else
        # set the index position (start + (k - 1)) and set wrap with %
        index = (start + k - 1)
        wrap = index % array.length
        array.delete_at(wrap)
        return josephus_problem(array, k, wrap)
    end
end

def error()
    puts "Usage: please input the total number of people and number of people to skip."
end

# check for incorrect number of arguments
# .any? loops over the elements of ARGV to check if the argument contains non-digit characters or empty strings
if ARGV.length != 2 || ARGV.any? { |arg| arg.match(/[^0-9]/) || arg.empty? }
    error()
else
    # convert the arguments to integers
    n = ARGV[0].to_i
    k = ARGV[1].to_i

    # create an array with a length of argument n
    array = [*1..n]

    # pass our array to the function with k and our start index (0)
    josephus_problem(array, k, 0)
end
```

{% endraw %}

Josephus Problem in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- AAshGray

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).