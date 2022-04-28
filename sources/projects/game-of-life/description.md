For those of you that don't know, the Game of Life is basically a cell
simulation where cells are arranged in an infinite grid. Each cell has one
of two states: alive or dead.

At each turn, all cells are evaluated using the following rules:

- Any live cell with fewer than two live neighbors dies, as if caused by underpopulation.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies, as if by overpopulation.
- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

For more information, check out the [Wikipedia page for Conway's Game of Life][1].
