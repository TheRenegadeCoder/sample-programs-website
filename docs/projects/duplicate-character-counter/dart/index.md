---
authors:
- gangaasoonu
date: 2025-10-04
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2025-10-04
layout: default
tags:
- dart
- duplicate-character-counter
title: Duplicate Character Counter in Dart
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/dart/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/dart/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Dart](https://sampleprograms.io/languages/dart) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```dart
//Issue 4974
void main(List<String> args){
  const String error_message = "Usage: please provide a string";
  if (args.isEmpty || args[0].isEmpty){
    print(error_message);
    return;
  } // end of empty check
  
  Map<String, int> frequency = {};
  bool duplicate_not_found = true;

  for (int i = 0; i < args[0].length; i ++){
    String char = args[0][i];
    if (RegExp(r'[a-zA-Z0-9]').hasMatch(char)) {
      frequency[char] = (frequency[char] ?? 0) + 1;
    }
  } // end of checking duplicate characters
  
  //either print all duplicate letters or set flag duplicate letters not found
  frequency.forEach((char, count){
    if (count > 1) {
      duplicate_not_found = false; // at least 1 duplicate letter is found
      print('$char: $count');
    }
  });
  // print if no duplicate characters
  if(duplicate_not_found == true){
      print("No duplicate characters");
  }
}

```

{% endraw %}

Duplicate Character Counter in [Dart](https://sampleprograms.io/languages/dart) was written by:

- gangaasoonu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).