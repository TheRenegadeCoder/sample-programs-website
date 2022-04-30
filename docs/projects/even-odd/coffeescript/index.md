---

title: Even Odd in Coffeescript
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Even Odd in Coffeescript page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```coffeescript
USAGE = "Usage: please input a number"
main = (arg) ->
  numberParsed = parseInt(arg)
  isNumber = Number.isInteger(numberParsed)
  if isNumber
    if numberParsed % 2 == 0 then "Even" else "Odd"
  else
    USAGE

console.log main(process.argv[2])
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).