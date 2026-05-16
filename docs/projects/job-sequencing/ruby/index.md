---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-14
featured-image: job-sequencing-in-every-language.jpg
last-modified: 2026-05-14
layout: default
tags:
- job-sequencing
- ruby
title: Job Sequencing in Ruby
title1: Job Sequencing
title2: in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/job-sequencing/ruby/how-to-implement-the-solution.md
- sources/programs/job-sequencing/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Job Sequencing](https://sampleprograms.io/projects/job-sequencing) in [Ruby](https://sampleprograms.io/languages/ruby)! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
# frozen_string_literal: true

USAGE = "Usage: please provide a list of profits and a list of deadlines"

def usage!
  warn USAGE
  exit 1
end

def parse_list(str)
  str.split(",").map { Integer(it.strip) }
rescue ArgumentError, NoMethodError
  usage!
end

def find(parent, x)
  while parent[x] != x
    parent[x] = parent[parent[x]]
    x = parent[x]
  end
  x
end

def schedule(profits, deadlines)
  jobs = profits.zip(deadlines)
  max_d = deadlines.max

  parent = (0..max_d).to_a

  total = 0

  jobs.sort_by { -it[0] }.each do |profit, d|
    slot = find(parent, [d, max_d].min)

    next if slot == 0

    parent[slot] = slot - 1
    total += profit
  end

  total
end

profits_str, deadlines_str = ARGV
usage! if profits_str.nil? || deadlines_str.nil? ||
  profits_str.strip.empty? || deadlines_str.strip.empty?

profits = parse_list(profits_str)
deadlines = parse_list(deadlines_str)

usage! if profits.size != deadlines.size

puts schedule(profits, deadlines)

```

{% endraw %}

Job Sequencing in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).