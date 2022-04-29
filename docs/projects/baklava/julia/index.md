---

title: Baklava in Julia

---

Welcome to the Baklava in Julia page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Julia
#!/usr/bin/julia

function main()
    for i = 0:10
        print(" "^(10 - i))
        println("*"^(i * 2 + 1))
    end 

    for i = 9:-1:0
        print(" "^(10 - i))
        println("*"^(i * 2 + 1))
    end
end

main()

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.