---

title: Sleep Sort in Every Language
layout: default
date: 2019-10-08
last-modified: 2020-05-02
featured-image:
tags: [sleep-sort]
authors:
  - agilob

---

Welcome to the Sleep Sort page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

## Description

Sleep sort is a sorting algorithm that for each input numeric variable it starts a thread 
(or thread like process) that automatically goes to sleep for given number of time units, 
eg. seconds. When a thread complets, it returns the number. When all threads complete, a 
sorted array of numbers is returned.

### Performance

Time complexity of this algorithm strictly depends on value of the highest number, therefore 
it's always O(n), space complexity is dependent on numbers of threads started - O(n) where n 
is number of inputs.


## Requirements

Write a sample program that takes a list of numbers in the format "4, 5, 3, 1, 2".
It should then sort the numbers and output them:

```console
$ ./sleep-sort.lang "4 5 3 1 2"
1, 2, 3, 4, 5
```


## Testing

Every project in the Sample Programs repo should be tested. In this section, we specify the set of tests specific to Sleep Sort. To keep things simple, we split up testing into two subsets: valid and invalid. Valid tests refer to tests that occur under correct input conditions. Invalid tests refer to tests that occur on bad input (e.g., letters instead of numbers).

### Valid Tests

No 'Valid Tests' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

### Invalid Tests

No 'Invalid Tests' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## Articles

- [Sleep Sort in C#](https://sampleprograms.io/projects/sleep-sort/c-sharp)
- [Sleep Sort in Dart](https://sampleprograms.io/projects/sleep-sort/dart)
- [Sleep Sort in Python](https://sampleprograms.io/projects/sleep-sort/python)