---
authors:
- rzuckerm
date: 2025-01-20
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-20
layout: default
tags:
- baklava
- ballerina
title: Baklava in Ballerina
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/ballerina/how-to-implement-the-solution.md
- sources/programs/baklava/ballerina/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Ballerina](https://sampleprograms.io/languages/ballerina) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ballerina
import ballerina/io;

public function main(string... args) {
    foreach int n in int:range(-10, 11, 1) {
        int numSpaces = int:abs(n);
        int numStars = 21 - 2 * numSpaces;
        io:println("".padEnd(numSpaces, " ") + "".padEnd(numStars, "*"));
    }
}

```

{% endraw %}

Baklava in [Ballerina](https://sampleprograms.io/languages/ballerina) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).