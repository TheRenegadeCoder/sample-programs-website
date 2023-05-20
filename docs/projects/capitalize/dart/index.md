---
title: Capitalize in Dart
layout: default
last-modified: 2020-05-02
featured-imaged: capitalize-in-every-language.jpg
tags: [dart, capitalize]
authors:
  - slashdoom

---

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Dart](https://sampleprograms.io/languages/dart) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```dart
import 'dart:io';

main(List<String> args) {

  if (args.isEmpty || args[0].isEmpty) {
    print("Usage: please provide a string");
    exit(1);
  }

  print(capitalize(args[0]));
}

String capitalize(String input) =>
    '${input[0].toUpperCase()}${input.substring(1)}';
```

{% endraw %}

[Capitalize](https://sampleprograms.io/projects/capitalize) in [Dart](https://sampleprograms.io/languages/dart) was written by:

- Jeremy Grifski
- Paddy

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 26 2019 22:15:11. The solution was first committed on Oct 17 2019 23:01:31. As a result, documentation below may be outdated.

## How to Implement the Solution

It's probably worth noting up front that there is a [strings library][1] available that includes a capitalize function with more error checking than we have here.  Since it's not one of the Dart built-in libraries, this would need to be installed with `pub get` or `flutter pub get`.  It would probably be worthwhile in a larger Dart/Flutter project where the package's additional functions may also be useful.

The built-in library that we are going to use, `dart:io`, is imported at the top and will give us access to the stdin and stdout properties and the exit function.

Dart uses the function name `main` as an entry point for the program and since we don't expect any return data from `main` no type has been specified. Within the main function's parameters, you'll see `List<String> args` which will define `args` as a list of strings and fill this list with input from the command line in the form of arguments which in this case are simply strings separated by spaces.

For example:

```
dart capitalize.dart "Hello World"
```

...would fill the args list as `[Hello World]`.

Our first check tests if any data was passed to the script via arguments by checking the isEmpty property of the `args` list. 
- If `args` is empty, we print out an error message and use the `dart:io` `exit()` function to exit out of the script with a proper error code.
- Otherwise, we assume that data was entered as an argument and continue on.

Our next check tests the first string in the args list since this is the only item in the list that we're actually going to process for capitalization.
- If `args[0]` is empty, we print out an error message and use the `dart:io` `exit()` function to exit out of the script with a proper error code.
- Otherwise, we assume we have a good string to process and continue on.

With this check complete we're ready to proceed and capitalize the string input.  Because we want to print out the result we call our `capitalize()` function within the `print()` function.  Within capitalize's parameters we pass the `args[0]` list element that we've tested.

Because our capitalize function is a one line piece of code, we're able to use Dart's shorthand function syntax which uses `"=>"` as a simple way to return the outcome of the one line expression as the value of the function.

Even though the capitalize expression (`'${input[0].toUpperCase()}${input.substring(1)}';`) is a single line, there's quite a bit going on here so let's break it down a bit.

The first concept in use here is string interpolation.  This lets us access the value of a variable or expression inside of a string using `${expression}`.  For example:

```dart
String x = 'hello';
String y = 'world';
print('${x} ${y}!');  // prints "hello world!"
```

Next, Dart lets us access the characters in a string by position (starting at position 0) using the variable name followed by the position enclosed in `[]`.  So `input[0]` gives us the first character of the input string which is what we need to capitalize.  We do this be applying the `toUpperCase` method to that character and return the result with string interpolation as mentioned before.

Now all we need to do is append the remainder of our original string without the first character. We can do this with the `substring` method.

```dart
String substring (int startIndex, [int endIndex])
```

Applying substring with a start index of 1 and no end index returns everything expect for the first character since substring, like the `[]` index, starts with the first character being position 0. By again wrapping this with string interpolation we've now returned the full string with the first character capitalized which will get printed from the `main()` function's `print()` statement. 

[1]: https://api.dart.dev/stable/2.19.6/dart-core/String-class.html


## How to Run the Solution

To run the Dart capitalize program, download the dart file from GitHub, install the Dart SDK as described at [dart.dev][2], and run the following from the command line:

```console
dart capitalize.dart "string to be capitalized"
```

Alternatively, you can copy the source code into [DartPad][3], an online Dart interpreter. Just keep in mind that you won't have access to the command line arguments or stdin and stdout using this method so you'll have to populate the args variable in the code instead. For example:

[2]: https://dart.dev/
[3]: https://dartpad.dev/
