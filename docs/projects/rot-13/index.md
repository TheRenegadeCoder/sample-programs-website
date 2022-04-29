---

title: Rot 13

---

Welcome to the Rot 13 page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

## Description

ROT-13 is a letter substitution cipher where every letter is replaced by the
letter 13 letters after it alphabetically and wrapping from `Z` to `A` if necessary:

    ABCDEFGHIJKLMNOPQRSTUVWXYZ -> NOPQRSTUVWXYZABCDEFGHIJKLM

As a result, encrypted strings can be decrypted using the same algorithm:

    NOPQRSTUVWXYZABCDEFGHIJKLM -> ABCDEFGHIJKLMNOPQRSTUVWXYZ


## Requirements

Write a sample program that takes a string of text as input.
It should then encrypt the inputted text using ROT-13 and output the result to the console.

```console
$ ./rot-13.lang "the quick brown fox jumped over the lazy dog"
gur dhvpx oebja sbk whzcrq bire gur ynml qbt
```

The solution should handle both lower case and capital letters

```console
$ ./rot-13.lang "THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG"
GUR DHVPX OEBJA SBK WHZCRQ BIRE GUR YNML QBT
```

Any characters/symbols besides a-z and A-Z should be ignored.

```console
$ ./rot-13.lang "The quick brown fox jumped. Was it over the lazy dog?"
Gur dhvpx oebja sbk whzcrq. Jnf vg bire gur ynml qbt?
```

In addition, there should be some error handling for situations where the user
doesn't supply any input.


## Testing

The following table contains various test cases that you can use to
verify the correctness of your solution:

| Description  | Input | Output |
|--------------|-------|--------|
| No Input     | | "Usage: please provide a string to encrypt" |
| Empty Input  | "" | "Usage: please provide a string to encrypt" |
| Sample Input: Lower Case | the quick brown fox jumped over the lazy dog | gur dhvpx oebja sbk whzcrq bire gur ynml qbt |
| Sample Input: Upper Case | THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG | GUR DHVPX OEBJA SBK WHZCRQ BIRE GUR YNML QBT |
| Sample Input: Punctuation | The quick brown fox jumped. Was it over the lazy dog? | Gur dhvpx oebja sbk whzcrq. Jnf vg bire gur ynml qbt? |


## Articles

- [Rot 13 in C](https://sampleprograms.io/projects/rot-13/c)
- [Rot 13 in C#](https://sampleprograms.io/projects/rot-13/c-sharp)
- [Rot 13 in Dart](https://sampleprograms.io/projects/rot-13/dart)
- [Rot 13 in Go](https://sampleprograms.io/projects/rot-13/go)
- [Rot 13 in Haskell](https://sampleprograms.io/projects/rot-13/haskell)
- [Rot 13 in Java](https://sampleprograms.io/projects/rot-13/java)
- [Rot 13 in Javascript](https://sampleprograms.io/projects/rot-13/javascript)
- [Rot 13 in Kotlin](https://sampleprograms.io/projects/rot-13/kotlin)
- [Rot 13 in Lua](https://sampleprograms.io/projects/rot-13/lua)
- [Rot 13 in Perl](https://sampleprograms.io/projects/rot-13/perl)
- [Rot 13 in Php](https://sampleprograms.io/projects/rot-13/php)
- [Rot 13 in Python](https://sampleprograms.io/projects/rot-13/python)
- [Rot 13 in Rust](https://sampleprograms.io/projects/rot-13/rust)