---

---

# Fizz Buzz in Racket

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Racket
;fizzbuzz in racket
;Author: Emblazion

#lang racket
(for ([i (in-range 1 101)])
  (cond
    [(and
      (equal? 0 (modulo i 3))
      (equal? 0 (modulo i 5)))
     (printf "FizzBuzz\n")]
    [(equal? 0 (modulo i 3)) (printf "Fizz\n")]
    [(equal? 0 (modulo i 5)) (printf "Buzz\n")]
    [else (printf "~a\n" i)]))

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.