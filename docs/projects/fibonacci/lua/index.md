---
authors:
- Andy Alban
date: 2019-10-14
featured-image: fibonacci-in-every-language.jpg
last-modified: 2019-10-14
layout: default
tags:
- fibonacci
- lua
title: Fibonacci in Lua
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/lua/how-to-implement-the-solution.md
- sources/programs/fibonacci/lua/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Lua](https://sampleprograms.io/languages/lua) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lua
function fib(n)
  local a, b = 0, 1
  for k = 1, n do
    a, b = b, a + b
    print(k .. ": " .. a)
  end
end

if tonumber(arg[1]) ~= nil then
  n = tonumber(arg[1])
  print(fib(n))
else
  print("Usage: please input the count of fibonacci numbers to output")
end

```

{% endraw %}

Fibonacci in [Lua](https://sampleprograms.io/languages/lua) was written by:

- Andy Alban

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).