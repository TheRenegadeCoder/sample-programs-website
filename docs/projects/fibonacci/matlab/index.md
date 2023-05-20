---
title: Fibonacci in Matlab
layout: default
date: 2019-10-24
featured-image: fibonacci-in-every-language.jpg
last-modified: 2019-10-24

---

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Matlab](https://sampleprograms.io/languages/matlab) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```matlab
function f = fibonacci(n)

if ischar(n)
    error('Usage: please input the count of fibonacci numbers to output')
end

if n < 0
    error('Usage: please input a non-negative integer')
end

if not(n==round(n))
    error('Usage: please input an integer, not a floating point')
end


a(1) = 1;
a(2) = 1;


for i=1:n
  a(i+2)=a(i+1)+a(i);
end

f = mat2str(a);

end
```

{% endraw %}

[Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Matlab](https://sampleprograms.io/languages/matlab) was written by:

- Gabi Herman
- gabiherman

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Nov 05 2019 15:10:54. The solution was first committed on Oct 24 2019 15:37:31. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).