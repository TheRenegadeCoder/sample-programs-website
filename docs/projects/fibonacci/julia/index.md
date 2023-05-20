---
title: Fibonacci in Julia
layout: default
date: 2018-10-12
featured-image: fibonacci-in-every-language.jpg
last-modified: 2018-10-12

---

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Julia](https://sampleprograms.io/languages/julia) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

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

[Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Julia](https://sampleprograms.io/languages/julia) was written by:

- Jeremy Grifski
- Michael King

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Apr 16 2019 10:06:37. The solution was first committed on Oct 12 2018 13:55:57. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).