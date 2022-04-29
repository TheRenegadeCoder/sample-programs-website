---

title: Factorial in Scala
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Factorial in Scala page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

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

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.