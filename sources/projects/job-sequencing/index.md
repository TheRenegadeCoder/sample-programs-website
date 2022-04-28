---

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
$ 50
```

Naturally, this is for testing
purposes as verifying all of the possible sequences would be
challenging.


## Testing

The following table contains various test cases that you can use to
verify the correctness of your solution:

| Description | Input | Output |
|-------------|-------|--------|
| No Input | | "Usage: please provide a list of profits and a list of deadlines" |
| Empty Input | "" | "Usage: please provide a list of profits and a list of deadlines" |
| Missing Input | "25, 15, 10, 5" | "Usage: please provide a list of profits and a list of deadlines" |
|Lists Different Lengths | "1, 2, 3, 4" "1, 2, 3, 4, 5" | "Usage: please provide a list of profits and a list of deadlines" |
| Sample Input | "25, 15, 10, 5" "3, 1, 2, 2" | 50 |
| Sample Input | "20, 15, 10, 5, 1" "2, 2, 1, 3, 3" | 40 |


## Articles

- [Job Sequencing in Go](https://sampleprograms.io/projects/job-sequencing/go)
- [Job Sequencing in Haskell](https://sampleprograms.io/projects/job-sequencing/haskell)
- [Job Sequencing in Java](https://sampleprograms.io/projects/job-sequencing/java)
- [Job Sequencing in Javascript](https://sampleprograms.io/projects/job-sequencing/javascript)
- [Job Sequencing in Kotlin](https://sampleprograms.io/projects/job-sequencing/kotlin)
- [Job Sequencing in Php](https://sampleprograms.io/projects/job-sequencing/php)
- [Job Sequencing in Python](https://sampleprograms.io/projects/job-sequencing/python)