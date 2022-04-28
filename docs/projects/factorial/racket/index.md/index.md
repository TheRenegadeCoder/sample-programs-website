---

---

Welcome to the Factorial in Racket page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.