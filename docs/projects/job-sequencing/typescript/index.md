---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: job-sequencing-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- job-sequencing
- typescript
title: Job Sequencing in TypeScript
title1: Job Sequencing
title2: in TypeScript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/job-sequencing/typescript/how-to-implement-the-solution.md
- sources/programs/job-sequencing/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Job Sequencing](https://sampleprograms.io/projects/job-sequencing) in [TypeScript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
type Job = { profit: number; deadline: number };

class DSU {
  parent: number[];

  constructor(size: number) {
    this.parent = Array.from({ length: size + 1 }, (_, i) => i);
  }

  find(x: number): number {
    if (this.parent[x] !== x) {
      this.parent[x] = this.find(this.parent[x]);
    }
    return this.parent[x];
  }

  occupy(x: number): void {
    this.parent[x] = this.find(x - 1);
  }
}

function createJobs(profits: number[], deadlines: number[]): Job[] {
  return profits.map((profit, i) => ({ profit, deadline: deadlines[i] }));
}

function sortJobs(jobs: Job[]): Job[] {
  return [...jobs].sort((a, b) => b.profit - a.profit);
}

function findMaxDeadline(jobs: Job[]): number {
  return jobs.reduce((max, j) => Math.max(max, j.deadline), 0);
}

function findMaxProfit(jobs: Job[]): number {
  const maxDeadline = findMaxDeadline(jobs);
  const dsu = new DSU(maxDeadline);

  let profit = 0;

  for (const job of jobs) {
    const availableSlot = dsu.find(Math.min(job.deadline, maxDeadline));

    if (availableSlot > 0) {
      profit += job.profit;
      dsu.occupy(availableSlot);
    }
  }

  return profit;
}

function parseList(input: string): number[] {
  return input
    .split(",")
    .map((s) => Number(s.trim()))
    .filter((n) => !Number.isNaN(n));
}

function validate(profits: number[], deadlines: number[]): void {
  if (profits.length !== deadlines.length || profits.length === 0) {
    throw new Error("Invalid input");
  }
}

function printUsage(): void {
  console.error(
    "Usage: please provide a list of profits and a list of deadlines",
  );
  process.exit(1);
}

function main(): void {
  const [, , profitInput, deadlineInput] = process.argv;

  if (!profitInput || !deadlineInput) {
    printUsage();
  }

  try {
    const profits = parseList(profitInput);
    const deadlines = parseList(deadlineInput);

    validate(profits, deadlines);

    const jobs = sortJobs(createJobs(profits, deadlines));
    console.log(findMaxProfit(jobs));
  } catch {
    printUsage();
  }
}

main();

```

{% endraw %}

Job Sequencing in [TypeScript](https://sampleprograms.io/languages/typescript) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).