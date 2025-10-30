---
authors:
- Apurva Vats
date: 2025-10-31
featured-image: job-sequencing-in-every-language.jpg
last-modified: 2025-10-31
layout: default
tags:
- c-plus-plus
- job-sequencing
title: Job Sequencing in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/job-sequencing/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/job-sequencing/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Job Sequencing](https://sampleprograms.io/projects/job-sequencing) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

const string usage_msg = "Usage: please provide a list of profits and a list of deadlines\n";
const int MAX_JOBS = 100;

struct Job {
    int profit;
    int deadline;
};

bool compare(const Job &a, const Job &b) {
    return a.profit > b.profit;
}

int jobSequencing(vector<Job> &jobs) {
    sort(jobs.begin(), jobs.end(), compare);

    int maxDeadline = 0;
    for (auto &job : jobs) {
        maxDeadline = max(maxDeadline, job.deadline);
    }

    vector<int> slot(MAX_JOBS, 0);
    int totalProfit = 0;

    for (auto &job : jobs) {
        for (int j = min((int)jobs.size(), job.deadline) - 1; j >= 0; --j) {
            if (slot[j] == 0) {
                slot[j] = 1;
                totalProfit += job.profit;
                break;
            }
        }
    }

    return totalProfit;
}

vector<int> parseInput(const string &input) {
    vector<int> arr;
    stringstream ss(input);
    string token;
    while (getline(ss, token, ',')) {
        token.erase(0, token.find_first_not_of(" \t"));
        token.erase(token.find_last_not_of(" \t") + 1);
        if (!token.empty()) {
            try {
                arr.push_back(stoi(token));
            } catch (...) {
                throw invalid_argument("Invalid input");
            }
        }
    }
    return arr;
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        cout << usage_msg;
        return 1;
    }

    vector<int> profits, deadlines;
    try {
        profits = parseInput(argv[1]);
        deadlines = parseInput(argv[2]);
    } catch (...) {
        cout << usage_msg;
        return 1;
    }

    if (profits.size() != deadlines.size() || profits.empty()) {
        cout << usage_msg;
        return 1;
    }

    vector<Job> jobs;
    for (size_t i = 0; i < profits.size(); ++i) {
        jobs.push_back({profits[i], deadlines[i]});
    }

    int result = jobSequencing(jobs);
    cout << result << endl;

    return 0;
}

```

{% endraw %}

Job Sequencing in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Apurva Vats

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).