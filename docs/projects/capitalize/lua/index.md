---
authors:
- Berry Semexan
- Jeremy Grifski
date: 2019-10-17
featured-image: capitalize-in-every-language.jpg
last-modified: 2020-10-15
layout: default
tags:
- capitalize
- lua
title: Capitalize in Lua
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/lua/how-to-implement-the-solution.md
- sources/programs/capitalize/lua/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Lua](https://sampleprograms.io/languages/lua) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lua
if (#arg < 1 or arg[1] == '')
then
    print('Usage: please provide a string')
else
    str = {...}
    s = ""
    for i,v in pairs(str) do
        s = s .. v .. " "
    end
    s, _ = s:gsub("^%l", string.upper)
    print(s)  
end

```

{% endraw %}

Capitalize in [Lua](https://sampleprograms.io/languages/lua) was written by:

- Berry Semexan
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).