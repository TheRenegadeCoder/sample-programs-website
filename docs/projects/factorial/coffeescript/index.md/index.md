---

---

# Factorial in Coffeescript

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Coffeescript
factorial = (n) ->
    return usage() if n < 0
    return 1 if n == "0"
    [1..n].reduce (x, y) -> x * y
    
usage = () ->
    "Usage: please input a non-negative integer"
    
main = () ->
    args = process.argv
    return factorial(args[2]) if args.length == 3 and isFinite(args[2]) and args[2] != ""
    usage()

console.log main()

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.