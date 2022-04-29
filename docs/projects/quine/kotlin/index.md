---

title: Quine in Kotlin
layout: default
date: 2022-04-28
last-modified: 2022-04-28

---

Welcome to the Quine in Kotlin page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Kotlin
fun main(args: Array<String>) { //Prints out it's own code
	val s = """fun main(args: Array<String>) { //Prints out it's own code
	val s = """

	val a = """^s\"\"\"^s\"\"\"\n\n\tval a = \"\"\"^a\"\"\"\n\tprint(\"^{a.replace(']' + 1, '$')}\")\n}\n"""
	print("$s\"\"\"$s\"\"\"\n\n\tval a = \"\"\"$a\"\"\"\n\tprint(\"${a.replace(']' + 1, '$')}\")\n}\n")
}
```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.