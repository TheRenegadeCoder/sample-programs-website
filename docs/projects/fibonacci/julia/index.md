---

title: Fibonacci in Julia
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Fibonacci in Julia page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```julia
#!/usr/bin/julia

function fib(n)
    f = BigInt[1 1; 1 0]
    for i = 1:n
        fn = f ^ i
        println(i, ": ", fn[2, 1])
    end
end

function error() 
   println("Usage: please input the count of fibonacci numbers to output") 
end

try
    fib(parse(Int, ARGS[1]))
catch e
    error()
end
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).