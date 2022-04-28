---

title: The Lisp Programming Language
layout: default
last-modified: 2021-08-12
featured-image: 
tags: [lisp]
authors:
  - the_renegade_coder

---

Welcome to the Lisp page! Here, you'll find a description of the language as well as a list of sample programs in that language.

## Description

According to Wikipedia, Lisp is actually a family of languages. In other 
words, Lisp has many dialects. For the purposes of this exercise, we�ll be 
using Common Lisp.

That said, let�s talk about Lisp in general. As it turns out, Lisp, a language 
developed in 1958, is the second oldest high-level programming language. The 
only older language is Fortran. Since its inception, the language has split 
into several dialects. Perhaps some of the most notable dialects are Scheme, 
Common Lisp, and Clojure.

## Features

Lisp includes several interesting features that are more fun to show rather
than tell. 

### Expressions

In terms of features, Lisp differs wildly from the languages we�ve already covered. 
For example, all data in Lisp is represented with expressions � in particular, symbolic 
expressions. These expressions are written in prefix notation:

```lisp
(+ 3 6 11)
```

In infix notation, the above expression reads:

```lisp
(3 + 6 + 11)
```

So, the expected result is 20.

### Lists

In addition, Lisp is heavily list based. In fact, Lisp is short for List Processor, 
so it should be no surprise that lists play an important role in the language.

Implementing a list in Lisp is rather simple:

```lisp
(list 1 5 2 1)
```

Here. we�ve generated a list of four elements: 1, 5, 2, and 1. In fact, we can even 
nest lists using the prefix notation:

```lisp
(list 1 (list 5 2) 1)
```

The resulting list would look like the following:

```lisp
(1 (5 2) 1)
```

Keep this syntax in mind when we get to functions.

### Lambda Expressions

Have you ever played with lambda expressions in other languages like Java or Python? 
Well, Lisp has them too:

```lisp
(lambda (arg) (* arg 2))
```

In this lambda expression, we simply multiply an argument by 2. If we wanted to use the 
expression, we would have to pass a value to it:

```lisp
((lambda (arg) (* arg 2)) 10)
```

If this is confusing, remember that everything is in prefix notation, so this code might 
look something like the following in a language like Python:

```lisp
foo = lambda n: n * 2
foo(10)
```

Notice, however, that we have a named function in the Python example and an anonymous 
function in the Lisp example. Don�t worry though. Lisp has named functions as well.

### Functions

In Lisp, a named function is essentially a lambda expression that is stored in a symbol:

```lisp
(defun foo (arg) (* arg 2))
```

In this example, we�ve created the exact same lambda expression, but we�ve stored it in 
a function called foo. We can then call foo from anywhere in our program:

```lisp
(foo 10)
```

How cool is that? I think I�m starting to like Lisp. Of course, we haven�t even gotten to 
implement Hello World in Lisp, so we should probably get to that.


## Articles

- [Baklava in Lisp](https://sampleprograms.io/projects/baklava/lisp)
- [Capitalize in Lisp](https://sampleprograms.io/projects/capitalize/lisp)
- [Even Odd in Lisp](https://sampleprograms.io/projects/even-odd/lisp)
- [Factorial in Lisp](https://sampleprograms.io/projects/factorial/lisp)
- [Fibonacci in Lisp](https://sampleprograms.io/projects/fibonacci/lisp)
- [Fizz Buzz in Lisp](https://sampleprograms.io/projects/fizz-buzz/lisp)
- [Hello World in Lisp](https://sampleprograms.io/projects/hello-world/lisp)
- [Prime Number in Lisp](https://sampleprograms.io/projects/prime-number/lisp)
- [Quick Sort in Lisp](https://sampleprograms.io/projects/quick-sort/lisp)
- [Reverse String in Lisp](https://sampleprograms.io/projects/reverse-string/lisp)