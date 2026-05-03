---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-10
featured-image: quine-in-every-language.jpg
last-modified: 2026-04-10
layout: default
tags:
- c-plus-plus
- quine
title: Quine in C++
title1: Quine
title2: in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/quine/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/quine/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Quine](https://sampleprograms.io/projects/quine) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <cstdio>
char*s="#include <cstdio>%cchar*s=%c%s%c;%cint main(){printf(s,10,34,s,34,10,10);}%c";
int main(){printf(s,10,34,s,34,10,10);}
```

{% endraw %}

Quine in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).