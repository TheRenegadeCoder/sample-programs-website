| Description               | List Input   | Target Integer Input | Output  |
|---------------------------|--------------|----------------------|---------|
| No Input                  |              |                      | error\* |
| Missing Input: List       | `1, 2, 3, 4` |                      | error\* |
| Missing Input: Target     | `""`         | `5`                  | error\* |
| Sample Input: First True  | `1, 3, 5, 7` | `1`                  | `true`  |
| Sample Input: Last True   | `1, 3, 5, 7` | `7`                  | `true`  |
| Sample Input: Middle True | `1, 3, 5, 7` | `5`                  | `true`  |
| Sample Input: One True    | `5`          | `5`                  | `true`  |
| Sample Input: One False   | `5`          | `7`                  | `false` |
| Sample Input: Many False  | `1, 3, 5, 6` | `7`                  | `false` |

\*The error string to print: `Usage: please provide a list of integers ("1, 4, 5, 11, 12") and the integer to find ("11")`
