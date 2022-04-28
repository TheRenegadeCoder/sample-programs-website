# Even Odd in Groovy

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Groovy
class EvenOdd {
  static void main(String... args) {
    if(args?.length != 1 || !args[0]?.isInteger()) {
      println 'Usage: please input a number'
    } else {
      println args[0].toInteger() % 2 == 0 ? 'Even' : 'Odd'
    }
  }
}

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.