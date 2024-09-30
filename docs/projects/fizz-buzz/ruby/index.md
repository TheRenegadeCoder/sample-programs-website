---
authors:
- Jeremy Grifski
date: 2018-08-12
featured-image: fizz-buzz-in-every-language.png
last-modified: 2018-08-12
layout: default
tags:
- fizz-buzz
- ruby
title: Fizz Buzz in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/ruby/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
def fizzbuzz(number)
    divisibleBy3 = (number % 3 == 0)
    divisibleBy5 = (number % 5 == 0)

    case
        when divisibleBy3 && divisibleBy5
            puts "FizzBuzz"
        when divisibleBy3
            puts "Fizz"
        when divisibleBy5
            puts "Buzz"
        else 
            puts number
    end
end

(1..100).each {|n| fizzbuzz n}

```

{% endraw %}

Fizz Buzz in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).