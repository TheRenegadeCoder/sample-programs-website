---
authors:
- gangaasoonu
date: 2025-10-04
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2025-10-04
layout: default
tags:
- dart
- palindromic-number
title: Palindromic Number in Dart
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/dart/how-to-implement-the-solution.md
- sources/programs/palindromic-number/dart/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Dart](https://sampleprograms.io/languages/dart) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```dart
//Issue 4971
void main(List<String> args){
  const String error_message= "Usage: please input a non-negative integer";
  if (args.isEmpty){
    print(error_message);
    return;
  }

  try{
    bool is_palindrome = true;
    int num_needed = int.parse(args[0]);

    if (num_needed.isNegative){
      print(error_message);
      return;
    }
 
   String original_string = num_needed.toString();
   String reverse_string = original_string.split('').reversed.join('') ;
   is_palindrome = (original_string == reverse_string);

    print(is_palindrome);
  }
  catch(e){
    print(error_message);
  }
}

```

{% endraw %}

Palindromic Number in [Dart](https://sampleprograms.io/languages/dart) was written by:

- gangaasoonu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).