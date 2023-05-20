---
title: Fizz Buzz in Matlab
layout: default
date: 2020-10-01
featured-image: fizz-buzz-in-every-language.png
last-modified: 2020-10-01

---

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Matlab](https://sampleprograms.io/languages/matlab) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```matlab
function [] = fizzBuzz(x)

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
      disp(i)
    else
      % If fizzbuzz variable is not empty, print the variable
      disp(fizzbuzz)
    end
  end
end
```

{% endraw %}

[Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Matlab](https://sampleprograms.io/languages/matlab) was written by:

- darkpanda08

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).