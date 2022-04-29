---

title: Even Odd in Lua
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Even Odd in Lua page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Lua
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.