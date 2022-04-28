# Reverse String in Kotlin

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Kotlin
fun main(args: Array<String>){
  // Get input, or use default value
  val targetValue = when (args.size > 0 && !args[0].isNullOrBlank()) {
    true -> args[0]
    false -> throw Error("No String Provided. Nothing to Reverse")
  }  
  
  // Kotlin provides a simple `reversed()` function in the standard
  // library for all String/CharSequence objects
  println(targetValue.reversed())
}
```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.