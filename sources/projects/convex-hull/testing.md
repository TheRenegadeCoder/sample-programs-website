The following table contains various test cases that you can use to
verify the correctness of your solution; please note that different algorithms
could produce the output starting from a different point, and/or in the opposite direction:

| Description           | Input X | Input Y | Output |
|-----------------------|---------|---------|--------|
| X-Ordered triangle    | 100, 180, 240                         | 220, 120, 20                         | (100, 220)<br>(240, 20)<br>(180, 120)                            |
| Pentagon, clockwise   | 100, 140, 320, 480, 280               | 240, 60, 40, 200, 300                | (100, 240)<br>(140, 60)<br>(320, 40)<br>(480, 200)<br>(280, 300) |
| Cluster in center     | 260, 280, 300, 320, 600, 360, 20, 240 | 160, 100, 180, 140, 160, 320, 200, 0 | (20, 200)<br>(240, 0)<br>(600, 160)<br>(360, 320)                |
| Too few values        | 100, 180                              | 240, 60, 40, 200, 300                | Error "Usage: please provide at least 3 x and y coordinates as separate lists (e.g. "100, 440, 210")" reported                          |
| Different cardinality | 100, 180, 240                         | 240, 60, 40, 200, 300                | Error "Usage: please provide at least 3 x and y coordinates as separate lists (e.g. "100, 440, 210")" reported                          |
| Missing y             | 100, 180, 240                         |                                      | Error "Usage: please provide at least 3 x and y coordinates as separate lists (e.g. "100, 440, 210")" reported                          |
| Invalid integer       | 100, 1A0, 240                         | 220, 120, 20                         | Error "Usage: please provide at least 3 x and y coordinates as separate lists (e.g. "100, 440, 210")" reported                          |

