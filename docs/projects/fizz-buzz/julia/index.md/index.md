# Fizz Buzz in Julia

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Julia
#!/usr/bin/julia

for i = 1:100
    str = i % 3 == 0 ? "Fizz" : ""
    str *= i % 5 == 0 ? "Buzz" : ""
    if isempty(str)
        str = i
    end
    println(str)
end

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.