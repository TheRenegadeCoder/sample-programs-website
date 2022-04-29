---

title: Factorial in Julia
layout: default
date: 2022-04-28
last-modified: 2022-04-28

---

Welcome to the Factorial in Julia page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

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

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.