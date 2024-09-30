---
authors:
- Jeremy Grifski
- zafar hussain
date: 2019-10-31
featured-image: fibonacci-in-every-language.jpg
last-modified: 2022-05-10
layout: default
tags:
- fibonacci
- racket
title: Fibonacci in Racket
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/racket/how-to-implement-the-solution.md
- sources/programs/fibonacci/racket/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Racket](https://sampleprograms.io/languages/racket) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```racket
#lang racket

;; A naive iimplementation of fibonacci

(define (fib n)
  (cond
    [(<= n 2)  1]
    [else
     (+ (fib (- n 1)) (fib (- n 2)))]))
     

  
(define (fibonacci n)
  (cond
    [(or (not n) (< n 0)) (display "Usage: please input the count of fibonacci numbers to output")]
    
    [else
     (for ([i (in-range 1 (add1 n))]) 
       (displayln (string-append (number->string i) ": " (number->string (fib i)))))
     ]))
    
  
(fibonacci 
  (string->number 
    (cond
      [(vector-empty? (current-command-line-arguments)) ""] 
      [else (vector-ref (current-command-line-arguments) 0)]
    )
  )
)

```

{% endraw %}

Fibonacci in [Racket](https://sampleprograms.io/languages/racket) was written by:

- Jeremy Grifski
- zafar hussain

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).