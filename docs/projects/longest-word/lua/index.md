---
authors:
- alexborovets11
date: 2025-03-26
featured-image: longest-word-in-every-language.jpg
last-modified: 2025-03-26
layout: default
tags:
- longest-word
- lua
title: Longest Word in Lua
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/lua/how-to-implement-the-solution.md
- sources/programs/longest-word/lua/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Lua](https://sampleprograms.io/languages/lua) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lua
if #arg < 1 then
    print("Usage: please provide a string")
    os.exit(1)
end

local input = arg[1]

function longest_word_length(str)
    local max_length = 0
    local found_word = false

    for word in string.gmatch(str, "%S+") do
        found_word = true
        local length = #word  
        if length > max_length then
            max_length = length  
        end
    end

    if not found_word then
        print("Usage: please provide a string")
        os.exit(1)
    end

    return max_length  
end


print(longest_word_length(input))
```

{% endraw %}

Longest Word in [Lua](https://sampleprograms.io/languages/lua) was written by:

- alexborovets11

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).