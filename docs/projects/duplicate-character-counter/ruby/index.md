---
authors:
- MSJ
date: 2024-10-31
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2024-10-31
layout: default
tags:
- duplicate-character-counter
- ruby
title: Duplicate Character Counter in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/ruby/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
# Duplicate Character Counter
if ARGV.length == 0 || ARGV[0] == ''
  puts 'Usage: please provide a string'
else
   hash_count_duplicate_letters = ARGV[0].each_char.with_object(Hash.new(0)) {|a, b| b[a]+=1}
   counter_duplicate_letters = 0
   hash_count_duplicate_letters.each do |key, value|
    if value>1
        puts "#{key}: #{value}"
        counter_duplicate_letters += 1
    end
end
    if counter_duplicate_letters == 0 
        puts "No duplicate characters"
    end 
end
# end

```

{% endraw %}

Duplicate Character Counter in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- MSJ

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).