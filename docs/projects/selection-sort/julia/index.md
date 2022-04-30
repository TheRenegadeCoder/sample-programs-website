---

title: Selection Sort in Julia
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Selection Sort in Julia page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```julia
#!/usr/bin/julia

function SelectionSort(arr)
    l = length(arr)
    sorted_list = []
    for i = 1:l
        m = minimum(arr)
        push!(sorted_list,m)
        deleteat!(arr, findfirst(x->x==m,arr))
    end
    return sorted_list
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
    sorted = SelectionSort(n)
    PrintOutput(sorted)

catch e
    error()
end
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).