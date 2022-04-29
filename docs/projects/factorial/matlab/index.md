---

---

Welcome to the Factorial in Matlab page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Matlab
function result=factorial(n)

if n<0
	error('Please input a non-negative integer')
end

if not(ischar(n))
	error('Please input a non-negative integer')
end

if isempty(n)=1
	error('Please input a non-negative integer')
end

x=1;

if n>0
	for i = 1:n
  
     		x=x*i;

	end
end

result = x
end

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.