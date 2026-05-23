---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-14
featured-image: convex-hull-in-every-language.jpg
last-modified: 2026-05-14
layout: default
tags:
- convex-hull
- ruby
title: Convex Hull in Ruby
title1: Convex Hull
title2: in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/convex-hull/ruby/how-to-implement-the-solution.md
- sources/programs/convex-hull/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Convex Hull](/projects/convex-hull) in [Ruby](/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
# frozen_string_literal: true

USAGE = 'Usage: please provide at least 3 x and y coordinates as separate lists (e.g. "100, 440, 210")'

def usage!
  warn USAGE
  exit 1
end

def parse_list(str)
  str.split(",").map { Integer(it.strip) }
rescue ArgumentError, NoMethodError
  usage!
end

def cross(o, a, b)
  (a[0] - o[0]) * (b[1] - o[1]) -
    (a[1] - o[1]) * (b[0] - o[0])
end

def build_hull(points)
  hull = []

  points.each do |p|
    hull.pop while hull.size >= 2 && cross(hull[-2], hull[-1], p) <= 0
    hull << p
  end

  hull
end

def convex_hull(points)
  points = points.sort

  lower = build_hull(points)
  upper = build_hull(points.reverse)

  lower + upper[1..-2]
end

x_str, y_str = ARGV
usage! if x_str.nil? || y_str.nil?

x = parse_list(x_str)
y = parse_list(y_str)

usage! if x.size != y.size || x.size < 3

points = x.zip(y)

convex_hull(points).each do |x, y|
  puts "(#{x}, #{y})"
end

```

{% endraw %}

Convex Hull in [Ruby](/languages/ruby) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).