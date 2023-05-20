---
title: Sleep Sort in Every Language
layout: default
date: 2019-10-08
last-modified: 2020-05-02
featured-image: sleep-sort-in-every-language.jpg
tags: [sleep-sort]
authors:
  - agilob

---

Welcome to the Sleep Sort page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

## Description

Sleep sort is a sorting algorithm that for each input numeric variable it starts a thread 
(or thread like process) that automatically goes to sleep for given number of time units, 
eg. seconds. When a thread complets, it returns the number. When all threads complete, a 
sorted array of numbers is returned.

### Performance

Time complexity of this algorithm strictly depends on value of the highest number, therefore 
it's always O(n), space complexity is dependent on numbers of threads started - O(n) where n 
is number of inputs.


## Requirements

Write a sample program that takes a list of numbers in the format "4, 5, 3, 1, 2".
It should then sort the numbers and output them:

```console
$ ./sleep-sort.lang "4, 5, 3, 1, 2"
1, 2, 3, 4, 5
```


## Testing

Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Sleep Sort.
In order to keep things simple, we split up the testing as follows:

- Sleep Sort Valid Tests
- Sleep Sort Invalid Tests

### Sleep Sort Valid Tests

| Description | Input | Output |
| ----------- | ----- | ------ |
| Sample Input | "4, 5, 3, 1, 2" | "1, 2, 3, 4, 5" |
| Sample Input: With Duplicate | "4, 5, 3, 1, 4, 2" | "1, 2, 3, 4, 4, 5" |
| Sample Input: Already Sorted | "1, 2, 3, 4, 5" | "1, 2, 3, 4, 5" |
| Sample Input: Reverse Sorted | "9, 8, 7, 6, 5, 4, 3, 2, 1" | "1, 2, 3, 4, 5, 6, 7, 8, 9" |

### Sleep Sort Invalid Tests

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input | "" |
| Invalid Input: Not A List | "1" |
| Invalid Input: Wrong Format | "4 5 3" |

All of these tests should output the following:

```
Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"
```


## Articles

- [Sleep Sort in Algol68](https://sampleprograms.io/projects/sleep-sort/algol68)
- [Sleep Sort in C#](https://sampleprograms.io/projects/sleep-sort/c-sharp)
- [Sleep Sort in Dart](https://sampleprograms.io/projects/sleep-sort/dart)
- [Sleep Sort in Euphoria](https://sampleprograms.io/projects/sleep-sort/euphoria)
- [Sleep Sort in Go](https://sampleprograms.io/projects/sleep-sort/go)
- [Sleep Sort in Php](https://sampleprograms.io/projects/sleep-sort/php)
- [Sleep Sort in Python](https://sampleprograms.io/projects/sleep-sort/python)
- [Sleep Sort in Rust](https://sampleprograms.io/projects/sleep-sort/rust)

***

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Selection Sort)](https://sampleprograms.io/projects/selection-sort)

</div>

<div id="next" markdown="1">

[Next Project (Transpose Matrix) -->](https://sampleprograms.io/projects/transpose-matrix)

</div>

</nav>