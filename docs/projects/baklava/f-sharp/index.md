---

title: Baklava in F#
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Baklava in F# page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```F#
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.