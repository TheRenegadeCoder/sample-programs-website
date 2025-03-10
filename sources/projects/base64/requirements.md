Write a program that accepts two parameters: the mode (encode or decode) and
some text.

- If the mode is `decode`, it should print the decoded base64 text.
- If the mode is `encode`, it should print the encoded text.
- It should print an error message and exit with an error when:
  - The mode is neither `encode` or `decode`.
  - For `decode`, the length of the input string is not a multiple of 4 or contains invalid characters.

```console
$ ./base64.lang "encode" "hello world"
aGVsbG8gd29ybGQ=
$ ./base64.lang "decode" "aGVsbG8gd29ybGQ="
hello world
```

Acceptable language utilities include language features and built-in libraries.
External dependencies are unacceptable. Remember, the goal is to show off
language features and utilities.

In this repository, the algorithm must handle ASCII strings. You don't need to
worry about handling a string in the general case.

The character set you should use is `ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/`.
The padding character should be `=`.
