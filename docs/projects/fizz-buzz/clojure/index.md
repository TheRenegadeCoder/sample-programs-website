---
title: Fizz Buzz in Clojure
layout: default
date: 2020-10-04
featured-image: fizz-buzz-in-every-language.png
last-modified: 2020-10-04

---

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Clojure](https://sampleprograms.io/languages/clojure) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```clojure
(ns fizzbuzz
  (:gen-class)
  (:require [clojure.string :refer [join]]))

(defn- is-multiple-of-3 [n]
  (= (mod n 3) 0))

(defn- is-multiple-of-5 [n]
  (= (mod n 5) 0))

(defn- n-to-str [n]
  (def fizz-str (if (is-multiple-of-3 n) "Fizz" ""))
  (def buzz-str (if (is-multiple-of-5 n) "Buzz" ""))
  (def fizz-buzz-str (str fizz-str buzz-str))
  (def n-str (if (= fizz-buzz-str "") (str n) ""))
  (str fizz-buzz-str n-str))

(defn- fizzbuzz [n]
  (join "\n" (map n-to-str (range 1 (+ n 1)))))

(println (fizzbuzz 100))
```

{% endraw %}

[Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Clojure](https://sampleprograms.io/languages/clojure) was written by:

- Cristiano Lopes

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 04 2020 19:20:07. The solution was first committed on Oct 04 2020 17:31:12. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).