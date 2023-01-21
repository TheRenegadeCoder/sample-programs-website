---

title: Josephus Problem in Every Language

layout: default
date: 2020-10-06
last-modified: 2020-10-06
featured-image: 
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

Some tests for your program are:


| Description | Input (n) | Input (k) | Output |
| :---------- | :---- | :---- | :----- |
| No Input                    |      |      | "Usage: please input the total number of people and number of people to skip." |
| Empty Input                 | ""   | ""   | "Usage: please input the total number of people and number of people to skip." |
| Invalid Input: not a number | word | word | "Usage: please input the total number of people and number of people to skip." |
| Sample Input: 0, 1 (0 people in circle)  | 0  | 1  | "Usage: please input the total number of people and number of people to skip." |
| Sample Input: 5, 2  | 5  | 2  | 3 |
| Sample Input: 7, 3  | 7  | 3  | 4 |
| Sample Input: 41, 4  | 41  | 4  | 11 |


## Articles

- [Josephus Problem in Javascript](https://sampleprograms.io/projects/josephus-problem/javascript)
- [Josephus Problem in Mathematica](https://sampleprograms.io/projects/josephus-problem/mathematica)
- [Josephus Problem in Python](https://sampleprograms.io/projects/josephus-problem/python)

---

<nav class="project-nav">

<div id="prev">

[<-- Previous Project (Job Sequencing)](https://sampleprograms.io/projects/job-sequencing)

</div>

<div id="next">

[Next Project (Linear Search) -->](https://sampleprograms.io/projects/linear-search)

</div>

</nav>