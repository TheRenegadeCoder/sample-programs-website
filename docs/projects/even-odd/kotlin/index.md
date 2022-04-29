---

title: Even Odd in Kotlin
layout: default
date: 2022-04-28
last-modified: 2022-04-28

---

Welcome to the Even Odd in Kotlin page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Kotlin
fun main(args: Array<String>) {
    if (args.isNullOrEmpty() || args[0].toIntOrNull() == null) {
        println("Usage: please input a number")
        return
    }
    val num = args[0].toInt()
    if (num % 2 == 0) {
        println("Even")
    } else {
        println("Odd")
    }
}
```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.