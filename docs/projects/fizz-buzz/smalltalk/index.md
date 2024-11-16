---
authors:
- Augy Markham
date: 2024-11-16
featured-image: fizz-buzz-in-every-language.png
last-modified: 2024-11-16
layout: default
tags:
- fizz-buzz
- smalltalk
title: Fizz Buzz in Smalltalk
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/smalltalk/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/smalltalk/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Smalltalk](https://sampleprograms.io/languages/smalltalk) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```smalltalk
"Loop 1 to 100"
1 to: 100 do: [ :i |
	
	"If the number isn't divisible by 3 or 5, show the number"
	i \\ 3 = 0 ifFalse: [i \\ 5 = 0 ifFalse: [Transcript show: (i  printString); cr]].
	
	"If the number is divisible by 3 AND 5, show 'FizzBuzz'"
	i \\ 3 = 0 ifTrue: [i \\ 5 = 0 ifTrue: [Transcript show: 'FizzBuzz' ; cr]].

	"If the number is only divisible by 3, show 'Fizz'"
	i \\ 3 = 0 ifTrue: [i \\ 5 = 0 ifFalse: [Transcript show: 'Fizz' ; cr]].
	
	"If the number is only divisible by 5, show 'Buzz"
	i \\ 5 = 0 ifTrue: [i \\ 3 = 0 ifFalse: [Transcript show: 'Buzz' ; cr]].
	].
```

{% endraw %}

Fizz Buzz in [Smalltalk](https://sampleprograms.io/languages/smalltalk) was written by:

- Augy Markham

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).