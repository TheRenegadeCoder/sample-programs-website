| Description                                            | Matrix                                                                          | Source | Destination |
| ------------------------------------------------------ | ------------------------------------------------------------------------------- | ------ | ----------- |
| No Input                                               |                                                                                 |        |             |
| Empty Input                                            | `""`                                                                            | `""`   | `""`        |
| Non-Square Input                                       | `"1, 0, 3, 0, 5, 1"`                                                            | `"1"`  | `"2"`       |
| No Destination                                         | `"0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0"`   | `"0"`  | `""`        |
| No Source and Destination                              | `"0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0"`   | `""`   | `""`        |
| The Source or The Destination < 0                      | `"0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0"`   | `"-1"` | `"2"`       |
| The Source or The Destination < 0                      | `"0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0"`   | `"-1"` | `"2"`       |
| Weight < 0                                             | `"0, 2, 0, -6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, -6, 8, 0, 0, 9, 0, 5, 7, 9, 0"` | `"1"`  | `"2"`       |
| The Source or The Destination > SquareRootOfMatrix - 1 | `"0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0"`   | `"1"`  | `"10"`      |
| No way                                                 | `"0, 0, 0, 0"`                                                                  | `"0"`  | `"1"`       |

All invalid tests should spit out a usage statement in the following form: 

```
Usage: please provide three inputs: a serialized matrix, a source node and a destination node
```
