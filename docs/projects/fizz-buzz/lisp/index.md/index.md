# Fizz Buzz in Lisp

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Lisp
(defun divides-by (num divisor)
    (= (mod num divisor) 0))

(dotimes (num 100)
    (write-line
      (cond
        ((and (divides-by (+ num 1) 3) (divides-by (+ num 1) 5)) "FizzBuzz")
        ((divides-by (+ num 1) 3) "Fizz")
        ((divides-by (+ num 1) 5) "Buzz")
        (t (write-to-string (+ num 1))))))
```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.