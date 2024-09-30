---
authors:
- darkpanda08
- rzuckerm
date: 2020-10-01
featured-image: fizz-buzz-in-every-language.png
last-modified: 2023-12-09
layout: default
tags:
- fizz-buzz
- octave
title: Fizz Buzz in Octave
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/octave/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/octave/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Octave](https://sampleprograms.io/languages/octave) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```octave
function fizz_buzz()

  % Loop from 1 to 100
  for i = 1:100
    fizzbuzz = '';
    
    % Check if i is divisible by 3
    if mod(i,3) == 0
      fizzbuzz = [fizzbuzz 'Fizz'];
    end
    
    % Check if i is divisible by 5
    if mod(i,5) == 0
      fizzbuzz = [fizzbuzz 'Buzz'];
    end
    
    % If fizzbuzz variable is empty,print i
    if isempty(fizzbuzz)
      disp(i);
    else
      % If fizzbuzz variable is not empty, print the variable
      disp(fizzbuzz);
    end
  end
end

```

{% endraw %}

Fizz Buzz in [Octave](https://sampleprograms.io/languages/octave) was written by:

- darkpanda08
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).