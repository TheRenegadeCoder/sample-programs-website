Write a program that accepts two parameters: the mode (`encode` or `decode`) and
some text.

- If the mode is `decode`, it should print the decoded Base64 text.
- If the mode is `encode`, it should print the encoded text.
- It should print an error message and exit with an error when the input is
  invalid.

```console
$ ./base64-encode-decode.lang "encode" "hello world"
aGVsbG8gd29ybGQ=
$ ./base64-encode-decode.lang "decode" "aGVsbG8gd29ybGQ="
hello world
```

Acceptable language utilities include language features and built-in libraries.
External dependencies are unacceptable. Remember, the goal is to show off
language features and utilities.

In this project, the algorithm must handle ASCII strings. You don't need to
worry about handling a string in the general case.
