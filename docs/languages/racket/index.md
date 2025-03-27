---
authors:
- Jeremy Grifski
- Ron Zuckerman
date: 2018-04-08
featured-image: programming-languages.jpg
last-modified: 2024-10-19
layout: default
tags:
- racket
title: The Racket Programming Language
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/languages/racket/description.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the Racket page! Here, you'll find a description of the language as well as a list of sample programs in that language.

This article was written by:

- Jeremy Grifski
- Ron Zuckerman

## Description

Well, at this point, Wikipedia has yet to fail me. As usual, I referenced 
it to learn a little bit more about today's language.

Like [Python][1] and [Java][2], [Racket][3] is a general-purpose programming language. 
Unfortunately, that's sort of where the similarities stop. After all, 
Racket comes from the [Lisp-Scheme family][4], so it resembles a typical 
functional programming language. In other words, expect plenty of parentheses.

What makes Racket different from its [Lisp][5] counterparts is its extensibility. 
In other words, the language can be easily modified using macros. Remember 
when we learned about macros in [Rust][6]? Same idea. We can use these macros to 
control the syntax of Racket.

Macros alone aren't interesting enough to warrant any excitement. However, 
mix macros with a module system, and we get an extremely versatile language. 
These modules allow us to import various macros that can be used to control 
the dialect of Racket. For instance, if we wanted a statically typed version 
of Racket, there's a module for that: typed/racket.

[1]: https://en.wikipedia.org/wiki/Python_(programming_language)
[2]: https://en.wikipedia.org/wiki/Java_(programming_language)
[3]: https://racket-lang.org/
[4]: https://en.wikipedia.org/wiki/List_of_Lisp-family_programming_languages
[5]: https://en.wikipedia.org/wiki/Lisp_(programming_language)
[6]: https://en.wikipedia.org/wiki/Rust_(programming_language)


## Articles

There are 4 articles:

- [Baklava in Racket](https://sampleprograms.io/projects/baklava/racket)
- [Fibonacci in Racket](https://sampleprograms.io/projects/fibonacci/racket)
- [Fizz Buzz in Racket](https://sampleprograms.io/projects/fizz-buzz/racket)
- [Hello World in Racket](https://sampleprograms.io/projects/hello-world/racket)