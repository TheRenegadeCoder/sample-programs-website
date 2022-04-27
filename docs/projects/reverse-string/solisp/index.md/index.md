# Reverse String in Solisp

## Solution

```Solisp
(If (== (Length args) 0)
	""
	(If (== (Length (Get 0 args)) 0)
		""
		(Join (Tail (Reverse (Join args " "))))
	)
)
```