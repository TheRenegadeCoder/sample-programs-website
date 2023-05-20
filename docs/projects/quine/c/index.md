---
title: Quine in C
layout: default
date: 2019-10-18
featured-image: quine-in-every-language.jpg
last-modified: 2019-10-18

---

Welcome to the [Quine](https://sampleprograms.io/projects/quine) in [C](https://sampleprograms.io/languages/c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c
#include "stdio.h"
int main() { char* s="#include %cstdio.h%c%cint main() { char* s=%c%s%c; printf(s,34,34,10,34,s,34,10); return 0; }%c"; printf(s,34,34,10,34,s,34,10); return 0; }
```

{% endraw %}

[Quine](https://sampleprograms.io/projects/quine) in [C](https://sampleprograms.io/languages/c) was written by:

- Juan D Frias

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).