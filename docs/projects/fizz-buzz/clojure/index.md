---

title: Fizz Buzz in Clojure
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Fizz Buzz in Clojure page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Clojure
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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).