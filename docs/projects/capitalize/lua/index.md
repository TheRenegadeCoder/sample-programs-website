---

title: Capitalize in Lua
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Capitalize in Lua page! Here, you'll find the source code for this program as well as a description of how the program works.

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

Capitalize in Lua was written by:

- Jeremy Grifski
- Berry Semexan

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 15 2020 19:22:39. The solution was first committed on Oct 17 2019 11:02:13. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).