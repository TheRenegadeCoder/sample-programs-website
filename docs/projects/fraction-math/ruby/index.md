---
authors:
- Ebtisam Jelani
- Ștefan-Iulian Alecu
date: 2025-10-31
featured-image: fraction-math-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- fraction-math
- ruby
title: Fraction Math in Ruby
title1: Fraction
title2: Math in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fraction-math/ruby/how-to-implement-the-solution.md
- sources/programs/fraction-math/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fraction Math](https://sampleprograms.io/projects/fraction-math) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
class Fraction
  attr_reader :numerator, :denominator

  def initialize(numerator, denominator)
    @numerator = numerator
    @denominator = denominator
  end

  def to_r
    Rational(numerator, denominator)
  end

  def operate(other, op)
    a = to_r
    b = other.to_r

    case op
    when "+" then (a + b).to_s
    when "-" then (a - b).to_s
    when "*" then (a * b).to_s
    when "/" then (a / b).to_s
    end
  end

  def compare(other, op)
    a = to_r
    b = other.to_r

    case op
    when "==" then a == b
    when "!=" then a != b
    when ">" then a > b
    when "<" then a < b
    when ">=" then a >= b
    when "<=" then a <= b
    end
  end
end

a, op, b = ARGV
abort("Usage: ./fraction-math operand1 operator operand2") unless a && op && b

num1, den1 = a.split("/").map(&:to_i)
num2, den2 = b.split("/").map(&:to_i)

lhs = Fraction.new(num1, den1)
rhs = Fraction.new(num2, den2)

result = lhs.operate(rhs, op)

if !result.nil?
  puts result
else
  cmp = lhs.compare(rhs, op)

  if !cmp.nil?
    puts cmp ? 1 : 0
  else
    puts "Invalid operator"
  end
end

```

{% endraw %}

Fraction Math in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Ebtisam Jelani
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).