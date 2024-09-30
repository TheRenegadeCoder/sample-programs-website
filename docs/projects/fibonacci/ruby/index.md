---
authors:
- Noah Nichols
- Parker Johansen
date: 2018-10-14
featured-image: fibonacci-in-every-language.jpg
last-modified: 2019-04-07
layout: default
tags:
- fibonacci
- ruby
title: Fibonacci in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/ruby/how-to-implement-the-solution.md
- sources/programs/fibonacci/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
def fibonacci(number)
    a = 0
    b = 1
    c = 0

    i = 0
    while i < number
        c = a + b
        b = a
        a = c

        print("#{i+1}: #{c}\n")
        i += 1
    end
end

num = Integer(ARGV[0]) rescue -1
if num >= 0
    fibonacci(num)
else
    print("Usage: please input the count of fibonacci numbers to output")
end
```

{% endraw %}

Fibonacci in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Noah Nichols
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).