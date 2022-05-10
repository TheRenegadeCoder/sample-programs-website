| Description                  | Tree Input                                                                    | Vertex Values     | Target Integer Input | Output  |
| ---------------------------- | ----------------------------------------------------------------------------- | ----------------- | -------------------- | ------- |
| No Input                     |                                                                               |                   |                      | error\* |
| Missing Input: Tree          | `""`                                                                          | `"1, 3, 5, 2, 4"` | `"4"`                | error\* |
| Missing Input: Vertex Values | `"0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0"` | `""`              | `"1"`                | error\* |
| Missing Input: Target        | `"0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0"` | `"1, 3, 5, 2, 4"` | `""`                 | error\* |
| Sample Input: First True     | `"0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0"` | `"1, 3, 5, 2, 4"` | `"1"`                | `true`  |
| Sample Input: Last True      | `"0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0"` | `"1, 3, 5, 2, 4"` | `"4"`                | `true`  |
| Sample Input: Middle True    | `"0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0"` | `"1, 3, 5, 2, 4"` | `"5"`                | `true`  |
| Sample Input: One True       | `"0"`                                                                         | `"1"`             | `"1"`                | `true`  |
| Sample Input: One False      | `"0"`                                                                         | `"1"`             | `"6"`                | `false` |
| Sample Input: Many False     | `"0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0"` | `"1, 3, 5, 2, 4"` | `"7"`                | `false` |

\*The error string to print: `Usage: please provide a tree in an adjacency matrix form ("0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0") together with a list of vertex values ("1, 3, 5, 2, 4") and the integer to find ("4")`
