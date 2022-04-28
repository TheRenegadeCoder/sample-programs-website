---

---

# Baklava in Solisp

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Solisp
(Join (Map x (Append (Seq 0 10) (Reverse (Seq 0 9)))
	(Join (Append
		(Clone (- 10 x) " ")
		(Clone (+ (* x 2) 1) "#")
	))
) "\n")
```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.