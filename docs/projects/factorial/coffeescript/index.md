---

title: Factorial in Coffeescript
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Factorial in Coffeescript page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```coffeescript
factorial = (n) ->
    return usage() if n < 0
    return 1 if n == "0"
    [1..n].reduce (x, y) -> x * y
    
usage = () ->
    "Usage: please input a non-negative integer"
    
main = () ->
    args = process.argv
    return factorial(args[2]) if args.length == 3 and isFinite(args[2]) and args[2] != ""
    usage()

console.log main()
```

{% endraw %}

Factorial in Coffeescript was written by:

- Jeremy Grifski
- Hanyuan Li

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 15 2020 22:14:45. The solution was first committed on Oct 11 2019 21:51:03. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).