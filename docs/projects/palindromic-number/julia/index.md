---
authors:
- smjalageri
date: 2022-10-11
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2022-10-11
layout: default
tags:
- julia
- palindromic-number
title: Palindromic Number in Julia
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/julia/how-to-implement-the-solution.md
- sources/programs/palindromic-number/julia/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Julia](https://sampleprograms.io/languages/julia) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```julia
function err() 
  println("Usage: please input a non-negative integer")
end

function palindrome_check(n)
  new_num = 0
  original = n
  while (n > 0)
    digit = n % 10
    new_num = new_num * 10 + digit 
    n ÷= 10
  end

  if(new_num == original)
      return "true"
  else
      return "false"
  end
end

try
   n = parse(Int, ARGS[1])
   if (n >= 0)
     println(palindrome_check(n))
   else
     err()
   end
catch e
   err()
end

```

{% endraw %}

Palindromic Number in [Julia](https://sampleprograms.io/languages/julia) was written by:

- smjalageri

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).