---

title: Even Odd in Lua
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Even Odd in Lua page! Here, you'll find the source code for this program as well as a description of how the program works.

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

Even Odd in Lua was written by:

- Berry Semexan

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).