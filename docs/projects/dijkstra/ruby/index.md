---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-14
featured-image: dijkstra-in-every-language.jpg
last-modified: 2026-05-14
layout: default
tags:
- dijkstra
- ruby
title: Dijkstra in Ruby
title1: Dijkstra
title2: in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/dijkstra/ruby/how-to-implement-the-solution.md
- sources/programs/dijkstra/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Dijkstra](/projects/dijkstra) in [Ruby](/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
# frozen_string_literal: true

USAGE = "Usage: please provide three inputs: a serialized matrix, a source node and a destination node"

def usage!
  warn USAGE
  exit 1
end

def parse_matrix(str)
  str.split(",").map { Integer(it.strip) }
rescue ArgumentError, NoMethodError
  usage!
end

def build_matrix(flat)
  n = Integer(Math.sqrt(flat.size))
  usage! unless n * n == flat.size

  matrix = flat.each_slice(n).to_a

  usage! if matrix.any? { |row| row.any?(&:negative?) }

  matrix
end

def parse_index(str, n)
  usage! if str.nil? || str.strip.empty?

  i = Integer(str)
  usage! unless i.between?(0, n - 1)

  i
rescue ArgumentError
  usage!
end

def dijkstra(matrix, src, dst)
  n = matrix.size
  dist = Array.new(n, Float::INFINITY)
  visited = Array.new(n, false)

  dist[src] = 0

  n.times do
    u = nil
    best = Float::INFINITY

    n.times do |i|
      next if visited[i]
      next if dist[i] >= best

      best = dist[i]
      u = i
    end

    break unless u

    visited[u] = true

    row = matrix[u]
    base = dist[u]

    row.each_with_index do |w, v|
      next if w <= 0 || visited[v]

      alt = base + w
      dist[v] = alt if alt < dist[v]
    end
  end

  dist[dst]
end

matrix_str, src_str, dst_str = ARGV
usage! if matrix_str.nil? || src_str.nil? || dst_str.nil?
usage! if matrix_str.strip.empty? || src_str.strip.empty? || dst_str.strip.empty?

matrix = build_matrix(parse_matrix(matrix_str))
n = matrix.size

src = parse_index(src_str, n)
dst = parse_index(dst_str, n)

dist = dijkstra(matrix, src, dst)

usage! unless dist.finite?

puts dist.to_i

```

{% endraw %}

Dijkstra in [Ruby](/languages/ruby) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).