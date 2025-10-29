---
authors:
- Connor H
date: 2025-10-29
featured-image: linear-search-in-every-language.jpg
last-modified: 2025-10-29
layout: default
tags:
- linear-search
- lua
title: Linear Search in Lua
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/linear-search/lua/how-to-implement-the-solution.md
- sources/programs/linear-search/lua/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Linear Search](https://sampleprograms.io/projects/linear-search) in [Lua](https://sampleprograms.io/languages/lua) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lua

local args = {...}

local nums_str = args[1]

local key = tonumber(args[2])

local numbers = {}

local found = false

    if #args ~= 2 then
        print('Usage: please provide a list of integers ("1, 4, 5, 11, 12") and the integer to find ("11")')
        return
    end
    
    if not key then

        print('Usage: please provide a list of integers ("1, 4, 5, 11, 12") and the integer to find ("11")')
        return
    end

    if #nums_str < 1 then
          print('Usage: please provide a list of integers ("1, 4, 5, 11, 12") and the integer to find ("11")')
        return
    end

for num in string.gmatch(nums_str, '([^,]+)') do
    table.insert(numbers, tonumber(num))
end




for i = 1, #numbers do

    if numbers[i] == key then
        found = true

      break
    end
end

print(found and "true" or "false")

```

{% endraw %}

Linear Search in [Lua](https://sampleprograms.io/languages/lua) was written by:

- Connor H

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).