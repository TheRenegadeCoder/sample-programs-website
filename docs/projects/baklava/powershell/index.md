---
authors:
- rzuckerm
date: 2024-10-28
featured-image: baklava-in-every-language.jpg
last-modified: 2024-10-28
layout: default
tags:
- baklava
- powershell
title: Baklava in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/powershell/how-to-implement-the-solution.md
- sources/programs/baklava/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
for ($X = -10; $X -le 10; $X++) {
    $NumSpaces = [Math]::Abs($X)
    $Line = " " * $NumSpaces + "*" * (21 - 2 * $NumSpaces)
    Write-Output $Line
}

```

{% endraw %}

Baklava in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).