---

title: Factorial in Racket
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Factorial in Racket page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Racket
#lang racket

;; A naive implementation of factorial

(define (fact n)
  (cond
    [(< n 2)  1]
    [else
     (* (fact (sub1 n)) n)]))
     

  
(define (factorial n)
  (cond
    [(or (not n) (< n 0) ) "Usage: please input a non-negative integer"]
    
    [else
     (println (fact n))]))
            
  
(factorial (string->number (read-line)))
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).