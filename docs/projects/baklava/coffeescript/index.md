---

title: Baklava in Coffeescript
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Baklava in Coffeescript page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Coffeescript
for i in [0...10]
  pattern = " ".repeat (10 - i)
  pattern += "*".repeat (i * 2 + 1)
  console.log pattern

for i in [10..0]
  pattern = " ".repeat (10 - i)
  pattern += "*".repeat (i * 2 + 1)
  console.log pattern
```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.