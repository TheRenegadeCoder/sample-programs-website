---
authors:
- Allan Klaus
date: 2020-10-06
featured-image: roman-numeral-in-every-language.jpg
last-modified: 2020-10-06
layout: default
tags:
- roman-numeral
- ruby
title: Roman Numeral in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/roman-numeral/ruby/how-to-implement-the-solution.md
- sources/programs/roman-numeral/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
ROMAN_VALUES = {
  "I": 1,
  "V": 5,
  "X": 10,
  "L": 50,
  "C": 100,
  "D": 500,
  "M": 1000
}

def roman_valid?(roman_numbers)
  return false if roman_numbers.any? { |roman_number| !ROMAN_VALUES.keys.include?(roman_number.to_sym) }  
  return false if roman_numbers.join.include?('MMMM')
  
  counter_numbers = roman_numbers.tally # Only on ruby 2.7+
  unless counter_numbers['M'].nil?
    return false if counter_numbers['M'] > 4
  end
  
  counter_numbers.reject { |k| k == 'M' }.all? { |(_, counter)| counter <= 3 }
end

def roman_to_decimal(full_roman_number)
  return 'Usage: please provide a string of roman numerals' if full_roman_number.nil?
  return 0 if full_roman_number.empty?

  roman_numbers = full_roman_number.upcase.split('')
  return 'Error: invalid string of roman numerals' unless roman_valid?(roman_numbers)

  total = 0

  roman_numbers.each_with_index do |roman_number, index|
    current_value = ROMAN_VALUES[roman_number.to_sym]
    next_value = ROMAN_VALUES[roman_numbers[index+1]&.to_sym] || 0
    
    if (current_value >= next_value)
      total += current_value
    else
      total -= current_value
    end
  end

  total
end

print(roman_to_decimal(ARGV[0]))
```

{% endraw %}

Roman Numeral in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Allan Klaus

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).