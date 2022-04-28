---

---

# Fizz Buzz in Dg

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Dg
fizz_buzz = n -> if
    n % 15 == 0 => "FizzBuzz"
    n % 3  == 0 => "Fizz"
    n % 5  == 0 => "Buzz"
    otherwise   => n

main = start end ruleset ->
    for i in range start (end + 1) =>
        print <| ruleset i

main 1 100 fizz_buzz

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.