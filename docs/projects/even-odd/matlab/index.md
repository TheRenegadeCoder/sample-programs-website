---

---

Welcome to the Even Odd in Matlab page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Matlab
function result_string= odd_even(number)

%number - input by user
%result_string - output determined by this program
   
if (nargin==0)
    %if there was no input
    result_string = 'please input a number';
elseif ~isnumeric(number) || mod(number,1) ~= 0
    %check whether input is a number
    %also check if input is an integer
    result_string = 'please input a number';
else
    if mod(number,2) == 0
        result_string = 'Even';
    else
        result_string = 'Odd';
    end
end
end
        
```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.