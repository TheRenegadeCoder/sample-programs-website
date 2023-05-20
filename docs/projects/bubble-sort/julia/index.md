---
title: Bubble Sort in Julia
layout: default
date: 2020-10-01
featured-image: bubble-sort-in-every-language.jpg
last-modified: 2020-10-01

---

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Julia](https://sampleprograms.io/languages/julia) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```julia
#!/usr/bin/julia

function BubbleSort(arr)
    l = length(arr)
    swapped = true
    while swapped
        swapped = false
        for j = 2:l
            if arr[j-1] > arr[j]
                tmp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = tmp
                swapped = true
            end
        end
    end
end

function error()
    println("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"")
end

function HandleInput(inp)

    a = split(inp,",")
    a = map(x->split(x," "),a)
    a = map(x->last(x),a)
    numbers = map(x->parse(Int,x),a)
    if length(numbers) == 1
        error()
        exit()
    end
    return numbers
    
end

function PrintOutput(out)
    for i = 1:length(out)
        print(out[i])
        if i != length(out)
            print(", ")
        end
    end
    println()
end

try

    n = HandleInput(ARGS[1])
    BubbleSort(n)
    PrintOutput(n)

catch e
    error()
end
```

{% endraw %}

[Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Julia](https://sampleprograms.io/languages/julia) was written by:

- sniklas142

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 01 2020 20:53:17. The solution was first committed on Oct 01 2020 15:22:44. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).