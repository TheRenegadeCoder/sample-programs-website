| Description                  | Tree Input                                                                    | Vertex Values     | Target Integer Input |
| ---------------------------- | ----------------------------------------------------------------------------- | ----------------- | -------------------- |
| No Input                     |                                                                               |                   |                      |
| Missing Input: Tree          | `""`                                                                          | `"1, 3, 5, 2, 4"` | `"4"`                |
| Missing Input: Vertex Values | `"0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0"` | `""`              | `"1"`                |
| Missing Input: Target        | `"0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0"` | `"1, 3, 5, 2, 4"` | `""`                 |

All invalid tests should spit out a usage statement in the following
form: 

```
Usage: please provide a tree in an adjacency matrix form ("0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0") together with a list of vertex values ("1, 3, 5, 2, 4") and the integer to find ("4")
```
