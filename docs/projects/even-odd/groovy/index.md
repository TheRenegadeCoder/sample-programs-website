---

title: Even Odd in Groovy
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Even Odd in Groovy page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

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

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.