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
