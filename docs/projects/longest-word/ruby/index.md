---
authors:
- reetansingh
date: 2025-03-26
featured-image: longest-word-in-every-language.jpg
last-modified: 2025-03-26
layout: default
tags:
- longest-word
- ruby
title: Longest Word in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/ruby/how-to-implement-the-solution.md
- sources/programs/longest-word/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
input_str = ARGV.join(" ").strip 

if input_str.empty?
   puts "Usage: please provide a string"
    exit
  end

  words = input_str.split
        max_length = 0

        words.each do |word|
            if word.length > max_length
              max_length = word.length
            end
          end
          
          puts max_length

```

{% endraw %}

Longest Word in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- reetansingh

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).