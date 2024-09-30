---
authors:
- agilob
- Jeremy Grifski
date: 2019-10-07
featured-image: sleep-sort-in-every-language.jpg
last-modified: 2020-10-06
layout: default
tags:
- dart
- sleep-sort
title: Sleep Sort in Dart
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/sleep-sort/dart/how-to-implement-the-solution.md
- sources/programs/sleep-sort/dart/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Sleep Sort](https://sampleprograms.io/projects/sleep-sort) in [Dart](https://sampleprograms.io/languages/dart) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```dart
import 'dart:async';

void main(List<String> args) async {
  
  if (args.length == 0 || args[0].isEmpty || args[0].split(",").length == 1) {
    print('Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"');
  } else {
    List<int> userInput = args[0].split(",").map((str) => int.tryParse(str))
      .takeWhile((test) => test != null)
      .toList();

    List<int> sorted = await sleepsort(userInput);

    print(sorted);
  }
}

Future<List<int>> sleepsort(Iterable<int> input) async {
  List<int> sorted = List();
  await Future.wait(input.map((i) => Future.delayed(Duration(seconds: i), () => sorted.add(i))));
  return Future.value(sorted);
}

```

{% endraw %}

Sleep Sort in [Dart](https://sampleprograms.io/languages/dart) was written by:

- agilob
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).