# Fizz Buzz in Solisp

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Solisp
(Join (Map num (Seq 1 100)
	(Switch
        {(== (% num 3) (% num 5) 0) "FizzBuzz"}
        {(== (% num 3) 0) "Fizz"}
        {(== (% num 5) 0) "Buzz"}
        {true num}
    )
) "\n")
```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.