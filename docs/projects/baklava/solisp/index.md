---
authors:
- rzuckerm
- Stuart Irwin
date: 2020-03-01
featured-image: baklava-in-every-language.jpg
last-modified: 2023-09-24
layout: default
tags:
- baklava
- solisp
title: Baklava in Solisp
---

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Solisp](https://sampleprograms.io/languages/solisp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```solisp
(JoinD newline (Map x (Append (Seq 0 10) (Reverse (Seq 0 9)))
	(Append
		(Clone (- 10 x) " ")
		(Clone (+ (* x 2) 1) (Force Char 42))
    )
))
```

{% endraw %}

Baklava in [Solisp](https://sampleprograms.io/languages/solisp) was written by:

- rzuckerm
- Stuart Irwin

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).