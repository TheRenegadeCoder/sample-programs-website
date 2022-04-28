# Capitalize in Dart

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Dart
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.