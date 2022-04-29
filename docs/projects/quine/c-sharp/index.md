---

title: Quine in C#
layout: default
date: 2022-04-28
last-modified: 2022-04-28

---

Welcome to the Quine in C# page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```C#
class Quine { static void Main() { var s = "class Quine {{ static void Main() {{ var s = {0}{1}{0}; System.Console.WriteLine(s, (char)34, s); }} }}"; System.Console.WriteLine(s, (char)34, s); } }
```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.