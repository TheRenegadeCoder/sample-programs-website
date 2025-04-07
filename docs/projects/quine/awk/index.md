---
authors:
- rzuckerm
date: 2025-04-07
featured-image: quine-in-every-language.jpg
last-modified: 2025-04-07
layout: default
tags:
- awk
- quine
title: Quine in Awk
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/quine/awk/how-to-implement-the-solution.md
- sources/programs/quine/awk/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Quine](https://sampleprograms.io/projects/quine) in [Awk](https://sampleprograms.io/languages/awk) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```awk
BEGIN{s="BEGIN{s=%c%s%c;printf(s,34,s,34,10)}%c";printf(s,34,s,34,10)}

```

{% endraw %}

Quine in [Awk](https://sampleprograms.io/languages/awk) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).