# Reverse String in Solisp

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Solisp
(If (== (Length args) 0)
	""
	(If (== (Length (Get 0 args)) 0)
		""
		(Join (Tail (Reverse (Join args " "))))
	)
)
```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.