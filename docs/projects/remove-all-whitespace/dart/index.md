---
authors:
- gangaasoonu
date: 2025-10-05
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2025-10-05
layout: default
tags:
- dart
- remove-all-whitespace
title: Remove All Whitespace in Dart
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/dart/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/dart/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Dart](https://sampleprograms.io/languages/dart) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```dart
// Issue 4973
void main(List<String> argv){
  const String error_message = "Usage: please provide a string";
  if (argv.isEmpty || argv[0].isEmpty){
    print(error_message);
    return;
  }
  //Do not convert \r, \n and \t explicitly into carriage return, newline and tab, as per Jeremy inputs
  // Use Regular Expressin to replace carriage return, newline and tab with empty string
  String sentence_no_spaces = argv[0].replaceAll(RegExp(r'[\t\r\n ]'), '');
  print(sentence_no_spaces);
}

```

{% endraw %}

Remove All Whitespace in [Dart](https://sampleprograms.io/languages/dart) was written by:

- gangaasoonu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).