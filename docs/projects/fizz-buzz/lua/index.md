---
title: Fizz Buzz in Lua
layout: default
date: 2018-09-19
featured-image: fizz-buzz-in-every-language.png
last-modified: 2018-09-19

---

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Lua](https://sampleprograms.io/languages/lua) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lua
for i = 1, 100 do
    output = ""

    if i % 3 == 0 then
        output = output .. "Fizz"
    end

    if i % 5 == 0 then
        output = output .. "Buzz"
    end

    if output == "" then
        output = i
    end

    print(output)
end
```

{% endraw %}

[Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Lua](https://sampleprograms.io/languages/lua) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).