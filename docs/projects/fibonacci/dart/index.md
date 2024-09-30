---
authors:
- Reilly Howell
date: 2019-10-20
featured-image: fibonacci-in-every-language.jpg
last-modified: 2019-10-20
layout: default
tags:
- dart
- fibonacci
title: Fibonacci in Dart
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/dart/how-to-implement-the-solution.md
- sources/programs/fibonacci/dart/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Dart](https://sampleprograms.io/languages/dart) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```dart
void main(List<String> args) {
  try{
    int first = 0;
    int second = 1;
    int val = 1;
    for(int i=1; i<int.parse(args[0])+1; i++){
      print("${i}: ${val}");
      val = first+second;
      first = second;
      second = val;
    }
  }
  catch(e){
    print("Usage: please input the count of fibonacci numbers to output");
  }
}


```

{% endraw %}

Fibonacci in [Dart](https://sampleprograms.io/languages/dart) was written by:

- Reilly Howell

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).