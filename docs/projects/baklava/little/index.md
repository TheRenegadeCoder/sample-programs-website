---
authors:
- rzuckerm
date: 2024-12-27
featured-image: baklava-in-every-language.jpg
last-modified: 2024-12-27
layout: default
tags:
- baklava
- little
title: Baklava in Little
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/little/how-to-implement-the-solution.md
- sources/programs/baklava/little/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Little](https://sampleprograms.io/languages/little) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```little
string repeat_string(string s, int n) {
    int i;
    string result = "";
    for (i = 0; i < n; i++) {
        result[END + 1] = s;
    }

    return result;
}

int n, numSpaces, numStars;
for (n = -10; n <= 10; n++) {
    numSpaces = abs(n);
    numStars = 21 - 2 * numSpaces;
    printf("%s%s\n", repeat_string(" ", numSpaces), repeat_string("*", numStars));
}

```

{% endraw %}

Baklava in [Little](https://sampleprograms.io/languages/little) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).