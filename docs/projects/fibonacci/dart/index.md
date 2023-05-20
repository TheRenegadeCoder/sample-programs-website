---
title: Fibonacci in Dart
layout: default
date: 2019-10-20
featured-image: fibonacci-in-every-language.jpg
last-modified: 2019-10-20

---

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Dart](https://sampleprograms.io/languages/dart) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```dart
void main(List<String> args) {
  try{
    int first = 0;
    int second = 1;
    int val = 1;
    for(int i=1; i<int.parse(args[0])+1; i++){
      print("${i}: ${val}");
      val = first+second;
      first = second;
      second = val;
    }
  }
  catch(e){
    print("Usage: please input the count of fibonacci numbers to output");
  }
}
```

{% endraw %}

[Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Dart](https://sampleprograms.io/languages/dart) was written by:

- Reilly Howell

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).