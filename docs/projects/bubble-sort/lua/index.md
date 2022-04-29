---

title: Bubble Sort in Lua

---

Welcome to the Bubble Sort in Lua page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Lua
-- Initialize table
nums = {}

-- Exit if no list is entered or list is empty
if arg[1] == nil or #arg[1] == 0 then
    print('Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"')
    return
end

-- Exit if list has a single entry or is not formatted with commas
if (not string.match(arg[1], " ")) or (not string.match(arg[1], ",")) then
    print('Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"')
    return
end

-- Read input list into a table
for i=1, #arg[1] do
    char = string.sub(arg[1], i, i)
    if tonumber(char) then
        table.insert(nums, char)
    end
end

-- Loop through entire table
for i=1, #nums do
    -- Loop through entire table
    for index,value in pairs(nums) do
        -- If current number is larger than next number, swap them
        if nums[index+1] ~= nil and value > nums[index+1] then
            nums[index] = nums[index+1]
            nums[index+1] = value
        end
    end
end

-- Print sorted list
for k,v in pairs(nums) do
    io.write(v)

    -- Comma formatting
    if nums[k+1] ~= nil then
        io.write(', ')
    end
end

io.write("\n")

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.