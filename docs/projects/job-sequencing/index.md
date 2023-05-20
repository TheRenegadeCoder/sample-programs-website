---
title: Job Sequencing in Every Language
layout: default
date: 2018-11-03
last-modified: 2020-05-02
featured-image: job-sequencing-in-every-language.jpg
tags: [job-sequencing]
authors:
  - the_renegade_coder

---

Welcome to the Job Sequencing page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

## Description

Job sequencing is an optimization problem where the goal is to maximize the
profit earned by completing jobs. In this particular rendition of the problem,
jobs have both a profit and a deadline, and all jobs can be completed in the
same amount of time:

| Job      | J1  | J2  | J3  | J4  |
| -------- | --- | --- | --- | --- |
| Profit   | 25  | 15  | 10  | 5   |
| Deadline | 3   | 1   | 2   | 2   |

In this example, we have four jobs sorted by largest profit first.
Using the greedy method, we can come up with the best sequence by
choosing the job with the current highest profit and scheduling it
at the last possible moment. In this case, we would end up with the
following sequence:

> J2, J3, J1

Because the last possible job we can choose has a deadline of 3, we can
only select 3 jobs at most for our sequence. As a result, we cannot
complete J4. In total, we can make a profit of 50.

Be aware that the output sequence is not unique. There may be multiple
configurations that yield the same profit.


## Requirements

In order to implement this program in your choice language, you should
define the input interface as follows:

```console
$ ./job-sequencing.lang "25, 15, 10, 5" "3, 1, 2, 2"
```

In other words, the input routine should accept a list of profits and
a list of deadlines. It will be up to the program to verify that these
lists are valid.

Once the program has determined a correct sequence, it should
output the maximum profit only. For example:

```console
$ ./job-sequencing.lang "25, 15, 10, 5" "3, 1, 2, 2"
50
```

Naturally, this is for testing
purposes as verifying all of the possible sequences would be
challenging.


## Testing

Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Job Sequencing.
In order to keep things simple, we split up the testing as follows:

- Sequencing Valid Tests
- Sequencing Invalid Tests

### Sequencing Valid Tests

| Description | Profits | Deadlines | Output |
| ----------- | ------- | --------- | ------ |
| Sample Input One | "25, 15, 10, 5" | "3, 1, 2, 2" | "50" |
| Sample Input Two | "20, 15, 10, 5, 1" | "2, 2, 1, 3, 3" | "40" |

### Sequencing Invalid Tests

| Description | Profits | Deadlines |
| ----------- | ------- | --------- |
| No Input |  |  |
| Empty Input | "" |  |
| Missing Input | "25, 15, 10, 5" |  |
| Lists Different Lengths | "1, 2, 3, 4" | "1, 2, 3, 4, 5" |

All of these tests should output the following:

```
Usage: please provide a list of profits and a list of deadlines
```


## Articles

- [Job Sequencing in Algol68](https://sampleprograms.io/projects/job-sequencing/algol68)
- [Job Sequencing in Euphoria](https://sampleprograms.io/projects/job-sequencing/euphoria)
- [Job Sequencing in Go](https://sampleprograms.io/projects/job-sequencing/go)
- [Job Sequencing in Haskell](https://sampleprograms.io/projects/job-sequencing/haskell)
- [Job Sequencing in Java](https://sampleprograms.io/projects/job-sequencing/java)
- [Job Sequencing in Javascript](https://sampleprograms.io/projects/job-sequencing/javascript)
- [Job Sequencing in Kotlin](https://sampleprograms.io/projects/job-sequencing/kotlin)
- [Job Sequencing in Mathematica](https://sampleprograms.io/projects/job-sequencing/mathematica)
- [Job Sequencing in Php](https://sampleprograms.io/projects/job-sequencing/php)
- [Job Sequencing in Python](https://sampleprograms.io/projects/job-sequencing/python)
- [Job Sequencing in Rust](https://sampleprograms.io/projects/job-sequencing/rust)

***

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Insertion Sort)](https://sampleprograms.io/projects/insertion-sort)

</div>

<div id="next" markdown="1">

[Next Project (Josephus Problem) -->](https://sampleprograms.io/projects/josephus-problem)

</div>

</nav>