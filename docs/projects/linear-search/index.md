---
title: Linear Search in Every Language
layout: default
date: 2019-10-17
last-modified: 2020-10-15
featured-image: linear-search-in-every-language.jpg
tags: [linear-search]
authors:
  - frankhart2017
  - the_renegade_coder

---

Welcome to the Linear Search page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

## Description

Linear search is quite intuitive, it is basically searching an element in an array by traversing 
the array from the beginning to the end and comparing each item in the array with the key. If a 
particular array entry matches with the key the position is recorded and the loop is stopped. 
The algorithm for this is:

1. Define a flag (set it's value to 0) for checking if key is present in array or notation.
2. Iterate through every element in array.
3. In each iteration compare the key and the current element.
4. If they match set the flag to 1, position to the current iteration and break from the loop.
5. If entire loop is traversed and the element is not found the value of flag will be 0 and user 
can notified that key is not in array.

### Performance

The performance of searching algorithms is generally defined in "Big O notation".
If you are not familiar with such notations, please refer to the relevant
article by [Rob Bell][1] or the [Wikipedia][2] entry listed in further readings below.

| Cases        | Big O Notatation |
| ------------ | ---------------- |
| Best case    | O(1)             |
| Average case | O(n)             |
| Worst case   | O(n)             |

Linear search is not efficient for large arrays, but for relatively smaller arrays it works fine.

### Example: key=3, array=[1, 2, 3, 4, 5]

<b>Iteration 1</b>
<br>array[i] = array[0] = 1
<br>key = 3
<br>key != array[i]

<b>Iteration 2</b>
<br>array[i] = array[1] = 2
<br>key = 3
<br>key != array[i]

<b>Iteration 3</b>
<br>array[i] = array[2] = 3
<br>key = 3
<br>key = array[i]
<br>break
<br>flag = 1
<br>pos = 2

[1]: https://robbell.io/2009/06/a-beginners-guide-to-big-o-notation
[2]: https://en.wikipedia.org/wiki/Big_O_notation


## Requirements

Write a sample program that takes a list of numbers (e.g. "1, 2, 3, 4, 5") and a key (e.g. "3").

```
linear-search.lang "1, 4, 2, 9" "3"
```

In addition, there should be some error handling for situations where the user
doesn't supply correct input.


## Testing

Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Linear Search.
In order to keep things simple, we split up the testing as follows:

- Linear Search Valid Tests
- Linear Search Invalid Tests

### Linear Search Valid Tests

| Description | List Input | Target Integer Input | Output |
| ----------- | ---------- | -------------------- | ------ |
| Sample Input First True | "1, 3, 5, 7" | "1" | "true" |
| Sample Input Last True | "1, 3, 5, 7" | "7" | "true" |
| Sample Input Middle True | "1, 3, 5, 7" | "5" | "true" |
| Sample Input One True | "5" | "5" | "true" |
| Sample Input One False | "5" | "7" | "false" |
| Sample Input Many False | "1, 3, 5, 6" | "7" | "false" |

### Linear Search Invalid Tests

| Description | List Input | Target Integer Input |
| ----------- | ---------- | -------------------- |
| No Input |  |  |
| Missing Input: Target | "1, 2, 3, 4" |  |
| Missing Input: List | "" | "5" |

All of these tests should output the following:

```
Usage: please provide a list of integers ("1, 4, 5, 11, 12") and the integer to find ("11")
```


## Articles

- [Linear Search in Algol68](https://sampleprograms.io/projects/linear-search/algol68)
- [Linear Search in C++](https://sampleprograms.io/projects/linear-search/c-plus-plus)
- [Linear Search in Euphoria](https://sampleprograms.io/projects/linear-search/euphoria)
- [Linear Search in Java](https://sampleprograms.io/projects/linear-search/java)
- [Linear Search in Javascript](https://sampleprograms.io/projects/linear-search/javascript)
- [Linear Search in Mathematica](https://sampleprograms.io/projects/linear-search/mathematica)
- [Linear Search in Php](https://sampleprograms.io/projects/linear-search/php)
- [Linear Search in Python](https://sampleprograms.io/projects/linear-search/python)
- [Linear Search in Rust](https://sampleprograms.io/projects/linear-search/rust)

***

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Josephus Problem)](https://sampleprograms.io/projects/josephus-problem)

</div>

<div id="next" markdown="1">

[Next Project (Longest Common Subsequence) -->](https://sampleprograms.io/projects/longest-common-subsequence)

</div>

</nav>