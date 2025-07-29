---
authors:
- rzuckerm
date: 2025-07-28
featured-image: convex-hull-in-every-language.jpg
last-modified: 2025-07-28
layout: default
tags:
- convex-hull
- powershell
title: Convex Hull in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/convex-hull/powershell/how-to-implement-the-solution.md
- sources/programs/convex-hull/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Convex Hull](https://sampleprograms.io/projects/convex-hull) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
function Show-Usage() {
    Write-Host 'Usage: please provide at least 3 x and y coordinates as separate lists (e.g. "100, 440, 210")'
    Exit 1
}

function Parse-IntList([string]$Str) {
    @($Str.Split(",") | ForEach-Object { [int]::Parse($_) })
}

class Point {
    [int]$X
    [int]$Y

    Point([int]$x, [int]$y) {
        $this.X = $x
        $this.Y = $y
    }

    [string] ToString() {
        return "($($this.X), $($this.Y))"
    }
}

function Get-Points([int[]]$X, [int[]]$Y) {
    @(0..($X.Length - 1) | ForEach-Object { [Point]::new($X[$_], $Y[$_]) })
}

# Find Convex Hull using Jarvis' algorithm
# Source: https://www.geeksforgeeks.org/convex-hull-using-jarvis-algorithm-or-wrapping/
function Invoke-ConvexHull([Point[]]$Points) {
    $n = $Points.Length

    # The first point is the leftmost point with the highest y-coord in the event of a tie
    $l = Find-LeftmostPoint $Points

    # Repeat until wrapped around to first hull point
    $p = $l
    do {
        # Output convex hull point
        $Points[$p]

        $q = ($p + 1) % $n
        for ($j = 0; $j -lt $n; $j++) {
            # If point j is more counter-clockwise, then update end point (q)
            if ((Get-Orientation $Points[$p] $Points[$j] $Points[$q]) -lt 0) {
                $q = $j
            }
        }

        $p = $q
    } while ($p -ne $l)
}

function Find-LeftmostPoint([Point[]]$Points) {
    $leftmostPoint = [Point]::new([int]::MaxValue, [int]::MinValue)
    $leftmostIndex = 0
    for ($i = 0; $i -lt $Points.Length; $i++) {
        # In the event of a tie, pick the point with the greater y-coord
        if ($Points[$i].X -lt $leftmostPoint.X -or
            ($Points[$i].X -eq $leftmostPoint.X -and $Points[$i].Y -gt $leftmostPoint.Y)
        ) {
            $leftmostPoint = $Points[$i]
            $leftmostIndex = $i
        }
    }

    $leftmostIndex
}

# Get orientation of three points
#
# 0 = points are in a line
# > 0 = points are clockwise
# < 0 = points are counter-clockwise
function Get-Orientation([Point]$P, [Point]$Q, [Point]$R) {
    ($Q.Y - $P.Y) * ($R.X - $Q.X) - ($Q.X - $P.X) * ($R.Y - $Q.Y)
}

if ($args.Length -lt 2 -or -not $args[0] -or -not $args[1]) {
    Show-Usage
}

try {
    $x = Parse-IntList $args[0]
    $y = Parse-IntList $args[1]
    if ($x.Length -ne $y.Length -or $x.Length -lt 3) {
        Show-Usage
    }
} catch {
    Show-Usage
}

# Combine values into set of points
$points = Get-Points $X $Y

# Get convex hull of points and show them
$hullPoints = Invoke-ConvexHull $points
Write-Output ($hullPoints -join "`n")

```

{% endraw %}

Convex Hull in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).