---

title: Baklava in Lua
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Baklava in Lua page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lua
function diamondStarPattern(height)
  for i = 1, height do -- loop for printing the upper half of the baklava
    for j = i, height - 1 do io.write(" ") end --to print the leading spaces
    for j = 1, (2*i-1) do io.write("*") end -- to print the * for the upper half
    io.write("\n") -- to move pointer to next line
  end
  for i = height - 1,1,-1 do -- loop for printing the lower half of the baklava
    for j = i, height - 1 do io.write(" ") end -- to print the spaces
    for j = 1, (2*i-1) do io.write("*") end --  to print the * for the lower half
    io.write("\n") -- to move pointer to next line
  end  
end

diamondStarPattern(11)
```

{% endraw %}

Baklava in Lua was written by:

- bhaskar_datta
- Jeremy Grifski

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 15 2020 19:22:39. The solution was first committed on Oct 28 2019 15:30:24. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).