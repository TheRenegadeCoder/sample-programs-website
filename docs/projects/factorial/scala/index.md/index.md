# Factorial in Scala

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Scala
// Scala Program to calculate 
// Factorial of a number 

// Creating object 
object GFG 
{ 
	// Iterative way to calculate 
	// factorial 
	def factorial(n: Int): Int = { 
		
		var f = 1
		for(i <- 1 to n) 
		{ 
			f = f * i; 
		} 
		
		return f 
	} 

	// Driver Code 
	def main(args: Array[String]) 
	{   val m= args(0).toInt
		println(factorial(m)) 
	} 

} 

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.