---
title: Josephus Problem in Every Language

layout: default
date: 2020-10-06
last-modified: 2020-10-06
featured-image: josephus-problem-in-every-language.jpg
tags: [josephus-problem]
authors:
 - belide_aakash

---

Welcome to the Josephus Problem page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

## Description

There are n people standing in a circle waiting to be executed. The counting out begins at some point in the circle and proceeds around the circle in a fixed direction. In each step, a certain number of people are skipped and the next person is executed. The elimination proceeds around the circle (which is becoming smaller and smaller as the executed people are removed), until only the last person remains, who is given freedom. Given the total number of persons n and a number k which indicates that k-1 persons are skipped and kth person is killed in circle. The task is to choose the place in the initial circle so that you are the last one remaining and so survive.

### Example

__Input:__

n = 5 (total number of people in circle)

k = 2 (number of people - 1 are skipped and kth person is killed)

__Output__: (Number of people in the circle currently, number of people to skip, index of the person to be killed or removed)

[1, 2, 3, 4, 5] 1 0

[1, 3, 4, 5] 1 1

[1, 3, 5] 1 2

[3, 5] 1 0

3

At the end, 3rd person stays alive.


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

- [Josephus Problem in Algol68](https://sampleprograms.io/projects/josephus-problem/algol68)
- [Josephus Problem in Euphoria](https://sampleprograms.io/projects/josephus-problem/euphoria)
- [Josephus Problem in Javascript](https://sampleprograms.io/projects/josephus-problem/javascript)
- [Josephus Problem in Mathematica](https://sampleprograms.io/projects/josephus-problem/mathematica)
- [Josephus Problem in Php](https://sampleprograms.io/projects/josephus-problem/php)
- [Josephus Problem in Python](https://sampleprograms.io/projects/josephus-problem/python)
- [Josephus Problem in Rust](https://sampleprograms.io/projects/josephus-problem/rust)

***

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Job Sequencing)](https://sampleprograms.io/projects/job-sequencing)

</div>

<div id="next" markdown="1">

[Next Project (Linear Search) -->](https://sampleprograms.io/projects/linear-search)

</div>

</nav>