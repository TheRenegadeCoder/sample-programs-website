---
authors:
- Jeremy Grifski
date: 2018-09-17
featured-image: baklava-in-every-language.jpg
last-modified: 2018-09-17
layout: default
tags:
- baklava
- ruby
title: Baklava in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/ruby/how-to-implement-the-solution.md
- sources/programs/baklava/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
10.times {|n|
    print " " * (10 - n)
    puts "*" * (2 * n + 1)
}

for i in 10.downto(0) do
  puts ((" " * (10 - i)) + ("*" * (i * 2 + 1)))
end

```

{% endraw %}

Baklava in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).