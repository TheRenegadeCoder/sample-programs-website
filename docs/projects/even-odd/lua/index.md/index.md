---

---

Welcome to the Even Odd in Lua page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.