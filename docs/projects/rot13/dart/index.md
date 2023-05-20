---
title: Rot13 in Dart
layout: default
date: 2019-10-18
featured-image: rot13-in-every-language.jpg
last-modified: 2019-10-18

---

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [Dart](https://sampleprograms.io/languages/dart) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```dart
import 'dart:io';

main(List<String> args) {
  if (args.isEmpty || args[0].isEmpty) {
    print("Usage: please provide a string to encrypt");
    exit(1);
  } else {
    print( rot13(args[0]) );
  }
}

String rot13(String input) {
  int aLower = "a".codeUnitAt(0);
  int aUpper = "A".codeUnitAt(0);
  int nLower = "n".codeUnitAt(0);
  int nUpper = "N".codeUnitAt(0);
  int zLower = "z".codeUnitAt(0);
  int zUpper = "Z".codeUnitAt(0);

  List<String> coded = [];

  input.codeUnits.forEach((char) {
    if ((char >= aLower && char < nLower) ||
        (char >= aUpper && char < nUpper)) {
      coded.add(new String.fromCharCode(char + 13));
    } else if ((char >= nLower && char <= zLower) ||
        (char >= nUpper && char <= zUpper)) {
      coded.add(new String.fromCharCode(char - 13));
    } else {
      coded.add(new String.fromCharCode(char));
    }
  });

  return coded.join();
}
```

{% endraw %}

[Rot13](https://sampleprograms.io/projects/rot13) in [Dart](https://sampleprograms.io/languages/dart) was written by:

- slashdoom

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 18 2019 09:04:37. The solution was first committed on Oct 18 2019 08:52:24. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).