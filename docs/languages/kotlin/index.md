---
authors:
- rzuckerm
date: 2018-04-10
featured-image: programming-languages.jpg
last-modified: 2025-03-25
layout: default
tags:
- kotlin
title: The Kotlin Programming Language
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/languages/kotlin/description.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the Kotlin page! Here, you'll find a description of the language as well as a list of sample programs in that language.

This article was written by:

- rzuckerm

## Description

Since Kotlin is a bit more popular than most of the newer languages, it 
actually has a Wikipedia page. So, we'll use that to learn more.

According to [Wikipedia][1], Kotlin is a programming language that runs on 
the [Java Virtual Machine][2]. In other words, Kotlin compiles down to Java 
bytecode. In fact, developers have the option to decide which version 
of Java bytecode they want. In addition to the JVM, Kotlin can also 
compile down to JavaScript.

In terms of features, Kotlin offers an aggressive form of type inference. 
In other words, the language supports static type checking on implicit 
types. Of course, the benefit is a far less verbose syntax than Java.

Of course, I think my favorite feature is extension methods. In Kotlin, 
we can take a class that already exists and tack on our own methods 
without creating an extension class. For instance, Wikipedia shares 
the following snippet:

```kotlin
fun String.lastChar():  Char = this.get(this.length - 1)
```

In this example, the lastChar method is added to the String class. How cool is that?

[1]: https://en.wikipedia.org/wiki/Kotlin_(programming_language)
[2]: https://en.wikipedia.org/wiki/Java_virtual_machine


## Articles

There are 21 articles:

- [Baklava in Kotlin](https://sampleprograms.io/projects/baklava/kotlin)
- [Binary Search in Kotlin](https://sampleprograms.io/projects/binary-search/kotlin)
- [Bubble Sort in Kotlin](https://sampleprograms.io/projects/bubble-sort/kotlin)
- [Capitalize in Kotlin](https://sampleprograms.io/projects/capitalize/kotlin)
- [Even Odd in Kotlin](https://sampleprograms.io/projects/even-odd/kotlin)
- [Factorial in Kotlin](https://sampleprograms.io/projects/factorial/kotlin)
- [Fibonacci in Kotlin](https://sampleprograms.io/projects/fibonacci/kotlin)
- [File Input Output in Kotlin](https://sampleprograms.io/projects/file-input-output/kotlin)
- [Fizz Buzz in Kotlin](https://sampleprograms.io/projects/fizz-buzz/kotlin)
- [Hello World in Kotlin](https://sampleprograms.io/projects/hello-world/kotlin)
- [Job Sequencing in Kotlin](https://sampleprograms.io/projects/job-sequencing/kotlin)
- [Linear Search in Kotlin](https://sampleprograms.io/projects/linear-search/kotlin)
- [Longest Common Subsequence in Kotlin](https://sampleprograms.io/projects/longest-common-subsequence/kotlin)
- [Longest Word in Kotlin](https://sampleprograms.io/projects/longest-word/kotlin)
- [Merge Sort in Kotlin](https://sampleprograms.io/projects/merge-sort/kotlin)
- [Palindromic Number in Kotlin](https://sampleprograms.io/projects/palindromic-number/kotlin)
- [Prime Number in Kotlin](https://sampleprograms.io/projects/prime-number/kotlin)
- [Quick Sort in Kotlin](https://sampleprograms.io/projects/quick-sort/kotlin)
- [Quine in Kotlin](https://sampleprograms.io/projects/quine/kotlin)
- [Reverse String in Kotlin](https://sampleprograms.io/projects/reverse-string/kotlin)
- [Rot13 in Kotlin](https://sampleprograms.io/projects/rot13/kotlin)