---

title: Bubble Sort in Dart
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Bubble Sort in Dart page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Dart
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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).