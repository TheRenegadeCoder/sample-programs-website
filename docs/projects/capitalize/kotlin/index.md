---

title: Capitalize in Kotlin
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Capitalize in Kotlin page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Kotlin
fun main(args: Array<String>) {
    if (args.isNullOrEmpty() || args[0].isBlank()) {
        println("Usage: please provide a string")
    } else {
        // Kotlin provides a simple `capitalize()` function in the standard
        // library for all String objects
        println(args[0].capitalize())
    }
}

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.