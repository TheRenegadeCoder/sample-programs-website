---
authors:
- Sanchit Sahay
date: 2020-10-02
featured-image: fizz-buzz-in-every-language.png
last-modified: 2020-10-02
layout: default
tags:
- dart
- fizz-buzz
title: Fizz Buzz in Dart
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/dart/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/dart/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Dart](https://sampleprograms.io/languages/dart) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```dart
void fizzBuzz(int maxNumber){
  for(int i=1;i<=maxNumber;i++){
    String output = "";
    if(i%3 == 0){
      output += "Fizz";
    }
    if(i%5 == 0){
      output += "Buzz";
    }
    if(output == ""){
      output = "$i";
    }
    print(output);
  }
}

void main() {
  fizzBuzz(100);
}

```

{% endraw %}

Fizz Buzz in [Dart](https://sampleprograms.io/languages/dart) was written by:

- Sanchit Sahay

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).