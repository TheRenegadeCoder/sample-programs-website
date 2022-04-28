---

---

# Capitalize in Matlab

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Matlab
function capString = capitalize(string)
    if(nargin==0)
        fprintf("Usage: please provide a string\n");
    else
        if(strlength(string)==0)
            fprintf("Usage: please provide a string\n");
        else
            string = char(string);
            capString = convertCharsToStrings(strcat(upper(string(1:1)),string(2:end)));
        end
    end
end
```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.