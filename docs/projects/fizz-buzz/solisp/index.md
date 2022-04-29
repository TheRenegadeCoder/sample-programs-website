---

title: Fizz Buzz in Solisp
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Fizz Buzz in Solisp page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Solisp
(Join (Map num (Seq 1 100)
	(Switch
        {(== (% num 3) (% num 5) 0) "FizzBuzz"}
        {(== (% num 3) 0) "Fizz"}
        {(== (% num 5) 0) "Buzz"}
        {true num}
    )
) "\n")
```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.