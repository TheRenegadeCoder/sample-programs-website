---

title: Even Odd in Matlab
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Even Odd in Matlab page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).