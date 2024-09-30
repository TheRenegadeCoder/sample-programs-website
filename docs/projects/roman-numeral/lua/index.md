---
authors:
- Jeremy Grifski
- jketterer
date: 2019-10-28
featured-image: roman-numeral-in-every-language.jpg
last-modified: 2020-10-15
layout: default
tags:
- lua
- roman-numeral
title: Roman Numeral in Lua
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/roman-numeral/lua/how-to-implement-the-solution.md
- sources/programs/roman-numeral/lua/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [Lua](https://sampleprograms.io/languages/lua) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lua
#!/bin/lua

-- Key value pairs for roman numerals
conversion_table = {
    ['I']=1,
    ['V']=5,
    ['X']=10,
    ['L']=50,
    ['C']=100,
    ['D']=500,
    ['M']=1000
}

-- Check if character is valid (in conversion table)
function validateCharacter(char) 
    for key,value in pairs(conversion_table) do
        if char == key then
            return true
        end
    end
    return false
end

-- Convert roman numeral to decimal
function convertToDecimal(roman)
    -- If numeral is a single character, simply return value
    if #roman == 1 then
        return conversion_table[roman]
    end

    sum = 0

    -- Iterate through entire number
    for i = 1, #roman do
        current = conversion_table[string.sub(roman, i, i)]
        next = conversion_table[string.sub(roman, i+1, i+1)]
        
        -- Subtract values if first character is smaller, then skip next character
        if (next ~= nil) and (current < next) then
            sum = sum + (next - current)
            break
        -- Add character value to sum
        else
            sum = sum + current
        end
    end

    return sum
end

-- Get input from command line
input = arg[1]

-- Exit if no input given
if arg[1] == nil then
    print('Usage: please provide a string of roman numerals')
    return
end

-- Check each character for validity, exit if any are invalid
for i = 1, #input do
    if validateCharacter(string.sub(input, i, i)) == false then
        print('Error: invalid string of roman numerals')
        return
    end
end

-- Print converted value
print(convertToDecimal(input))

```

{% endraw %}

Roman Numeral in [Lua](https://sampleprograms.io/languages/lua) was written by:

- Jeremy Grifski
- jketterer

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).