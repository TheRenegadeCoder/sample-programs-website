---

title: Fibonacci in Boo
layout: default
date: 2022-04-28
last-modified: 2022-05-10

---

Welcome to the Fibonacci in Boo page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).