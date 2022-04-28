---

---

# Selection Sort in Matlab

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Matlab
function sorted = selection_sort(array)
  if nargin == 0 || length(array)<=1
      fprintf("Usage: please provide a list of at least two integers to sort in the format [1 2 3 4 5]\n");
      return
  end  
  
  sorted = [];
  while ~isempty(array)
      x = min(array);
      sorted = [ sorted array(array==x) ];
      array(array==x) = [];  
  end
end
```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.