---

title: Fibonacci in Lua
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Fibonacci in Lua page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Lua
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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).