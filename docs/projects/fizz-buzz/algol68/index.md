---

title: Fizz Buzz in Algol68
layout: default
date: 2022-04-28
last-modified: 2023-01-21

---

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Algol68](https://sampleprograms.io/languages/algol68) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```algol68
FOR n FROM 1 TO 100
DO
    IF n MOD 3 = 0
    THEN
        print((n MOD 5 = 0 | "FizzBuzz" | "Fizz"))
    ELIF n MOD 5 = 0
    THEN
        print("Buzz")
    ELSE
        print(whole(n, 0))
    FI;

    print(newline)
OD
```

{% endraw %}

[Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Algol68](https://sampleprograms.io/languages/algol68) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).