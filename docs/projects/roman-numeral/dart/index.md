---

title: Roman Numeral in Dart
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Roman Numeral in Dart page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Dart
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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).