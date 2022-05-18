| Description           | Input X           | Input Y                   |
| --------------------- | ----------------- | ------------------------- |
| Too few values        | `"100, 180"`      | `"240, 60, 40, 200, 300"` |
| Different cardinality | `"100, 180, 240"` | `"240, 60, 40, 200, 300"` |
| Missing y             | `"100, 180, 240"` |                           |
| Invalid integer       | `"100, 1A0, 240"` | `"220, 120, 20"`          |

All invalid tests should spit out a usage statement in the following form:

```
Usage: please provide at least 3 x and y coordinates as separate lists (e.g. "100, 440, 210")
```
