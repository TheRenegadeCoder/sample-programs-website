---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-04-10
featured-image: quine-in-every-language.jpg
last-modified: 2026-04-10
layout: default
tags:
- f-sharp
- quine
title: Quine in F#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/quine/f-sharp/how-to-implement-the-solution.md
- sources/programs/quine/f-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Quine](https://sampleprograms.io/projects/quine) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
let s = "let s = {0}{1}{0} in System.Console.WriteLine(s, char 34, s);;" in System.Console.WriteLine(s, char 34, s);;
```

{% endraw %}

Quine in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).