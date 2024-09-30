---
authors:
- Berry Semexan
date: 2019-10-17
featured-image: even-odd-in-every-language.jpg
last-modified: 2019-10-17
layout: default
tags:
- even-odd
- lua
title: Even Odd in Lua
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/lua/how-to-implement-the-solution.md
- sources/programs/even-odd/lua/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Lua](https://sampleprograms.io/languages/lua) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lua
main = function(input)
    usage = "Usage: please input a number"
    
    if tonumber(input) ~= nil then
        if input % 2 == 0 then
            print("Even")
        else
            print("Odd")
        end
    else
        print(usage)
    end
end
    
main(arg[1])
```

{% endraw %}

Even Odd in [Lua](https://sampleprograms.io/languages/lua) was written by:

- Berry Semexan

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).