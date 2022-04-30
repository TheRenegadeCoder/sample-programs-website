---

title: Baklava in Crystal
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Baklava in Crystal page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Crystal
a = -1
loop do
  a += 1
  puts ((" " * (10 - a)) + ("*" * (a * 2 + 1)))
  break if a == 10
end

b = 10
loop do
  b -= 1
  puts ((" " * (10 - b)) + ("*" * (b * 2 + 1)))
  break if b == 0
end
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).