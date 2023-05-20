---
title: Baklava in Solisp
layout: default
date: 2020-03-01
featured-image: baklava-in-every-language.jpg
last-modified: 2020-03-01

---

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Solisp](https://sampleprograms.io/languages/solisp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```solisp
(Join (Map x (Append (Seq 0 10) (Reverse (Seq 0 9)))
    (Join (Append
        (Clone (- 10 x) " ")
        (Clone (+ (* x 2) 1) "#")
    ))
) "\n")
```

{% endraw %}

[Baklava](https://sampleprograms.io/projects/baklava) in [Solisp](https://sampleprograms.io/languages/solisp) was written by:

- Stuart Irwin

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).