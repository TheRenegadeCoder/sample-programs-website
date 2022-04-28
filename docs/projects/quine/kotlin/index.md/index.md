---

---

# Quine in Kotlin

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Kotlin
fun main(args: Array<String>) { //Prints out it's own code
	val s = """fun main(args: Array<String>) { //Prints out it's own code
	val s = """

	val a = """^s\"\"\"^s\"\"\"\n\n\tval a = \"\"\"^a\"\"\"\n\tprint(\"^{a.replace(']' + 1, '$')}\")\n}\n"""
	print("$s\"\"\"$s\"\"\"\n\n\tval a = \"\"\"$a\"\"\"\n\tprint(\"${a.replace(']' + 1, '$')}\")\n}\n")
}
```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.