---

title: Fizz Buzz in Julia
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Fizz Buzz in Julia page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```julia
#!/usr/bin/julia

for i = 1:100
    str = i % 3 == 0 ? "Fizz" : ""
    str *= i % 5 == 0 ? "Buzz" : ""
    if isempty(str)
        str = i
    end
    println(str)
end
```

{% endraw %}

Fizz Buzz in Julia was written by:

- Michael King

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).