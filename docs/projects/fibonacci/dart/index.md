---

title: Fibonacci in Dart
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Fibonacci in Dart page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Dart
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.