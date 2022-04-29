---

title: Prime Number in Matlab

---

Welcome to the Prime Number in Matlab page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Matlab
function result = prime_number(n)

if n < 0
	result = 'Please input a non-negative integer'
end

if not(ischar(n))
	result = 'Please input a non-negative integer'
end

if not(isempty(n)) = 1
	result = 'Please input a non-negative integer'
end

if not(~isinf(x) & floor(x) == x)
    result = 'Please input a non-negative integer'
end

if n == 0 | n == 1
    result = 'Neither Prime nor Composite'
end

m = 2;
isprime = 1;

while (m <= sqrt(n))
    if(rem(n, m) == 0)
        isprime = 0;
        break;
    end
    m = m + 1;
end

if(isprime == 1)
    result = 'Prime'
else
    result = 'Composite'

end
```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.