---
title: Baklava in F#
layout: default
date: 2019-09-12
featured-image: baklava-in-every-language.jpg
last-modified: 2019-09-12

---

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [F#](https://sampleprograms.io/languages/f-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```f#
let line space asterisk =
    String.replicate space " "  + String.replicate asterisk "*" + "\n"

let rec baklavaShrink =
    List.fold (fun accum n -> accum + (line n (21 - n * 2))) "" [ 1 .. 10 ]

let rec baklavaGrow =
    List.fold (fun accum n -> accum + (line n (21 - n * 2))) "" [ 10 .. -1 .. 0 ]

let baklava =
    baklavaGrow + baklavaShrink

[<EntryPoint>]
let main argv =
    printfn "%s" <| baklava.TrimEnd()
    0
```

{% endraw %}

[Baklava](https://sampleprograms.io/projects/baklava) in [F#](https://sampleprograms.io/languages/f-sharp) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Sep 12 2019 22:00:23. The solution was first committed on Sep 12 2019 21:20:15. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).