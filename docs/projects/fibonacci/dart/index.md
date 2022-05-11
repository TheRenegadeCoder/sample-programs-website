---

title: Fibonacci in Dart
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Fibonacci in Dart page! Here, you'll find the source code for this program as well as a description of how the program works.

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

Fibonacci in Dart was written by:

- Reilly Howell

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).