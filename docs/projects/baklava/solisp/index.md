---

title: Baklava in Solisp
layout: default
date: 2022-04-28
last-modified: 2022-04-28

---

Welcome to the Baklava in Solisp page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Solisp
(Join (Map x (Append (Seq 0 10) (Reverse (Seq 0 9)))
	(Join (Append
		(Clone (- 10 x) " ")
		(Clone (+ (* x 2) 1) "#")
	))
) "\n")
```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.