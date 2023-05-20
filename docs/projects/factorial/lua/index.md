---
title: Factorial in Lua
layout: default
date: 2019-10-10
featured-image: factorial-in-every-language.jpg
last-modified: 2019-10-10

---

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

[Factorial](https://sampleprograms.io/projects/factorial) in [Lua](https://sampleprograms.io/languages/lua) was written by:

- Jeremy Grifski
- Matt Wiley

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 15 2020 19:22:39. The solution was first committed on Oct 10 2019 12:43:45. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).