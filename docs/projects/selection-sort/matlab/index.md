---

title: Selection Sort in Matlab
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Selection Sort in Matlab page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```matlab
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

{% endraw %}

Selection Sort in Matlab was written by:

- iwishiwasaneagle

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).