---
authors:
- awoerner92
- Jeremy Grifski
- Ron Zuckerman
date: 2018-04-08
featured-image: programming-languages.jpg
last-modified: 2024-10-28
layout: default
tags:
- scheme
title: The Scheme Programming Language
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/languages/scheme/description.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the Scheme page! Here, you'll find a description of the language as well as a list of sample programs in that language.

This article was written by:

- awoerner92
- Jeremy Grifski
- Ron Zuckerman

## Description

Once again, I took to [Wikipedia][1] to learn more about the new language.

According to Wikipedia, Scheme is the minimalist branch of Lisp. The only indicator of 
minimalism in Scheme I can find is the fact that it features only 23 s-expressions. 
Unfortunately, I wasn't able to find any additional information on what makes scheme so 
simple. Let me know in the comments.

In terms of features, Scheme leverages lambda calculus, lexical scoping, tail recursion, 
and first-class continuations. To be honest, I had to research [lexical scoping][2]. 
Turns out, lexical scoping is just a fancy name for static scoping. In other words, variables 
only exist within the block of text that they're defined. In contrast, 
[Common Lisp supports both lexical and dynamic scoping][3].

Despite Scheme appearing back in 1970, it's still used today for primarily educational purposes.
For instance, many universities use Scheme in their introductory programming courses. Beyond 
education, Scheme is mainly used by hobbyists for scripting purposes.

[1]: https://en.wikipedia.org/wiki/Scheme_(programming_language)
[2]: https://en.wikipedia.org/wiki/Scope_(computer_science)#Lexical_scoping_and_dynamic_scoping
[3]: https://en.wikipedia.org/wiki/Common_Lisp


## Articles

There are 3 articles:

- [Baklava in Scheme](https://sampleprograms.io/projects/baklava/scheme)
- [Hello World in Scheme](https://sampleprograms.io/projects/hello-world/scheme)
- [Reverse String in Scheme](https://sampleprograms.io/projects/reverse-string/scheme)