---
authors:
- Paddy
date: 2019-10-18
featured-image: bubble-sort-in-every-language.jpg
last-modified: 2019-10-18
layout: default
tags:
- bubble-sort
- dart
title: Bubble Sort in Dart
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/bubble-sort/dart/how-to-implement-the-solution.md
- sources/programs/bubble-sort/dart/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Dart](https://sampleprograms.io/languages/dart) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```dart
import 'dart:io';

main(List<String> args) {
  try {
    List<double> numbersList = parseInput(args.join());
    if (numbersList.length <= 1) exitWithError();
    print(bubbleSort(numbersList));
  } catch (e) {
    exitWithError();
  }
}

String bubbleSort(List<double> numbersList) {
  bool pairSwapped = true;
  int listLength = numbersList.length;

  while (pairSwapped) {
    pairSwapped = false;

    for (int position = 0; position < listLength - 1; position++) {
      if (numbersList[position] > numbersList[position + 1]) {
        numbersList = swapPair(numbersList, position, (position + 1));
        pairSwapped = true;
      }
    }
  }

  return formatOutput(numbersList);
}

List<double> swapPair(
    List<double> numbersList, int currentPosition, int nextPosition) {
  double currentValue = numbersList[currentPosition];

  numbersList[currentPosition] = numbersList[nextPosition];
  numbersList[nextPosition] = currentValue;

  return numbersList;
}

String formatOutput(List<double> numbersList) {
  List<String> output = [];

  numbersList.forEach((number) {
    output.add((number * 10) % 10 != 0 ? "$number" : "${number.toInt()}");
  });

  return output.join(", ");
}

List<double> parseInput(String input) {
  List<double> parsedList = [];

  for (String item in input.replaceAll(" ", "").split(",")) {
    parsedList.add(double.parse(item));
  }

  return parsedList;
}

exitWithError() {
  print(
      'Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"');
  exit(1);
}

```

{% endraw %}

Bubble Sort in [Dart](https://sampleprograms.io/languages/dart) was written by:

- Paddy

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).