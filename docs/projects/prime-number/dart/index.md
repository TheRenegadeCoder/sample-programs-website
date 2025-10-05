---
authors:
- gangaasoonu
date: 2025-10-05
featured-image: prime-number-in-every-language.jpg
last-modified: 2025-10-05
layout: default
tags:
- dart
- prime-number
title: Prime Number in Dart
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/dart/how-to-implement-the-solution.md
- sources/programs/prime-number/dart/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Dart](https://sampleprograms.io/languages/dart) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```dart
// Issue 4970
import 'dart:math';
void main(List<String> args){
  const String error_message= "Usage: please input a non-negative integer";
  if (args.isEmpty){
    print(error_message);
    return;
  }
  try{
    int num_needed = int.parse(args[0]);
    if (num_needed.isNegative){
      print(error_message);
      return;
    }

    // If the number is even number other than 2 OR if number is either 0 or 1, Print Composite
    if( (num_needed == 0)|| (num_needed == 1) || (num_needed %2 ==0 && num_needed != 2) ){
      print("Composite");
      return;
    }
    bool is_prime = true;    
    int max_divisor = sqrt(num_needed).toInt();
    for (int i_index = 3; i_index <= max_divisor; i_index +=2){
      if(num_needed % i_index == 0){
        is_prime = false;
        break;
      }
    }

    print(is_prime ? "Prime" : "Composite");
  }
  catch(e){
    print(error_message);
  }
}

```

{% endraw %}

Prime Number in [Dart](https://sampleprograms.io/languages/dart) was written by:

- gangaasoonu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).