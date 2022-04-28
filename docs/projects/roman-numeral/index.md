---

---

Welcome to the Roman Numeral page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

## Description

Roman numerals are the numbers that were used in ancient Rome, which employed
combinations of letters from the Latin alphabet (I, V, X, L, C, D and M).

The following table shows the letter to decimal mapping:

| Letter | Decimal |
| ------ | ------- |
| I      | 1       |
| V      | 5       |
| X      | 10      |
| L      | 50      |
| C      | 100     |
| D      | 500     |
| M      | 1000    |

Stringing together these digits yields a value that is the sum of their
respective mappings. However, there is a catch. Roman numerals must appears in
order of greatest to least. If a smaller value appears before a larger one,
the smaller value is subtracted from the total.

As a result, a string like `XV` would evaluate to 15 while `XIV` would
evaluate to 14.

Of course, there are other limitations, but we'll ignore those for simplicity.


## Requirements

Create a file called Roman Numeral Conversion using whatever naming
convention is appropriate for the choice language.

Using the table above, write a sample program which accepts a Roman numeral on
the command line and outputs its decimal value on standard output. Be careful
to appropriately handle invalid input such as `XT`. More on that in the testing
section.

_Please_ make sure your program is executable. In other words, the solution
should be able to be called in the appropriate environment with a string
of roman numerals (i.e. `./roman-numeral-conversion XXVI`).


## Testing

The following table contains appropriate examples for testing a Roman Numeral
Conversion program:

| Description   | Input | Output                                             |
| ------------- | ----- | -------------------------------------------------- |
| No Input      |       | "Usage: please provide a string of roman numerals" |
| Invalid Input | "XT"  | "Error: invalid string of roman numerals"          |
| Empty Input   | ""    | 0                                                  |
| Single I      | "I"   | 1                                                  |
| Single V      | "V"   | 5                                                  |
| Single X      | "X"   | 10                                                 |
| Single L      | "L"   | 50                                                 |
| Single C      | "C"   | 100                                                |
| Single D      | "D"   | 500                                                |
| Single M      | "M"   | 1000                                               |
| Addition      | "XXV" | 25                                                 |
| Subtraction   | "XIV" | 14                                                 |


## Articles

- [Roman Numeral in C](https://sampleprograms.io/projects/roman-numeral/c)
- [Roman Numeral in C#](https://sampleprograms.io/projects/roman-numeral/c-sharp)
- [Roman Numeral in C++](https://sampleprograms.io/projects/roman-numeral/c-plus-plus)
- [Roman Numeral in Dart](https://sampleprograms.io/projects/roman-numeral/dart)
- [Roman Numeral in Go](https://sampleprograms.io/projects/roman-numeral/go)
- [Roman Numeral in Haskell](https://sampleprograms.io/projects/roman-numeral/haskell)
- [Roman Numeral in Javascript](https://sampleprograms.io/projects/roman-numeral/javascript)
- [Roman Numeral in Lua](https://sampleprograms.io/projects/roman-numeral/lua)
- [Roman Numeral in Php](https://sampleprograms.io/projects/roman-numeral/php)
- [Roman Numeral in Python](https://sampleprograms.io/projects/roman-numeral/python)
- [Roman Numeral in Ruby](https://sampleprograms.io/projects/roman-numeral/ruby)
- [Roman Numeral in Rust](https://sampleprograms.io/projects/roman-numeral/rust)