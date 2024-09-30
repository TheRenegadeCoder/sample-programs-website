---
authors:
- bhaskar_datta
- Jeremy Grifski
date: 2019-10-27
featured-image: prime-number-in-every-language.jpg
last-modified: 2020-10-15
layout: default
tags:
- lua
- prime-number
title: Prime Number in Lua
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/lua/how-to-implement-the-solution.md
- sources/programs/prime-number/lua/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Lua](https://sampleprograms.io/languages/lua) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lua
--returns true if prime
function isPrime(n)
    comp = "Composite"
    prime = "Prime"
    usage = "Usage: please input a non-negative integer"
    local n = tonumber(n)
    --catch nil, negative and non int numbers
    if not n or n < 0 or (n % 1 ~= 0) then 
        print(usage)
    --catch 0 and 1
    elseif n < 2 then
        print(comp)
    --catch even number above 2
    elseif n > 2 and (n % 2 == 0) then 
        print(comp)
    --catch numbers that end in 5 or 0 (multiples of 5)
    elseif n>5 and (n % 5 ==0) then 
        print(comp)
    --now check for prime
    else
        --only do the odds
        result = prime
        for i = 3, math.sqrt(n), 2 do
            --did it divide evenly
            if (n % i == 0) then
                result = comp
            end
        end
        --can defeat optimus
        print(result)
    end
end

isPrime(arg[1])

```

{% endraw %}

Prime Number in [Lua](https://sampleprograms.io/languages/lua) was written by:

- bhaskar_datta
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).