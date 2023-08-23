---
authors:
- Ron Zuckerman
- smaludzi
date: 2018-09-20
featured-image: reverse-string-in-every-language.jpg
last-modified: 2023-08-23
layout: default
tags:
- never
- reverse-string
title: Reverse String in Never
---

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Never](https://sampleprograms.io/languages/never) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```never
func reverse(s: string) -> string
{
    let n = length(s);
    (n > 0) ? s[n - 1 .. 0] : ""
}

func main(argv[argc]: string) -> int
{
    let s = (argc > 1) ? argv[1] : "";
    prints(reverse(s) + "\n");
    0
}

```

{% endraw %}

Reverse String in [Never](https://sampleprograms.io/languages/never) was written by:

- Ron Zuckerman
- smaludzi

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).