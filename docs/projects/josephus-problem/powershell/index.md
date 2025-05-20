---
authors:
- rzuckerm
date: 2025-05-20
featured-image: josephus-problem-in-every-language.jpg
last-modified: 2025-05-20
layout: default
tags:
- josephus-problem
- powershell
title: Josephus Problem in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/josephus-problem/powershell/how-to-implement-the-solution.md
- sources/programs/josephus-problem/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Josephus Problem](https://sampleprograms.io/projects/josephus-problem) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
function Show-Usage() {
    Write-Host "Usage: please input the total number of people and number of people to skip."
    Exit 1
}

<#
Reference: https://en.wikipedia.org/wiki/Josephus_problem#The_general_case

Use zero-based index algorithm:

    g(1, k) = 0
    g(m, k) = [g(m - 1, k) + k] MOD m, for m = 2, 3, ..., n

Final answer is g(n, k) + 1 to get back to one-based index
#>
function Get-JosephusProblem([int]$N, [int]$K) {
    $G = 0
    for ($M = 2; $M -le $N; $M++) {
        $G = ($G + $K) % $M
    }

    $G + 1
}

if ($args.Length -lt 2) {
    Show-Usage
}

try {
    $N = [int]::Parse($args[0])
    $K = [int]::Parse($args[1])
} catch {
    Show-Usage
}

Write-Host (Get-JosephusProblem $N $K)

```

{% endraw %}

Josephus Problem in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).