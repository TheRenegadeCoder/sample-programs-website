---

title: Fibonacci in Groovy
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Fibonacci in Groovy page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

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

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.