---
authors:
- Jeremy Grifski
- Matt Wiley
date: 2019-10-10
featured-image: factorial-in-every-language.jpg
last-modified: 2020-10-15
layout: default
tags:
- factorial
- lua
title: Factorial in Lua
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/lua/how-to-implement-the-solution.md
- sources/programs/factorial/lua/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Lua](https://sampleprograms.io/languages/lua) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lua

--
-- Calculate the factorial
--
factorial = function(num)
    product = 1
    if num > 1
    then
        for i = 2, num 
        do
            product = product * i
        end
    end
    return product
end

--
-- Main executable logic
--
main = function(input)
    maxInput = 20
    usage = "Usage: please input a non-negative integer"

    if not (input == nil or input == "")
    then
        inputValidation = input:gsub('[0-9]','')
        if inputValidation:len() == 0
        then
            inputNum = tonumber(input)
            if inputNum > maxInput
            then
                print('Input of ' .. inputNum .. ' is too large to calculate a factorial for. Max input is ' .. maxInput .. '.')
            else
                print(factorial(tonumber(input)))
            end
        else
            print(usage)
        end
    else
        print(usage)
    end

end

-- Run the script
main(arg[1])

```

{% endraw %}

Factorial in [Lua](https://sampleprograms.io/languages/lua) was written by:

- Jeremy Grifski
- Matt Wiley

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).