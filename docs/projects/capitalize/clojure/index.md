---
title: Capitalize in Clojure
layout: default
date: 2019-10-10
featured-image: capitalize-in-every-language.jpg
last-modified: 2019-10-10

---

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

[Capitalize](https://sampleprograms.io/projects/capitalize) in [Clojure](https://sampleprograms.io/languages/clojure) was written by:

- Jeremy Grifski
- pablocostass

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 26 2019 23:49:48. The solution was first committed on Oct 10 2019 23:54:24. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).