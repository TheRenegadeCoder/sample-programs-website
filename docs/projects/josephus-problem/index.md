---
date: 2021-10-08
featured-image: josephus-problem-in-every-language.jpg
last-modified: 2025-10-26
layout: default
tags:
- josephus-problem
title: Josephus Problem
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/projects/josephus-problem/description.md
- sources/projects/josephus-problem/requirements.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the Josephus Problem page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

This article was written by:

- Jeremy Grifski
- rzuckerm

## Description

There are `n` people standing in a circle waiting to be executed. The counting out begins
at some point in the circle and proceeds around the circle in a fixed direction. In each
step, a certain number of people are skipped and the next person is executed. The
elimination proceeds around the circle (which is becoming smaller and smaller as the
executed people are removed), until only the last person remains, who is given freedom.
Given the total number of persons `n` and a number `k` (the step count) which indicates
that `k-1` persons are skipped and `k`th person is killed in circle. The task is to find
out which person will survive.

### Example

In this example, 5 people are placed in a circle (`n = 5`), and the step count is 2 (`k = 2`).

<pre>
      [1]
     /   \
  [5]     [2]
   |       |
  [4]-----[3]
</pre>

The count starts at person 1, and person 2 is executed:

<pre>
      [1]
     /   \
  [5]     <span style="color: red">[2] X</span>
   |       |
  [4]-----[3]
</pre>

The count now starts at person 3, and person 4 is executed:

<pre>
      [1]
     /   \
  [5]     <span style="color: red;">[2] X</span>
   |       |
<span style="color: red;">X [4]</span>-----[3]
</pre>

The count now starts a person 5, and person 1 is executed:

<pre>
      <span style="color: red;">[1] X</span>
     /   \
  [5]     <span style="color: red;">[2] X</span>
   |       |
<span style="color: red;">X [4]</span>-----[3]
</pre>

The count now starts at person 3, and person 5 is executed:

<pre>
      <span style="color: red;">[1] X</span>
     /   \
<span style="color: red;">X [5]</span>     <span style="color: red;">[2] X</span>
   |       |
<span style="color: red;">X [4]</span>-----[3]
</pre>

At the end, person 3 is the survivor.


## Requirements

Create a file called "Josephus problem" using the naming convention appropriate for your language of choice.

Write a sample program which accepts an integer n (total number of people in the circle) and k (k-1 number of people to be skipped to kill next person) and provide the output integer of the last person alive.


## Testing

Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Josephus Problem.
In order to keep things simple, we split up the testing as follows:

- Josephus Problem Valid Tests
- Josephus Problem Invalid Tests

### Josephus Problem Valid Tests

| Description | Input (n) | Input (k) | Output |
| ----------- | --------- | --------- | ------ |
| Sample Input 5, 2 | "5" | "2" | "3" |
| Sample Input 7 3 | "7" | "3" | "4" |
| Sample Input 41 4 | "41" | "4" | "11" |

### Josephus Problem Invalid Tests

| Description | Input |
| ----------- | ----- |
| No Input |  |
| Empty Input | "" |
| Invalid Input: Not A Number | "a" |
| Invalid Input: No K | "1" |

All of these tests should output the following:

```
Usage: please input the total number of people and number of people to skip.
```


## Articles

There are 20 articles:

- [Josephus Problem in Algol68](https://sampleprograms.io/projects/josephus-problem/algol68)
- [Josephus Problem in Awk](https://sampleprograms.io/projects/josephus-problem/awk)
- [Josephus Problem in Beef](https://sampleprograms.io/projects/josephus-problem/beef)
- [Josephus Problem in C](https://sampleprograms.io/projects/josephus-problem/c)
- [Josephus Problem in C#](https://sampleprograms.io/projects/josephus-problem/c-sharp)
- [Josephus Problem in C++](https://sampleprograms.io/projects/josephus-problem/c-plus-plus)
- [Josephus Problem in Commodore Basic](https://sampleprograms.io/projects/josephus-problem/commodore-basic)
- [Josephus Problem in Euphoria](https://sampleprograms.io/projects/josephus-problem/euphoria)
- [Josephus Problem in Go](https://sampleprograms.io/projects/josephus-problem/go)
- [Josephus Problem in Javascript](https://sampleprograms.io/projects/josephus-problem/javascript)
- [Josephus Problem in M4](https://sampleprograms.io/projects/josephus-problem/m4)
- [Josephus Problem in Mathematica](https://sampleprograms.io/projects/josephus-problem/mathematica)
- [Josephus Problem in Pascal](https://sampleprograms.io/projects/josephus-problem/pascal)
- [Josephus Problem in Php](https://sampleprograms.io/projects/josephus-problem/php)
- [Josephus Problem in Powershell](https://sampleprograms.io/projects/josephus-problem/powershell)
- [Josephus Problem in Python](https://sampleprograms.io/projects/josephus-problem/python)
- [Josephus Problem in Ruby](https://sampleprograms.io/projects/josephus-problem/ruby)
- [Josephus Problem in Rust](https://sampleprograms.io/projects/josephus-problem/rust)
- [Josephus Problem in Tcl](https://sampleprograms.io/projects/josephus-problem/tcl)
- [Josephus Problem in Ti Basic](https://sampleprograms.io/projects/josephus-problem/ti-basic)

***

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Job Sequencing)](https://sampleprograms.io/projects/job-sequencing)

</div>

<div id="next" markdown="1">

[Next Project (Linear Search) -->](https://sampleprograms.io/projects/linear-search)

</div>

</nav>