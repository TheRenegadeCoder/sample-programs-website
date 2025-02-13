---
authors:
- Jacob Woodbury
date: 2025-02-13
featured-image: prime-number-in-every-language.jpg
last-modified: 2025-02-13
layout: default
tags:
- julia
- prime-number
title: Prime Number in Julia
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/julia/how-to-implement-the-solution.md
- sources/programs/prime-number/julia/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Julia](https://sampleprograms.io/languages/julia) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```julia
function err() 
    return "Usage: please input a non-negative integer"
 end
 

function isPrime(num)
# handle 0 and 1
    if num <= 1 
        return "composite"
    end 

# default handler
    for i in 2:sqrt(num) #loop starting at 2, ending at the squareroot of the input
        if (num % i == 0)
            return "composite"
        end
    end
    return "prime"             
end

#check for a valid input
try
    n = parse(Int, ARGS[1])
    if n < 0
        println(err())
    else
        println(isPrime(n))
    end
catch e
    println(err())
end

```

{% endraw %}

Prime Number in [Julia](https://sampleprograms.io/languages/julia) was written by:

- Jacob Woodbury

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).