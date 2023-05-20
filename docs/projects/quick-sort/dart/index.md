---
title: Quick Sort in Dart
layout: default
date: 2019-10-28
featured-image: quick-sort-in-every-language.jpg
last-modified: 2019-10-28

---

Welcome to the [Quick Sort](https://sampleprograms.io/projects/quick-sort) in [Dart](https://sampleprograms.io/languages/dart) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```dart

import 'dart:io';

/**
 *
 * Merge sort Algorithm from introduction to algorithm
 */

quicksort(List lst,int start,int end){
  if(start < end){

    int mid = partition(lst,start,end);
    //How to use recursive calls
    //Divide and conquer
    quicksort(lst, start, mid-1);
    quicksort(lst, mid, end);
  }
}

partition(List lst,int start,int end){
  //Sort the array accordingly to the pivot_element
  var pivot_element = lst[end];
  var start_position = start -1;
  for (var i = start; i < end; i++){
      if(lst[i] <= pivot_element){
        start_position++;
        swap(lst, start_position, i);
      }
  }
  swap(lst, start_position+1, end);
  return start_position+1;
}

swap(List<int> lst, int position, int position2){
  var tmp = lst[position];
  lst[position] = lst[position2];
  lst[position2] = tmp;
}

List<int>parseInput(List<String> input){
  List<int> lst = [];
  var inputString = input.join().replaceAll(" ", "").replaceAll("'", "").split(",");
  for(var stringNumber in inputString){
    lst.add(int.parse(stringNumber));
  }
  return lst;
}

exitWithError() {
  print(
      'Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"');
  exit(1);
}


main(List<String> args) {

  try {
    List<int> lst = parseInput(args);
    if (lst.length <= 1) exitWithError();
      quicksort(lst, 0, lst.length - 1);
      print(lst.join(", "));
  }catch (e) {
    exitWithError();
  }
}
```

{% endraw %}

[Quick Sort](https://sampleprograms.io/projects/quick-sort) in [Dart](https://sampleprograms.io/languages/dart) was written by:

- Oxymora

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Nov 04 2019 12:06:42. The solution was first committed on Oct 28 2019 14:45:55. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).