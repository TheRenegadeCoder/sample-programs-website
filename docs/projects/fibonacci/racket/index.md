---

title: Fibonacci in Racket
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Fibonacci in Racket page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Racket
#lang racket

;; A naive iimplementation of fibonacci

(define (fib n)
  (cond
    [(<= n 2)  1]
    [else
     (+ (fib (- n 1)) (fib (- n 2)))]))
     

  
(define (fibonacci n)
  (cond
    [(or (not n) (< n 0) ) "Usage: please input the count of fibonacci numbers to output"]
    
    [else
     (for ([i (in-range 1 (add1 n))]) 
       (println (string-append (number->string i) ": " (number->string (fib i)))))
     ]))
    
  
(fibonacci (string->number (read-line)))
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).