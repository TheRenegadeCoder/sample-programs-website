---
authors:
- pablocostass
- rzuckerm
date: 2019-10-11
featured-image: reverse-string-in-every-language.jpg
last-modified: 2023-03-19
layout: default
tags:
- clojure
- reverse-string
title: Reverse String in Clojure
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/clojure/how-to-implement-the-solution.md
- sources/programs/reverse-string/clojure/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Clojure](https://sampleprograms.io/languages/clojure) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```clojure
(ns reverse-string
	(:gen-class))

(defn main [args]
  (if (not= (count args) 0)
    (println(clojure.string/reverse (first args)))
  ))

(main *command-line-args*)

```

{% endraw %}

Reverse String in [Clojure](https://sampleprograms.io/languages/clojure) was written by:

- pablocostass
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).