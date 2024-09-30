---
authors:
- Jeremy Grifski
- pablocostass
date: 2019-10-10
featured-image: capitalize-in-every-language.jpg
last-modified: 2019-10-26
layout: default
tags:
- capitalize
- clojure
title: Capitalize in Clojure
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/clojure/how-to-implement-the-solution.md
- sources/programs/capitalize/clojure/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Clojure](https://sampleprograms.io/languages/clojure) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```clojure
(ns capitalize
	(:gen-class))

(defn- is-valid-input [args]
  (and 
    (not= (count args) 0) 
    (not= (first args) "")))

(defn- print-error []
  (println "Usage: please provide a string"))

(defn- capitalize [s]
  (str 
    (clojure.string/upper-case 
      (subs s 0 1)) (subs s 1)
  ))

(defn main [args]
  (if (is-valid-input args) 
    (println (capitalize (first args)))
    (print-error)
  ))


(main *command-line-args*)

```

{% endraw %}

Capitalize in [Clojure](https://sampleprograms.io/languages/clojure) was written by:

- Jeremy Grifski
- pablocostass

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).