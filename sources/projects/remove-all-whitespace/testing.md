The following table contains various test cases that you can use to verify the correctness of your solution:

| Description                    | Input                          | Output                           |
|--------------------------------|--------------------------------|----------------------------------|
| No Input                       |                                | "Usage: please provide a string" |
| Empty Input                    | ""                             | "Usage: please provide a string" |
| Sample Input: No Spaces        | "RemoveAllWhitespace"          | "RemoveAllWhitespace"            |
| Sample Input: Leading Spaces   | "      RemoveAllWhitespace"    | "RemoveAllWhitespace"            |
| Sample Input: Trailing Spaces  | "RemoveAllWhitespace      "    | "RemoveAllWhitespace"            |
| Sample Input: Inner Spaces     | "Remove    All   Whitespace"   | "RemoveAllWhitespace"            |
| Sample Input: Tabs             | "\tRemove\tAll\tWhitespace\t"  | "RemoveAllWhitespace"            |
| Sample Input: Newlines         | "\nRemove\nAll\nWhitespace\n"  | "RemoveAllWhitespace"            |
| Sample Input: Carriage Returns | "\rRemove\rAll\rWhitespace\r"  | "RemoveAllWhitespace"            |

As always, these tests will be run against any code submitted to the repo via [Glotter][glotter-github].
