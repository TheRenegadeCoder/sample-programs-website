---

title: Capitalize in Lua
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Capitalize in Lua page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).