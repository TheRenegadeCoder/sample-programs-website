---
authors:
- rzuckerm
- Sayantan Sarkar
date: 2020-10-07
featured-image: job-sequencing-in-every-language.jpg
last-modified: 2025-05-04
layout: default
tags:
- javascript
- job-sequencing
title: Job Sequencing in Javascript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/job-sequencing/javascript/how-to-implement-the-solution.md
- sources/programs/job-sequencing/javascript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Job Sequencing](https://sampleprograms.io/projects/job-sequencing) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
/**
 * Job Sequencing with deadlines
 */

class Job{
  constructor(profit, deadline){
    this.profit = profit;
    this.deadline = deadline;
  }
}

/* Function to create an array of Job objects */
const createJobs = (array1, array2) => {
  let addedJobs = [];
  for(let index=0; index<array1.length; index++){
    addedJobs.push(new Job(array1[index], array2[index]));
  }
  return addedJobs;
}

/* Sort Jobs based on profit in descending order */
const sortJobs = (jobs) => jobs.sort((a,b) => {
  if(a.profit > b.profit){
    return -1;
  }else if(a.profit > b.profit){
    return 1;
  }else{
    return 0;
  }
});

/* Function to find the maximum deadline to limit the total time slot */
const findMaxDeadline = (jobs) => {
  let maxDeadline = 0;
  for(let index = 0; index<jobs.length; index++){
    maxDeadline = Math.max(jobs[index].deadline, maxDeadline);
  }
  return maxDeadline;
}

/* Function to find the maximum profit */
const findMaxProfit = (jobs, maxDeadline) => {
  let jobSlotsFull = Array(maxDeadline).fill(false);
  let maxProfit = 0;
  let count=0;
  for(let index=0; index < jobs.length; index++){
    if(count === maxDeadline){
      break;
    }
    let deadline = jobs[index].deadline;
    if(deadline > maxDeadline){
      continue;
    }
    for(let slotIndex = deadline-1; slotIndex >= 0; slotIndex--){
      if(jobSlotsFull[slotIndex] === false){
        maxProfit += jobs[index].profit;
        jobSlotsFull[slotIndex] = true;
        count++;
        break;
      }
    }
  }
  return maxProfit;
}

/* Function to split strings into arrays */
const splitString = (str) => str.split(',').map(each => parseInt(each.trim(),10));

/* Function to check the validity of the number arrays */
const checkValidity = (array1, array2) => {
  if(array1.some(isNaN) || 
      array2.some(isNaN) ||
      array1.length != array2.length){
        throw new Error();
    }
}

/* Function to exit in case of invalid input */
const exit = () => {
  const USAGE = "Usage: please provide a list of profits and a list of deadlines";
  console.log(USAGE);
}

/* Main Function */
const main = (string1, string2) => {
  try{
    const array1  = splitString(string1);
    const array2  = splitString(string2);
    checkValidity(array1, array2);
    let jobs = createJobs(array1, array2);
    jobs = sortJobs(jobs);
    let maxDeadline = findMaxDeadline(jobs);
    console.log(findMaxProfit(jobs, maxDeadline));
  }
  catch(err){
    exit();
  }
}

main(process.argv[2], process.argv[3]);

```

{% endraw %}

Job Sequencing in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- rzuckerm
- Sayantan Sarkar

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).