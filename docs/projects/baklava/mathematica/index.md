---

title: Baklava in Mathematica
layout: default
date: 2022-04-28
last-modified: 2023-04-02

---

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

TableForm[
   Table[
    Table[
     (* asterisk or space depending on Manhattan distance *)
     If[Abs[i] + Abs[j] <= #, "*", " "],
     {i, -#, +#}],
    {j, -#, +#}],
   TableSpacing -> {0, 0}] &[10]
```

{% endraw %}

[Baklava](https://sampleprograms.io/projects/baklava) in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).