---

title: Prime Number in Rexx
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Prime Number in Rexx page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Rexx
/* ARG with source string named in REXX program invocation */
arg number
If (DATATYPE(number, 'W') == 0) then signal err
If (number < 0) then signal err
isPrime = 1
if \((number // 2 = 0) & (number \= 2) | (number == 1)) then
	do
		i = TRUNC(number / 2)
		do while(i > 3)
			if (number // i == 0) then
				isPrime = 0
			i = i - 1
		end
	end
else
	isPrime = 0

if (isPrime == 1) then
	say "Prime"
else
	say "Composite"
;exit

Err:
say 'Usage: please input a non-negative integer'; exit

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.