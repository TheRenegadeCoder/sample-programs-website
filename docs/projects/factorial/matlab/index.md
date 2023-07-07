---
authors:
- sdmmssa
date: 2019-10-11
featured-image: factorial-in-every-language.jpg
last-modified: 2019-10-11
layout: default
tags:
- factorial
- matlab
title: Factorial in Matlab
---

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Matlab](https://sampleprograms.io/languages/matlab) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```matlab
function result=factorial(n)

if n<0
	error('Please input a non-negative integer')
end

if not(ischar(n))
	error('Please input a non-negative integer')
end

if isempty(n)=1
	error('Please input a non-negative integer')
end

x=1;

if n>0
	for i = 1:n
  
     		x=x*i;

	end
end

result = x
end

```

{% endraw %}

Factorial in [Matlab](https://sampleprograms.io/languages/matlab) was written by:

- sdmmssa

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).