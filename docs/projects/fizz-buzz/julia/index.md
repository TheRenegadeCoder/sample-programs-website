---
title: Fizz Buzz in Julia
layout: default
date: 2018-10-12
featured-image: fizz-buzz-in-every-language.png
last-modified: 2018-10-12

---

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Julia](https://sampleprograms.io/languages/julia) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

[Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Julia](https://sampleprograms.io/languages/julia) was written by:

- Michael King

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).