---

title: Baklava in Groovy
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Baklava in Groovy page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Groovy
(0..9).each{ index ->
    println "${' ' * (10 - index)}${'*' * (index * 2 + 1)}"
}
(9..0).each{ index ->
    println "${' ' * (10 - index)}${'*' * (index * 2 + 1)}"
}
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).