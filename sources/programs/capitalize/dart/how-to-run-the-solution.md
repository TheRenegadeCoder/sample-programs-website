To run the Dart capitalize program, download the dart file from GitHub, install the Dart SDK as described at [dart.dev][2], and run the following from the command line:

```console
dart capitalize.dart "string to be capitalized"
```

Alternatively, you can copy the source code into [DartPad][3], an online Dart interpreter. Just keep in mind that you won't have access to the command line arguments or stdin and stdout using this method so you'll have to populate the args variable in the code instead. For example:

```dart
import 'dart:io';

main(List<String> args) {
  args = ["string to be capitalized"];

  if (args[0].isEmpty) {
    print("Usage: provide a string");
    exit(1);
  }

  print(capitalize(args[0]));
}

String capitalize(String input) =>
    '${input[0].toUpperCase()}${input.substring(1)}';
```
