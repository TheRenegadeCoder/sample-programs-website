# Baklava in Solisp

## Solution

```Solisp
(Join (Map x (Append (Seq 0 10) (Reverse (Seq 0 9)))
	(Join (Append
		(Clone (- 10 x) " ")
		(Clone (+ (* x 2) 1) "#")
	))
) "\n")
```