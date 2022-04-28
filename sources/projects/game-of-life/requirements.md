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
