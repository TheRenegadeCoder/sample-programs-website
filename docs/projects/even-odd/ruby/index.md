---
authors:
- Mallikarjuna S J
date: 2019-10-31
featured-image: even-odd-in-every-language.jpg
last-modified: 2019-11-04
layout: default
tags:
- even-odd
- ruby
title: Even Odd in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/ruby/how-to-implement-the-solution.md
- sources/programs/even-odd/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
# Requirement https://sample-programs.therenegadecoder.com/projects/even-odd/
# Issue 1839

if ARGV.empty?
# if ARGV.length < 1
    puts "Usage: please input a number"
    exit
else
    # if ARGV.empty?
    #     puts "Usage: please input a number"
    # end
    begin
    string1 = ARGV[0]
    num = Integer(string1)
    rescue ArgumentError
    puts "Usage: please input a number"
    exit
    end

    if num % 2 == 0
    	puts "Even"
    else
    	puts "Odd"
    end
end

```

{% endraw %}

Even Odd in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Mallikarjuna S J

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).