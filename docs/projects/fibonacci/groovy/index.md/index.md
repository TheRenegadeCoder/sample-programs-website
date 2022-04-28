# Fibonacci in Groovy

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Groovy
class Fibonacci {
    static void main(String[] args) {
        if (args.length < 1 || !args[0].isInteger()) {
            println 'please provide a positive integer'
        } else {
            def n = args[0] as Integer
            def first = 0G
            def second = 1G
            println first.class
            (1..n).each {
                second += first
                first = second - first
                println "$it: $first"
            }
        }
    }
}

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.