---
title: Bubble Sort in Lua
layout: default
date: 2019-10-28
featured-image: bubble-sort-in-every-language.jpg
last-modified: 2019-10-28

---

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Lua](https://sampleprograms.io/languages/lua) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lua
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

[Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Lua](https://sampleprograms.io/languages/lua) was written by:

- Jeremy Grifski
- jketterer

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 15 2020 19:22:39. The solution was first committed on Oct 28 2019 15:46:03. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).