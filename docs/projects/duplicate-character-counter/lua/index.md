---
authors:
- abdirashidexe
date: 2025-02-18
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2025-02-18
layout: default
tags:
- duplicate-character-counter
- lua
title: Duplicate Character Counter in Lua
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/lua/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/lua/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Lua](https://sampleprograms.io/languages/lua) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lua
function duplicateCharacterCounter(word)
  local hasDuplicates = false;

  -- Empty or no input validation
  if word == "" or word == nil then 
    print("Usage: please provide a string")
    return

  -- Check for duplicates validation
  elseif (string.len(word) >= 1) then
    local myTable = {}
    local duplicateList = {}
    
    for i=1, string.len(word) do
      local char = string.sub(word, i, i)
      if (myTable[char]) then
        myTable[char] = myTable[char]+1
        hasDuplicates = true

      else
        myTable[char] = 1;
        table.insert(duplicateList, char)
      end
    end
    for _, char in ipairs(duplicateList) do
        if myTable[char] > 1 then
            print(char .. ": " .. myTable[char])
        end
    end
  end

  -- No duplicates validation
  if not (hasDuplicates) then
    print("No duplicate characters")
  end
end

duplicateCharacterCounter(arg[1])
```

{% endraw %}

Duplicate Character Counter in [Lua](https://sampleprograms.io/languages/lua) was written by:

- abdirashidexe

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).