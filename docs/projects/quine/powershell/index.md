---
authors:
- rzuckerm
date: 2025-05-12
featured-image: quine-in-every-language.jpg
last-modified: 2025-05-12
layout: default
tags:
- powershell
- quine
title: Quine in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/quine/powershell/how-to-implement-the-solution.md
- sources/programs/quine/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Quine](https://sampleprograms.io/projects/quine) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
$S='$S={0}{1}{0}{2}Write-Host ($S -f [string][char]39,$S,[string][char]10)'
Write-Host ($S -f [string][char]39,$S,[string][char]10)

```

{% endraw %}

Quine in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).