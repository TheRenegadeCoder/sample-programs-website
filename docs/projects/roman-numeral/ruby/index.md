---

title: Roman Numeral in Ruby
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Roman Numeral in Ruby page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Ruby
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.