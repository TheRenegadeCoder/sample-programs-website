---

---

# Even Odd in Swift

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Swift
// for System.exit()
import Foundation


/*
    Check if there is exactly one argument and if it can be parsed as an integer
*/
guard CommandLine.argc == 2, let number = Int(CommandLine.arguments[1]) else {
    print("Usage: please input a number")
    exit(0)
}

let is_even = number % 2 == 0

if is_even {
    print("Even")
} else {
    print("Odd")
}
```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.