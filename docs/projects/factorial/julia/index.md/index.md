---

---

# Factorial in Julia

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Julia
#!/usr/bin/julia

function err() 
   println("Usage: please input a non-negative integer")
end

function fac(n)
    if n < 0
        err()
        exit()
    end
        
    out = 1
    for i = 1:n
        out = out * i
    end
    return out
end

try
    println(fac(parse(Int, ARGS[1])))
catch e
    err()
end

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.