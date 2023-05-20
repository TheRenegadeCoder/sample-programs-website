---
title: Even Odd in Julia
layout: default
date: 2021-11-01
featured-image: even-odd-in-every-language.jpg
last-modified: 2021-11-01

---

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Julia](https://sampleprograms.io/languages/julia) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```julia

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

{% endraw %}

[Even Odd](https://sampleprograms.io/projects/even-odd) in [Julia](https://sampleprograms.io/languages/julia) was written by:

- smjalageri

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).