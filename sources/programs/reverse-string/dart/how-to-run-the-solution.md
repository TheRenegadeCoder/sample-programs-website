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
