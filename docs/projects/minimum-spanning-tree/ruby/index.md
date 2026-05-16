---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-14
featured-image: minimum-spanning-tree-in-every-language.jpg
last-modified: 2026-05-14
layout: default
tags:
- minimum-spanning-tree
- ruby
title: Minimum Spanning Tree in Ruby
title1: Minimum Spanning
title2: Tree in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/minimum-spanning-tree/ruby/how-to-implement-the-solution.md
- sources/programs/minimum-spanning-tree/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Minimum Spanning Tree](https://sampleprograms.io/projects/minimum-spanning-tree) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
# frozen_string_literal: true

USAGE = "Usage: please provide a comma-separated list of integers"

def usage!
  warn USAGE
  exit 1
end

def parse_input
  raw = ARGV.first
  usage! if raw.nil? || raw.strip.empty?

  nums = raw.split(",").map { Integer(it.strip) }
  n = Integer(Math.sqrt(nums.length))
  usage! unless n * n == nums.length

  Array.new(n) { |i| nums[i * n, n] }
rescue ArgumentError, NoMethodError
  usage!
end

def find(parent, x)
  (parent[x] == x) ? x : (parent[x] = find(parent, parent[x]))
end

def union(parent, rank, a, b)
  a = find(parent, a)
  b = find(parent, b)
  return if a == b

  if rank[a] < rank[b]
    parent[a] = b
  elsif rank[a] > rank[b]
    parent[b] = a
  else
    parent[b] = a
    rank[a] += 1
  end
end

def mst_weight(matrix)
  n = matrix.size

  edges =
    (0...n).flat_map do |i|
      (i + 1...n).map do |j|
        w = matrix[i][j]
        w.positive? ? [w, i, j] : nil
      end
    end.compact

  edges.sort_by!(&:first)

  parent = (0...n).to_a
  rank = Array.new(n, 0)

  edges.reduce(0) do |total, (w, u, v)|
    next total if find(parent, u) == find(parent, v)

    union(parent, rank, u, v)
    total + w
  end
end

matrix = parse_input
puts mst_weight(matrix)

```

{% endraw %}

Minimum Spanning Tree in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).