# Fibonacci in Racket

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.