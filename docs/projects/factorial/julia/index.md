---
title: Factorial in Julia
layout: default
date: 2020-10-01
featured-image: factorial-in-every-language.jpg
last-modified: 2020-10-01

---

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Julia](https://sampleprograms.io/languages/julia) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```julia
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

[Factorial](https://sampleprograms.io/projects/factorial) in [Julia](https://sampleprograms.io/languages/julia) was written by:

- sniklas142

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).