---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-14
featured-image: depth-first-search-in-every-language.jpg
last-modified: 2026-05-14
layout: default
tags:
- depth-first-search
- ruby
title: Depth First Search in Ruby
title1: Depth First
title2: Search in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/depth-first-search/ruby/how-to-implement-the-solution.md
- sources/programs/depth-first-search/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Depth First Search](/projects/depth-first-search) in [Ruby](/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
# frozen_string_literal: true

USAGE = 'Usage: please provide a tree in an adjacency matrix form ("0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0") together with a list of vertex values ("1, 3, 5, 2, 4") and the integer to find ("4")'

def usage!
  warn USAGE
  exit 1
end

def parse_list(str)
  str.split(",").map { Integer(it.strip) }
rescue ArgumentError, NoMethodError
  usage!
end

def matrix(flat)
  n = Integer(Math.sqrt(flat.size))
  usage! unless n * n == flat.size
  flat.each_slice(n).to_a
end

def dfs(mat, vals, i, target, seen)
  return true if vals[i] == target
  return false if seen[i]

  seen[i] = true

  mat[i].each_with_index do |edge, j|
    next unless edge == 1
    return true if dfs(mat, vals, j, target, seen)
  end

  false
end

tree_s, vals_s, target_s = ARGV
usage! if tree_s.nil? || vals_s.nil? || target_s.nil?

tree = parse_list(tree_s)
vals = parse_list(vals_s)
target = begin
  Integer(target_s)
rescue
  usage!
end

usage! unless vals.size * vals.size == tree.size

mat = matrix(tree)

puts dfs(mat, vals, 0, target, {})

```

{% endraw %}

Depth First Search in [Ruby](/languages/ruby) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).