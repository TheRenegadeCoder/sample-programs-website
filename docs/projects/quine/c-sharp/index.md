---
title: Quine in C#
layout: default
date: 2018-12-30
featured-image: quine-in-every-language.jpg
last-modified: 2018-12-30

---

Welcome to the [Quine](https://sampleprograms.io/projects/quine) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
class Quine { static void Main() { var s = "class Quine {{ static void Main() {{ var s = {0}{1}{0}; System.Console.WriteLine(s, (char)34, s); }} }}"; System.Console.WriteLine(s, (char)34, s); } }
```

{% endraw %}

[Quine](https://sampleprograms.io/projects/quine) in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).