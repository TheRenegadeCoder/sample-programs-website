---
title: Fibonacci in Every Language
layout: default
date: 2018-11-01
last-modified: 2020-05-02
featured-image: fibonacci-in-every-language.jpg
tags: [fibonacci]
authors:

---

Welcome to the Fibonacci page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

## Description

In mathematics, the Fibonacci numbers are the numbers in the following integer
sequence, called the Fibonacci sequence, and characterized by the fact that
every number after the first two is the sum of the two preceding ones:

    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...


## Requirements

For this sample program, each solution should leverage dynamic programming to produce this
list up to the nth term. For instance, `./fib 5` on the command line should output

```
1: 1
2: 1
3: 2
4: 3
5: 5
```

In addition, there should be some error handling for situations where the user
doesn't supply any input or the user supplies input that is not a number
(i.e. `./fib` or `./fib hello`, respectively).


## Testing

Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Fibonacci.
In order to keep things simple, we split up the testing as follows:

- Fibonacci Valid Tests
- Fibonacci Invalid Tests

### Fibonacci Valid Tests

| Description | Input | Output |
| ----------- | ----- | ------ |
| Sample Input 0 | "0" |  |
| Sample Input 1 | "1" | "1: 1" |
| Sample Input 2 | "2" | "1: 1"<br>"2: 1" |
| Sample Input 5 | "5" | "1: 1"<br>"2: 1"<br>"3: 2"<br>"4: 3"<br>"5: 5" |
| Sample Input 10 | "10" | "1: 1"<br>"2: 1"<br>"3: 2"<br>"4: 3"<br>"5: 5"<br>"6: 8"<br>"7: 13"<br>"8: 21"<br>"9: 34"<br>"10: 55" |

### Fibonacci Invalid Tests

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input | "" |
| Invalid Input: Not A Number | "a" |

All of these tests should output the following:

```
Usage: please input the count of fibonacci numbers to output
```


## Articles

- [Fibonacci in Algol68](https://sampleprograms.io/projects/fibonacci/algol68)
- [Fibonacci in Bash](https://sampleprograms.io/projects/fibonacci/bash)
- [Fibonacci in Boo](https://sampleprograms.io/projects/fibonacci/boo)
- [Fibonacci in C](https://sampleprograms.io/projects/fibonacci/c)
- [Fibonacci in C#](https://sampleprograms.io/projects/fibonacci/c-sharp)
- [Fibonacci in C++](https://sampleprograms.io/projects/fibonacci/c-plus-plus)
- [Fibonacci in Dart](https://sampleprograms.io/projects/fibonacci/dart)
- [Fibonacci in Euphoria](https://sampleprograms.io/projects/fibonacci/euphoria)
- [Fibonacci in Go](https://sampleprograms.io/projects/fibonacci/go)
- [Fibonacci in Groovy](https://sampleprograms.io/projects/fibonacci/groovy)
- [Fibonacci in Haskell](https://sampleprograms.io/projects/fibonacci/haskell)
- [Fibonacci in Java](https://sampleprograms.io/projects/fibonacci/java)
- [Fibonacci in Javascript](https://sampleprograms.io/projects/fibonacci/javascript)
- [Fibonacci in Julia](https://sampleprograms.io/projects/fibonacci/julia)
- [Fibonacci in Kotlin](https://sampleprograms.io/projects/fibonacci/kotlin)
- [Fibonacci in Lisp](https://sampleprograms.io/projects/fibonacci/lisp)
- [Fibonacci in Lua](https://sampleprograms.io/projects/fibonacci/lua)
- [Fibonacci in Mathematica](https://sampleprograms.io/projects/fibonacci/mathematica)
- [Fibonacci in Matlab](https://sampleprograms.io/projects/fibonacci/matlab)
- [Fibonacci in Nim](https://sampleprograms.io/projects/fibonacci/nim)
- [Fibonacci in Objective C](https://sampleprograms.io/projects/fibonacci/objective-c)
- [Fibonacci in Pascal](https://sampleprograms.io/projects/fibonacci/pascal)
- [Fibonacci in Perl](https://sampleprograms.io/projects/fibonacci/perl)
- [Fibonacci in Php](https://sampleprograms.io/projects/fibonacci/php)
- [Fibonacci in Python](https://sampleprograms.io/projects/fibonacci/python)
- [Fibonacci in Quack](https://sampleprograms.io/projects/fibonacci/quack)
- [Fibonacci in Racket](https://sampleprograms.io/projects/fibonacci/racket)
- [Fibonacci in Ruby](https://sampleprograms.io/projects/fibonacci/ruby)
- [Fibonacci in Rust](https://sampleprograms.io/projects/fibonacci/rust)
- [Fibonacci in Scala](https://sampleprograms.io/projects/fibonacci/scala)
- [Fibonacci in Swift](https://sampleprograms.io/projects/fibonacci/swift)
- [Fibonacci in Typescript](https://sampleprograms.io/projects/fibonacci/typescript)
- [Fibonacci in Verilog](https://sampleprograms.io/projects/fibonacci/verilog)

***

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Factorial)](https://sampleprograms.io/projects/factorial)

</div>

<div id="next" markdown="1">

[Next Project (File Input Output) -->](https://sampleprograms.io/projects/file-input-output)

</div>

</nav>