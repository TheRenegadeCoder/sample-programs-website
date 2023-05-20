---
title: Job Sequencing in Rust
layout: default
date: 2023-04-15
featured-image: job-sequencing-in-every-language.jpg
last-modified: 2023-04-15

---

Welcome to the [Job Sequencing](https://sampleprograms.io/projects/job-sequencing) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
use std::env::args;
use std::process::exit;
use std::str::FromStr;
use std::cmp::Ordering;

fn usage() -> ! {
    println!("Usage: please provide a list of profits and a list of deadlines");
    exit(0);
}

fn parse_int<T: FromStr>(s: &str) -> Result<T, <T as FromStr>::Err> {
    s.trim().parse::<T>()
}

fn parse_int_list<T: FromStr>(s: &str) -> Result<Vec<T>, <T as FromStr>::Err> {
    s.split(',')
        .map(parse_int)
        .collect::<Result<Vec<T>, <T as FromStr>::Err>>()
}

#[derive(Debug, Ord, Eq)]
struct JobInfo {
    job_id: usize,
    profit: i32,
    deadline: usize,
}

impl JobInfo {
    fn new(job_id: usize, profit: i32, deadline: usize) -> Self {
        Self {job_id: job_id, profit: profit, deadline: deadline}
    }
}

impl PartialOrd for JobInfo {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        // Reverse order of compare so that it is in descending order by profit
        // then deadline
        match self.profit != other.profit {
            true => Some(other.profit.cmp(&self.profit)),
            false => Some(other.deadline.cmp(&self.deadline)),
        }
    }
}

impl PartialEq for JobInfo {
    fn eq(&self, other: &Self) -> bool {
        self.profit == other.profit && self.deadline == other.deadline
    }
}

// Job sequencing with deadlines
// Source: https://www.techiedelight.com/job-sequencing-problem-deadlines/
fn job_sequencing(profits: &Vec<i32>, deadlines: &Vec<i32>) -> Vec<JobInfo> {
    // Set up job details
    let mut jobs: Vec<JobInfo> = profits.iter()
        .zip(deadlines.iter())
        .enumerate()
        .map(|(n, (&p, &d))| JobInfo::new(n + 1, p, d as usize))
        .collect();

    // Get longest deadline
    let longest_deadline: i32 = *deadlines.iter()
        .max()
        .unwrap();

    // Initialize job slots
    let mut slots: Vec<JobInfo> = (0..longest_deadline)
        .map(|_| JobInfo::new(0, 0, 0))
        .collect();

    // Sort jobs by profit then deadline
    jobs.sort();

    // For each job, see if there is available slot at or before the deadline.
    // If so, store this job in that slot
    for job in jobs {
        for j in (0..job.deadline).rev() {
            if slots[j].job_id < 1 {
                slots[j] = job;
                break;
            }
        }
    }

    slots
}

fn get_total_profit(jobs: &Vec<JobInfo>) -> i32 {
    jobs.iter()
        .map(|x| x.profit)
        .sum()
}

fn main() {
    let mut args = args().skip(1);

    // Convert 1st command-line argument to list of integers
    let mut profits: Vec<i32> = args
        .next()
        .and_then(|s| parse_int_list(&s).ok())
        .unwrap_or_else(|| usage());

    // Convert 2nd command-line argument to list of integers
    let mut deadlines: Vec<i32> = args
        .next()
        .and_then(|s| parse_int_list(&s).ok())
        .unwrap_or_else(|| usage());

    // Exit if profits not same length as deadlines
    if profits.len() != deadlines.len() {
        usage();
    }

    // Get job sequence
    let jobs = job_sequencing(&profits, &deadlines);

    // Get total profit and display
    println!("{}", get_total_profit(&jobs));
}
```

{% endraw %}

[Job Sequencing](https://sampleprograms.io/projects/job-sequencing) in [Rust](https://sampleprograms.io/languages/rust) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 08 2023 19:53:07. The solution was first committed on Apr 15 2023 13:21:35. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).