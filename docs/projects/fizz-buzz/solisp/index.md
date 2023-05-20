---
title: Fizz Buzz in Solisp
layout: default
date: 2020-02-25
featured-image: fizz-buzz-in-every-language.png
last-modified: 2020-02-25

---

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Solisp](https://sampleprograms.io/languages/solisp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```solisp
(Join (Map num (Seq 1 100)
    (Switch
        {(== (% num 3) (% num 5) 0) "FizzBuzz"}
        {(== (% num 3) 0) "Fizz"}
        {(== (% num 5) 0) "Buzz"}
        {true num}
    )
) "\n")
```

{% endraw %}

[Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Solisp](https://sampleprograms.io/languages/solisp) was written by:

- Stuart Irwin

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Mar 23 2020 14:34:09. The solution was first committed on Feb 25 2020 15:47:14. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).