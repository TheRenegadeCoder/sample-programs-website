---
title: Even Odd in Matlab
layout: default
date: 2019-10-11
featured-image: even-odd-in-every-language.jpg
last-modified: 2019-10-11

---

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Matlab](https://sampleprograms.io/languages/matlab) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```matlab
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

[Even Odd](https://sampleprograms.io/projects/even-odd) in [Matlab](https://sampleprograms.io/languages/matlab) was written by:

- Jeremy Grifski
- sakurakhadag

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 22 2021 15:02:49. The solution was first committed on Oct 11 2019 15:40:27. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).