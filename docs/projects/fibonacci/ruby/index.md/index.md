---

---

Welcome to the Fibonacci in Ruby page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Ruby
def fibonacci(number)
    a = 0
    b = 1
    c = 0

    i = 0
    while i < number
        c = a + b
        b = a
        a = c

        print("#{i+1}: #{c}\n")
        i += 1
    end
end

num = Integer(ARGV[0]) rescue -1
if num >= 0
    fibonacci(num)
else
    print("Usage: please input the count of fibonacci numbers to output")
end
```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.