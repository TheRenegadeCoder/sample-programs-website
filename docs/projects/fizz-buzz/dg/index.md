---

title: Fizz Buzz in Dg
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Fizz Buzz in Dg page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Dg
fizz_buzz = n -> if
    n % 15 == 0 => "FizzBuzz"
    n % 3  == 0 => "Fizz"
    n % 5  == 0 => "Buzz"
    otherwise   => n

main = start end ruleset ->
    for i in range start (end + 1) =>
        print <| ruleset i

main 1 100 fizz_buzz
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).