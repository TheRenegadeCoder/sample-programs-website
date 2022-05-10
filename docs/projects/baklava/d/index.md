---

title: Baklava in D
layout: default
date: 2022-04-28
last-modified: 2022-05-10

---

Welcome to the Baklava in D page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```d
import std.stdio, std.array;

void main (string[ ] args)
{

    for (byte i = 0; i < 10; i++)
        writeln (
            " ".replicate (10 - i), "*".replicate (i * 2 + 1)
        );

    for (byte i = 10; -1 < i; i--)
        writeln (
            " ".replicate (10 - i), "*".replicate (i * 2 + 1)
        );

}
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).