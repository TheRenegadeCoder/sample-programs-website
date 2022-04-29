---

---

Welcome to the Fizz Buzz in Lua page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Lua
for i = 1, 100 do
    output = ""

    if i % 3 == 0 then
        output = output .. "Fizz"
    end

    if i % 5 == 0 then
        output = output .. "Buzz"
    end

    if output == "" then
        output = i
    end

    print(output)
end

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.