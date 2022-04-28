---

---

# Even Odd in Julia

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Julia

#!/usr/bin/julia

function err() 
   println("Usage: please input a number")
end

function even_odd(n)

    if (n % 2 == 0 )
      return "Even"
    else
      return "Odd"
    end  
end

try
    println(even_odd(parse(Int, ARGS[1])))
catch e
    err()
end

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.