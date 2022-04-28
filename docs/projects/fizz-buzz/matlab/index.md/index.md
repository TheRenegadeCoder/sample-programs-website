---

---

Welcome to the Fizz Buzz in Matlab page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Matlab
function [] = fizzBuzz(x)

  % Loop from 1 to 100
  for i = 1:100
    fizzbuzz = '';
    
    % Check if i is divisible by 3
    if mod(i,3) == 0
      fizzbuzz = [fizzbuzz 'Fizz'];
    end
    
    % Check if i is divisible by 5
    if mod(i,5) == 0
      fizzbuzz = [fizzbuzz 'Buzz'];
    end
    
    % If fizzbuzz variable is empty,print i
    if isempty(fizzbuzz)
      disp(i)
    else
      % If fizzbuzz variable is not empty, print the variable
      disp(fizzbuzz)
    end
  end
end
```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.