---
authors:
- gangaasoonu
date: 2025-10-04
featured-image: factorial-in-every-language.jpg
last-modified: 2025-10-04
layout: default
tags:
- dart
- factorial
title: Factorial in Dart
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/dart/how-to-implement-the-solution.md
- sources/programs/factorial/dart/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Dart](https://sampleprograms.io/languages/dart) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```dart
// Issue 4969
void main(List<String> args){
  const String error_message = "Usage: please input a non-negative integer";
  try{

    int factorial = 1;
    int num_needed = int.parse(args[0]);
    if (num_needed.isNegative == true){
      print(error_message);
    }
    else{
      for (int i_index = 1; i_index <= num_needed; i_index ++){
        factorial *= i_index;
      }
      print(factorial.toString());
    }

  }
  catch(e){
    print(error_message);
  }
}

```

{% endraw %}

Factorial in [Dart](https://sampleprograms.io/languages/dart) was written by:

- gangaasoonu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).