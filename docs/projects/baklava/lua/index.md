---
title: Baklava in Lua
layout: default
date: 2019-10-28
featured-image: baklava-in-every-language.jpg
last-modified: 2019-10-28

---

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Lua](https://sampleprograms.io/languages/lua) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

[Baklava](https://sampleprograms.io/projects/baklava) in [Lua](https://sampleprograms.io/languages/lua) was written by:

- bhaskar_datta
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 15 2020 19:22:39. The solution was first committed on Oct 28 2019 15:42:24. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).