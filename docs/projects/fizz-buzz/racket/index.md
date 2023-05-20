---
title: Fizz Buzz in Racket
layout: default
date: 2020-10-02
featured-image: fizz-buzz-in-every-language.png
last-modified: 2020-10-02

---

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Racket](https://sampleprograms.io/languages/racket) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```racket
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

{% endraw %}

[Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Racket](https://sampleprograms.io/languages/racket) was written by:

- RubinMathias

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).