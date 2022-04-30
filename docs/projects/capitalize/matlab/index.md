---

title: Capitalize in Matlab
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Capitalize in Matlab page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

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

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).