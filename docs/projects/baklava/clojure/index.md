---
authors:
- rzuckerm
date: 2025-01-15
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-15
layout: default
tags:
- baklava
- clojure
title: Baklava in Clojure
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/clojure/how-to-implement-the-solution.md
- sources/programs/baklava/clojure/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Clojure](https://sampleprograms.io/languages/clojure) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```clojure
(ns baklava
  (:gen-class)
  (:require [clojure.string :refer [join]])
)

(defn repeat-string [n, s]
  (join (repeat n s))
)

(defn baklava-line [n]
  (def num-spaces (abs (- n 10)))
  (def num-stars (- 21 (* 2 num-spaces)))
  (str (repeat-string num-spaces " ") (repeat-string num-stars "*"))
)

(defn baklava [n]
  (join "\n" (map baklava-line (range 0 n)))
)

(println (baklava 21))

```

{% endraw %}

Baklava in [Clojure](https://sampleprograms.io/languages/clojure) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).