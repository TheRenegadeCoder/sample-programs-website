---
authors:
- gangaasoonu
date: 2025-10-04
featured-image: longest-word-in-every-language.jpg
last-modified: 2025-10-04
layout: default
tags:
- dart
- longest-word
title: Longest Word in Dart
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/dart/how-to-implement-the-solution.md
- sources/programs/longest-word/dart/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Dart](https://sampleprograms.io/languages/dart) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```dart
//Issue 4972

void main(List<String> argv){
  const String error_message = "Usage: please provide a string";
  if (argv.isEmpty || argv[0].isEmpty){
    print(error_message);
    return;
  }

  String sentence = argv[0];
  String raw = sentence.replaceAll(r'\t', '\t').replaceAll(r'\r', '\r').replaceAll(r'\n', '\n');
  List<String> words = raw.split(RegExp(r'\s+'));
  int max_length= 0;

  for (String each_word in words){
    if (each_word.length > max_length){
      max_length = each_word.length;
    }
  }
  print(max_length);
}

```

{% endraw %}

Longest Word in [Dart](https://sampleprograms.io/languages/dart) was written by:

- gangaasoonu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).