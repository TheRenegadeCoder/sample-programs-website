---
authors:
- rzuckerm
date: 2025-01-01
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-01
layout: default
tags:
- baklava
- hack
title: Baklava in Hack
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/hack/how-to-implement-the-solution.md
- sources/programs/baklava/hack/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Hack](https://sampleprograms.io/languages/hack) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```hack
use namespace HH\Lib\Str;

<<__EntryPoint>>
function main(): void {
    for ($n = -10; $n <= 10; $n++) {
        $numSpaces = abs($n);
        $numStars = 21 - 2 * $numSpaces;
        echo Str\repeat(" ", $numSpaces) . Str\repeat("*", $numStars) . "\n";
    }
}

```

{% endraw %}

Baklava in [Hack](https://sampleprograms.io/languages/hack) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).