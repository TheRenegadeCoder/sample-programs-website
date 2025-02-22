Write a program that accepts two parameters: the mode (encode or decode) and
some text.

If the mode is `decode`, it should print the decoded base64 text.
If the mode is `encode`, it should print the encoded text.
If the mode is neither `encode` nor `decode`, it exit with an error.

```console
$ ./base64.lang "encode" "hello world"
aGVsbG8gd29ybGQ=
$ ./base64.lang "decode" "aGVsbG8gd29ybGQ="
hello world
```
