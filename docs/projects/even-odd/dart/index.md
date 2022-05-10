---

title: Even Odd in Dart
layout: default
date: 2022-04-28
last-modified: 2022-05-10

---

Welcome to the Even Odd in Dart page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).