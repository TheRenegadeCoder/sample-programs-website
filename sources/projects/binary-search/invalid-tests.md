| Description           | List Input   | Target Integer Input |
| --------------------- | ------------ | -------------------- |
| No Input              |              |                      |
| Missing Input: List   | `1, 2, 3, 4` |                      |
| Missing Input: Target | `""`         | `5`                  |
| Out of Order Input    | `3, 5, 1, 2` | `3`                  |

All invalid tests should spit out a usage statement in the following
form: 

```
Usage: please provide a list of sorted integers ("1, 4, 5, 11, 12") and the integer to find ("11")
```
