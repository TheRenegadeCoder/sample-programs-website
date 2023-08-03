---
authors:
- rzuckerm
date: 2023-08-02
featured-image: quine-in-every-language.jpg
last-modified: 2023-08-02
layout: default
tags:
- gnu-make
- quine
title: Quine in Gnu Make
---

Welcome to the [Quine](https://sampleprograms.io/projects/quine) in [Gnu Make](https://sampleprograms.io/languages/gnu-make) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```gnu_make
q=$(info q=$(value q))$(info $$(q))$(eval q:;@:)
$(q)

```

{% endraw %}

Quine in [Gnu Make](https://sampleprograms.io/languages/gnu-make) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).