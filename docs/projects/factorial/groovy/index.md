---

title: Factorial in Groovy
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Factorial in Groovy page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Groovy
class Factorial {
    static def factorial(BigInteger n) {
        if (n == 0) {
            return 1
        }
        return n * factorial(n - 1)
    }

    static void main(args){
        if(args?.size() != 1 || !args[0].isInteger() || args[0].toInteger() < 0) {
          println "Usage: please input a non-negative integer"
          return
        }

        if(args[0].toInteger() >= 1000){
            println "Usage: please input a value below 1000"
            return
        }

        println factorial(args[0].toInteger())
    }
}
```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.