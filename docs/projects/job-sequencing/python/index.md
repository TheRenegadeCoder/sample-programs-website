---
title: Job Sequencing in Python
layout: default
date: 2018-11-19
featured-image: job-sequencing-in-every-language.jpg
last-modified: 2018-11-19

---

Welcome to the [Job Sequencing](https://sampleprograms.io/projects/job-sequencing) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
import sys


class Job:
    def __init__(self, profit, deadline):
        self.profit = profit
        self.deadline = deadline

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __gt__(self, other):
        return self.profit > other.profit

    def __lt__(self, other):
        return self.profit < other.profit


def input_list(list_str):
    return [int(x.strip(" "), 10) for x in list_str.split(',')]


def max_profit(jobs):
    return sum([j.profit for _, j in iterate_job_sequence(jobs).items()])


def iterate_job_sequence(available, complete=None):
    complete = complete or {}
    if not available:
        return complete
    max_job = max(available)
    available.remove(max_job)
    index_opts = [i for i in range(0, max_job.deadline) if i not in complete]
    new_index = max(index_opts) if index_opts else -1
    if new_index >= 0:
        complete[new_index] = max_job
    return iterate_job_sequence(available, complete)


def exit_with_error():
    print('Usage: please provide a list of profits and a list of deadlines')
    sys.exit(1)


def main(args):
    try:
        profits = input_list(args[0])
        deadlines = input_list(args[1])
        if len(profits) != len(deadlines):
            exit_with_error()

        jobs = [Job(p, d) for p, d in zip(profits, deadlines)]
        print(max_profit(jobs))
    except (IndexError, ValueError):
        exit_with_error()


if __name__ == "__main__":
    main(sys.argv[1:])
```

{% endraw %}

[Job Sequencing](https://sampleprograms.io/projects/job-sequencing) in [Python](https://sampleprograms.io/languages/python) was written by:

- Parker Johansen
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Mar 19 2023 22:13:03. The solution was first committed on Nov 19 2018 14:50:55. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).