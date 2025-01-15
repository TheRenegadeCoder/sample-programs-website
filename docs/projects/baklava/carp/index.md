---
authors:
- rzuckerm
date: 2025-01-15
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-15
layout: default
tags:
- baklava
- carp
title: Baklava in Carp
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/carp/how-to-implement-the-solution.md
- sources/programs/baklava/carp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Carp](https://sampleprograms.io/languages/carp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```carp
(defn main[]
  (for [n -10 11]
    (do
      (let [
        num-spaces (abs n)
        num-stars (- 21 (* 2 num-spaces))
      ]
        (println* (String.repeat num-spaces " ") (String.repeat num-stars "*"))
      )
    )
  )
)

```

{% endraw %}

Baklava in [Carp](https://sampleprograms.io/languages/carp) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).