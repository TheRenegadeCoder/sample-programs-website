---
authors:
- rzuckerm
date: 2025-01-06
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-06
layout: default
tags:
- baklava
- ferret
title: Baklava in Ferret
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/ferret/how-to-implement-the-solution.md
- sources/programs/baklava/ferret/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Ferret](https://sampleprograms.io/languages/ferret) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ferret
(defn print-repeat-string
  ([s n]
    (if (> n 0)
      (do
        (print s)
        (print-repeat-string s (dec n))
      )
    )
  )
)

(defn baklava-line
  ([n]
    (let [
      num-spaces (abs n)
      num-stars (- 21 (* 2 num-spaces))
    ]
      (print-repeat-string " " num-spaces)
      (print-repeat-string "*" num-stars)
      (println)
    )
  )
)

(defn baklava
  ([n ne]
    (if (<= n ne)
      (do
        (baklava-line n)
        (baklava (inc n) ne)
      )
    )
  )
)

(do
  (baklava -10 10)
)

```

{% endraw %}

Baklava in [Ferret](https://sampleprograms.io/languages/ferret) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).