---
title: Even Odd in Dart
layout: default
date: 2019-10-18
featured-image: even-odd-in-every-language.jpg
last-modified: 2019-10-18

---

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Dart](https://sampleprograms.io/languages/dart) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```dart
void main(List<String> args) {
  try{
    (int.parse(args[0])%2 == 0)?print("Even"):print("Odd");
  }
  catch(e){
    print("Usage: please input a number");
  }
}
```

{% endraw %}

[Even Odd](https://sampleprograms.io/projects/even-odd) in [Dart](https://sampleprograms.io/languages/dart) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).