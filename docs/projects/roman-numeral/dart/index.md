---
authors:
- Reilly Howell
date: 2019-10-20
featured-image: roman-numeral-in-every-language.jpg
last-modified: 2019-10-21
layout: default
tags:
- dart
- roman-numeral
title: Roman Numeral in Dart
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/roman-numeral/dart/how-to-implement-the-solution.md
- sources/programs/roman-numeral/dart/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [Dart](https://sampleprograms.io/languages/dart) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```dart
void main(List<String> args) {
  try{
    Map numerals = numeral_map();
    List<int> values = [0];
    for(int i=0; i<args[0].length; i++){
      values.add(numerals[args[0][i]]);
    }

    int sum = values[values.length-1];
    for(int i=1; i<values.length; i++){
      sum = (values[i]>values[i-1]) ? sum-values[i-1] : sum+values[i-1]; 
    }
    print(sum);
  }
  on RangeError{
    print("Usage: please provide a string of roman numerals");
  }
  on NoSuchMethodError{
    print("Error: invalid string of roman numerals");
  }
}

Map numeral_map(){
  var numerals = new Map();
  numerals['I'] = 1;
  numerals['V'] = 5;
  numerals['X'] = 10;
  numerals['L'] = 50;
  numerals['C'] = 100;
  numerals['D'] = 500;
  numerals['M'] = 1000;
  return numerals;
}
```

{% endraw %}

Roman Numeral in [Dart](https://sampleprograms.io/languages/dart) was written by:

- Reilly Howell

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).