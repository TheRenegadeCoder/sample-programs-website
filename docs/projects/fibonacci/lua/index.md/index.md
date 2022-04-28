# Fibonacci in Lua

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.