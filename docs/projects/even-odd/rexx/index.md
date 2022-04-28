---

---

Welcome to the Even Odd in Rexx page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Rexx
/* ARG with source string named in REXX program invocation */
arg number
If (DATATYPE(number, 'W') == 0) then signal err
if (number // 2 == 0) then
	say "Even"
else
	say "Odd"
;exit

Err:
say 'Usage: please input a number'; exit

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.