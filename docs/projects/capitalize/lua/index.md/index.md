---

---

# Capitalize in Lua

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Lua
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.