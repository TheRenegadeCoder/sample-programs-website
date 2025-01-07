---
authors:
- Zia
date: 2025-01-07
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-07
layout: default
tags:
- baklava
- elvish
title: Baklava in Elvish
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/elvish/how-to-implement-the-solution.md
- sources/programs/baklava/elvish/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Elvish](https://sampleprograms.io/languages/elvish) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```elvish
# By github.com/Kaamkiya

for i [(range 11) (range 9 -1)] {
  var line = ''

  range (- 10 $i) | each { |_| set line = $line' '}
  range (+ 1 (* 2 $i)) | each { |_| set line = $line'*' }

  echo $line
}

```

{% endraw %}

Baklava in [Elvish](https://sampleprograms.io/languages/elvish) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).