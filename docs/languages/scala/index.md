---
title: The Scala Programming Language
layout: default
last-modified: 2020-05-02
featured-imaged: programming-languages.jpg
tags: [scala]
authors:
  - the_renegade_coder

---

Welcome to the Scala page! Here, you'll find a description of the language as well as a list of sample programs in that language.

## Description

According to [Wikipedia][1], Scala is another general-purpose programming 
language. Likewise, Scala is a multi-paradigm language. However, it 
does have functional capabilities, so I think it fits nicely into our 
recent string of functional languages: Lisp, Scheme, Racket, etc.

Now, Scala is a relatively new language. In fact, it was released in 
2004, almost ten years after the release of Java. I mention Java because 
Scala was actually designed to correct many of Java's problems. For 
instance, here's a list of some of Scala's features: a unified type 
system, syntactic flexibility, functional tendencies, and object-oriented 
extensions.

At this point, I should probably share an example to illustrate some of 
these differences, but I think Wikipedia already shares several excellent 
examples. In addition, I dug up a couple decent blogs comparing the two 
languages:

- [Scala vs. Java: Differences and Similarities][2]
- [Scala vs. Java: Why Should I Learn Scala?][3]

Since Scala has functional tendencies, I figured I'd dig into that a bit 
too. As it turns out, everything in Scala is an expression. And as a result, 
every expression is a function. This means that return statements are not 
required and are actually discouraged:

```scala
val myGrade = if (score >= 70) "Pass" else "Fail"
```

For those familiar with [Java][4], this example probably looks odd. Fortunately, 
the solution is simple. Just evaluate the if-else expression and store the 
expected result in myGrade. If score is 90, then myGrade would store "Pass." 
That's pretty cool stuff!

At any rate, we probably shouldn't dive too much further. After all, we have 
yet to implement Hello World in Scala.

[1]: https://en.wikipedia.org/wiki/Scala_(programming_language)
[2]: https://javarevisited.blogspot.com/2013/11/scala-vs-java-differences-similarities-books.html#axzz7xCsga6Qe
[3]: https://www.toptal.com/scala/why-should-i-learn-scala
[4]: https://en.wikipedia.org/wiki/Java_(programming_language)


## Articles

- [Bubble Sort in Scala](https://sampleprograms.io/projects/bubble-sort/scala)
- [Capitalize in Scala](https://sampleprograms.io/projects/capitalize/scala)
- [Even Odd in Scala](https://sampleprograms.io/projects/even-odd/scala)
- [Factorial in Scala](https://sampleprograms.io/projects/factorial/scala)
- [Fibonacci in Scala](https://sampleprograms.io/projects/fibonacci/scala)
- [File Input Output in Scala](https://sampleprograms.io/projects/file-input-output/scala)
- [Fizz Buzz in Scala](https://sampleprograms.io/projects/fizz-buzz/scala)
- [Hello World in Scala](https://sampleprograms.io/projects/hello-world/scala)
- [Quick Sort in Scala](https://sampleprograms.io/projects/quick-sort/scala)
- [Reverse String in Scala](https://sampleprograms.io/projects/reverse-string/scala)