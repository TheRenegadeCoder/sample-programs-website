---

title: Game Of Life
layout: default
date: 2022-04-28
last-modified: 2022-04-28

---

Welcome to the Game Of Life page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

## Description

For those of you that don't know, the Game of Life is basically a cell
simulation where cells are arranged in an infinite grid. Each cell has one
of two states: alive or dead.

At each turn, all cells are evaluated using the following rules:

- Any live cell with fewer than two live neighbors dies, as if caused by underpopulation.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies, as if by overpopulation.
- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

For more information, check out the [Wikipedia page for Conway's Game of Life][1].


## Requirements

Of course, for the purposes of the repo, here are the requirements for a contribution:

1. Source code must fit in a single file
2. Grid must wrap-around on the edges (think [asteroids][2])
3. The program must support the following command line arguments
    - Grid width (assume square grid)
    - Frame rate (frames/second)
    - Total number of frames
    - Spawn rate (% of living vs. dead as decimal between 0 and 1)
4. Simulation must be a GUI
    - An exception to this rule can be made for languages where it's impossible
      or impractical to have an actual GUI. In that case, a terminal application
      is sufficient.

Beyond that, there's really no hard-and-fast requirements. All I ask is that
solutions are minimal. In other words, don't worry about command line options or
GUI elements. Keep it simple. Remember, the goal is to show off language features.

Also, I ask that you don't use external libraries. I like for these files to
be as easy as possible to test, so limiting dependencies is helpful.


## Testing

Verify that the actual output matches the expected output. See the
[requirements][3] section for an example of the expected output.


## Articles

- [Game Of Life in Bash](https://sampleprograms.io/projects/game-of-life/bash)
- [Game Of Life in C](https://sampleprograms.io/projects/game-of-life/c)
- [Game Of Life in C#](https://sampleprograms.io/projects/game-of-life/c-sharp)
- [Game Of Life in C++](https://sampleprograms.io/projects/game-of-life/c-plus-plus)
- [Game Of Life in Dart](https://sampleprograms.io/projects/game-of-life/dart)
- [Game Of Life in Haskell](https://sampleprograms.io/projects/game-of-life/haskell)
- [Game Of Life in Java](https://sampleprograms.io/projects/game-of-life/java)
- [Game Of Life in Javascript](https://sampleprograms.io/projects/game-of-life/javascript)
- [Game Of Life in Kotlin](https://sampleprograms.io/projects/game-of-life/kotlin)
- [Game Of Life in Php](https://sampleprograms.io/projects/game-of-life/php)
- [Game Of Life in Python](https://sampleprograms.io/projects/game-of-life/python)
- [Game Of Life in Scala](https://sampleprograms.io/projects/game-of-life/scala)
- [Game Of Life in Typescript](https://sampleprograms.io/projects/game-of-life/typescript)