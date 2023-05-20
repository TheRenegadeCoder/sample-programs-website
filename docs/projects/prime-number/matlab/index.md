---
title: Prime Number in Matlab
layout: default
date: 2019-10-14
featured-image: prime-number-in-every-language.jpg
last-modified: 2019-10-14

---

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Matlab](https://sampleprograms.io/languages/matlab) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```matlab
function result = prime_number(n)

if n < 0
    result = 'Please input a non-negative integer'
end

if not(ischar(n))
    result = 'Please input a non-negative integer'
end

if not(isempty(n)) = 1
    result = 'Please input a non-negative integer'
end

if not(~isinf(x) & floor(x) == x)
    result = 'Please input a non-negative integer'
end

if n == 0 | n == 1
    result = 'Neither Prime nor Composite'
end

m = 2;
isprime = 1;

while (m <= sqrt(n))
    if(rem(n, m) == 0)
        isprime = 0;
        break;
    end
    m = m + 1;
end

if(isprime == 1)
    result = 'Prime'
else
    result = 'Composite'

end
```

{% endraw %}

[Prime Number](https://sampleprograms.io/projects/prime-number) in [Matlab](https://sampleprograms.io/languages/matlab) was written by:

- rpartha

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).