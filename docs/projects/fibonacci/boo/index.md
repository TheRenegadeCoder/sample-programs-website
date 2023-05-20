---
title: Fibonacci in Boo
layout: default
date: 2020-10-02
featured-image: fibonacci-in-every-language.jpg
last-modified: 2020-10-02

---

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Boo](https://sampleprograms.io/languages/boo) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```boo
def fib():
    a, b = 0L, 1L       # The 'L's make the numbers double word length (typically 64 bits)
    while true:
        yield b
        a, b = b, a + b

# Print the first 5 numbers in the series:
for index as int, element in zip(range(5), fib()):
    print("${index+1}: ${element}")
```

{% endraw %}

[Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Boo](https://sampleprograms.io/languages/boo) was written by:

- Subhayu Roy

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).