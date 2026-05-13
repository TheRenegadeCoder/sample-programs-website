---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-14
featured-image: transpose-matrix-in-every-language.jpg
last-modified: 2026-05-14
layout: default
tags:
- ruby
- transpose-matrix
title: Transpose Matrix in Ruby
title1: Transpose
title2: Matrix in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/transpose-matrix/ruby/how-to-implement-the-solution.md
- sources/programs/transpose-matrix/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Transpose Matrix](https://sampleprograms.io/projects/transpose-matrix) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
# frozen_string_literal: true

USAGE = "Usage: please enter the dimension of the matrix and the serialized matrix"

def usage!
  warn USAGE
  exit 1
end

def parse_int(str)
  Integer(str)
rescue ArgumentError, NoMethodError
  usage!
end

def parse_list(str)
  str.split(",").map { parse_int(it.strip) }
end

cols_str, rows_str, matrix_str = ARGV

usage! if cols_str.nil? || rows_str.nil? || matrix_str.nil?
usage! if cols_str.strip.empty? || rows_str.strip.empty? || matrix_str.strip.empty?

cols = parse_int(cols_str)
rows = parse_int(rows_str)

usage! if cols <= 0 || rows <= 0

flat = parse_list(matrix_str)
usage! if flat.length != cols * rows

matrix = flat.each_slice(cols).to_a
transposed = matrix.transpose

puts transposed.flatten.join(", ")

```

{% endraw %}

Transpose Matrix in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).