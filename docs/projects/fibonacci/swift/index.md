---

---

Welcome to the Fibonacci in Swift page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Swift
import Foundation

func fibonacciProgram(_ n: Int) {
    var f1=0, f2=1, fib=1
    for i in 0..<n {
        print("\(i+1): \(fib)")
        fib = f1 + f2
        f1 = f2
        f2 = fib
    }
}


func fibonacciRecursive(_ n: Int) -> Int {
    if (n == 0) {
        return 0
    } else if (n == 1) {
        return 1
    }
    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)
}

/*
    Check if there is exactly one argument and if it can be parsed as an integer
*/
guard CommandLine.argc == 2, let number = Int(CommandLine.arguments[1]) else {
    print("Usage: please input the count of fibonacci numbers to output")
    exit(0)
}

fibonacciProgram(number)
```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.