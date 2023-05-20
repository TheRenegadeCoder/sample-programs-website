---
title: Capitalize in Matlab
layout: default
date: 2020-10-02
featured-image: capitalize-in-every-language.jpg
last-modified: 2020-10-02

---

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Matlab](https://sampleprograms.io/languages/matlab) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```matlab
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

[Capitalize](https://sampleprograms.io/projects/capitalize) in [Matlab](https://sampleprograms.io/languages/matlab) was written by:

- iwishiwasaneagle

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 02 2020 11:51:28. The solution was first committed on Oct 02 2020 11:42:05. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).