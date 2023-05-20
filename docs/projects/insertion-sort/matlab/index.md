---
title: Insertion Sort in Matlab
layout: default
date: 2020-10-05
featured-image: insertion-sort-in-every-language.jpg
last-modified: 2020-10-05

---

Welcome to the [Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [Matlab](https://sampleprograms.io/languages/matlab) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```matlab
function sorted = insertion_sort(array)
% Insertion sort in ascending order

if(size(array,1)>1)
    error('Input must be a 1xN vector');
end
if(isempty(array))
    error('Input should not be empty');
end
disp(['Array to be sorted: ' num2str(array)]);
n = length(array);
for i = 2:n
    d = i;    
    while((d > 1) && (array(d) < array(d-1)))
        temp = array(d);
        array(d) = array(d-1);
        array(d-1) = temp;
        d = d-1;
    end
end
sorted = array;
disp(['Sorted Array: ' num2str(array)]);
end

input_array = [9 8 7 6 5 4];
%input_array element can be different
output_array = insertion_sort(input_array);
```

{% endraw %}

[Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [Matlab](https://sampleprograms.io/languages/matlab) was written by:

- aiashwarj kumar

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).