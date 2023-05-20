---
title: Bubble Sort in Clojure
layout: default
date: 2019-10-02
featured-image: bubble-sort-in-every-language.jpg
last-modified: 2019-10-02

---

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Clojure](https://sampleprograms.io/languages/clojure) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```clojure
(ns bubble-sort
    (:gen-class))
  
(defn- bubble [ys x]
  (if-let [y (peek ys)]
    (if (> y x)
      (conj (pop ys) x y)
      (conj ys x))
    [x]))

(defn bubble-sort [xs]
  (let [ys (reduce bubble [] xs)]
    (if (= xs ys)
      xs
      (recur ys))))

(defn- convert-to-int-array [string]
  (->> (clojure.string/split string #", " )
       (map #(Integer/parseInt %))))

(defn- convert-to-string [int-array]
  (clojure.string/join ", " int-array))

(defn- print-bubble-sort [string]   
  (println 
    (convert-to-string 
      (bubble-sort 
        (convert-to-int-array string)))))

(defn- is-valid-input [args]
  (and 
    (not= (count args) 0) 
    (not= (first args) "")
    (> (count (convert-to-int-array (first args))) 1)
    ))

(defn- print-error []
  (println "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\""))

(defn main [args]
  (try
    (if (is-valid-input args) 
      (print-bubble-sort (first args)) 
      (print-error))
    (catch Exception e (print-error))))

(main *command-line-args*)
```

{% endraw %}

[Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Clojure](https://sampleprograms.io/languages/clojure) was written by:

- Kateryna Tokar
- Tobias Schröder

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 19 2019 23:52:25. The solution was first committed on Oct 02 2019 16:17:26. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).