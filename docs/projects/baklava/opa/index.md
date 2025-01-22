---
authors:
- rzuckerm
date: 2025-01-22
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-22
layout: default
tags:
- baklava
- opa
title: Baklava in Opa
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/opa/how-to-implement-the-solution.md
- sources/programs/baklava/opa/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Opa](https://sampleprograms.io/languages/opa) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```opa
function page() {
    <pre>{baklava()}</pre>
}

function baklava() {
    recursive function baklava_rec(lines, n) {
        if (n > 0) lines + baklava_line(n) + baklava_rec(lines, n - 1) else lines + baklava_line(n)
    }

    baklava_rec("", 20)
}

function baklava_line(n) {
    num_spaces = Int.abs(n - 10)
    num_stars = 21 - 2 * num_spaces
    String.repeat(num_spaces, " ") + String.repeat(num_stars, "*") + "\n"
}

Server.start(
   Server.http,
   { title: "Baklava", page: page}
)

```

{% endraw %}

Baklava in [Opa](https://sampleprograms.io/languages/opa) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).