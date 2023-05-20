---
title: Reverse String in Clojure
layout: default
date: 2019-10-11
featured-image: reverse-string-in-every-language.jpg
last-modified: 2019-10-11

---

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

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Clojure](https://sampleprograms.io/languages/clojure) was written by:

- pablocostass
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Mar 19 2023 22:24:49. The solution was first committed on Oct 11 2019 00:07:12. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).