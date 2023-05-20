---
title: Capitalize in Lua
layout: default
date: 2019-10-17
featured-image: capitalize-in-every-language.jpg
last-modified: 2019-10-17

---

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

[Capitalize](https://sampleprograms.io/projects/capitalize) in [Lua](https://sampleprograms.io/languages/lua) was written by:

- Berry Semexan
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 15 2020 19:22:39. The solution was first committed on Oct 17 2019 11:02:13. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).