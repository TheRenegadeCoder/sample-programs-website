---
title: Reverse String in Dart
layout: default
last-modified: 2020-05-02
featured-imaged: reverse-string-in-every-language.jpg
tags: [dart, reverse-string]
authors:
  - slashdoom

---

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Dart](https://sampleprograms.io/languages/dart) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```dart
// Run using : dart reverse-string.dart hello-world
void main(List<String> args) {
    if ( args.length > 0 ) {
        print( reverse(args[0]) );
    }
}
String reverse(input) {
    return input.split('').reversed.join();
}
```

{% endraw %}

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Dart](https://sampleprograms.io/languages/dart) was written by:

- Bassem Mohamed
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Mar 19 2023 22:24:49. The solution was first committed on Oct 01 2018 05:17:13. As a result, documentation below may be outdated.

## How to Implement the Solution

Much like C or Java, Dart uses the function name `main` as an entry point for the program. In this case, we don't need `main` to return any data so the type `void` is used. Within the `main` function's parameters, you'll see `List<String> args` which will define `args` as a list of strings and fill this list with input from the command line in the form of arguments.

For example:

```
dart reverse-string.dart "Hello World"
```

would fill the args list as `["Hello World"]`.

```
dart reverse-string.dart "Hello" "World"
```

would fill the args list as `["Hello", "World"]`.

It should be noted that in this example program only the first argument passed to the program will be processed because we're only passing the first string in the list to our reverse function's input by adding the index position `[0]` to `args` in the `print( reverse(args[0]) );` line. So, in the second example above, only `Hello` would get reversed.

So let's look at that `reverse` function. We've defined the function with type `String` as it'll return our reversed string to be printed to the console. It takes the parameter `input` as an undefined variable but we're assuming here that it will be a string value.

The `Dart:core` library `String` class contains the `split` method which will split a string or list of strings into a list of substrings based on the pattern given to it. If the pattern is empty as in our reverse function, split will break up the input into single-code unit strings (individual characters). So `"Hello"` with the empty pattern `''` returns `["H", "e", "l", "l", "o"].

After we've broken the string into characters with split, we'll use the `reversed` property from the `Dart:core` library's List class. This property simply takes a list and returns it in reversed order as an Iterable object. So our example list, `["H", "e", "l", "l", "o"]`, becomes `["o", "l", "l", "e", "H"]`.

For the purposes of this sample program, there is very little difference between List and Iterable objects. Both are in fact iterable. At a high level, lists will have additional functionality such as indexed read/write access to its elements and sorting functions. Iterables on the other hand are typically created once then accessed as readonly data during an iteration operation like a for-loop.

Both Iterables and Lists have the `join` method which will take their elements and concatenate them into a string. We use `join` here on the reversed Iterable which is returned as the final string value of our `reverse` function. This value is then printed out to the console from `print` function within `main`.


## How to Run the Solution

To run the Dart string reversal program, download the [dart file from GitHub](https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/d/dart/reverse-string.dart), install the Dart SDK as described at [dart.dev](https://dart.dev/get-dart), and run the following from the command line:

```console
dart reverse-string.dart "Hello, World!"
```

Alternatively, you can copy the source code into [DartPad](https://dartpad.dartlang.org/), an online Dart interpreter. Just keep in mind that you won't have access to the command line arguments input using this method so you'll have to populate the args variable in the code instead. For example:

```dart
void main(List<String> args) {
    args = ['Hello World'];
    print( reverse(args[0]) );
}
String reverse(input) {
    return input.split('').reversed.join();
}
```
