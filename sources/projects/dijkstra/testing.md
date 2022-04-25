| Description      | Matrix   | Source      | Destination | Output                                          |
| ---------------- | -------- | ------------| ----------- | ----------------------------------------------- |
| No Input         |          |             |             | "Usage: please provide a comma-separated list of integers" |
| Empty Input      | ""       |      ""       |       ""     |  "Usage: please provide a comma-separated list of integers" |
| Non-Square Input | "1, 0, 3, 0, 5, 1" |      "1"    |  "2"  | "Usage: please provide a comma-separated list of integers" |
| No Destination | "0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0" | "0" | "" | "Usage: please provide a destination" |
| No Source and Destination  | "0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0" | "" | "" | "Usage: please provide source and destination" |
| The Source or The Destination < 0 | "0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0" | "-1" | "2" | "Usage: please provide positive node number" |
| The Source or The Destination < 0 | "0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0" | "-1" | "2" | "Usage: please provide positive node number" |
| Weight < 0                 | "0, 2, 0, -6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, -6, 8, 0, 0, 9, 0, 5, 7, 9, 0" | "1" | "2" | "Usage: please provide positive weights" | 
| The Source or The Destination > SquareRootOfMatrix - 1 | "0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0" | "1" | "10" | "Usage: please provide a node number in the Graph" |
| No way                     | "0, 0, 0, 0" | "0" | "1"   |  "There is no way between {Source} and {Destination}"|
| Proper Input               | "0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0" | "0" | "1" | 2 |
