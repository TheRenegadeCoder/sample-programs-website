---
authors:
- rzuckerm
date: 2025-07-11
featured-image: depth-first-search-in-every-language.jpg
last-modified: 2025-07-11
layout: default
tags:
- depth-first-search
- powershell
title: Depth First Search in Powershell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/depth-first-search/powershell/how-to-implement-the-solution.md
- sources/programs/depth-first-search/powershell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Depth First Search](https://sampleprograms.io/projects/depth-first-search) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
function Show-Usage() {
    Write-Host 'Usage: please provide a tree in an adjacency matrix form' `
        '("0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0")' `
        'together with a list of vertex values ("1, 3, 5, 2, 4") and the integer to find ("4")'
    Exit 1
}

function Parse-IntList([string]$Str) {
    @($Str.Split(",") | ForEach-Object { [int]::Parse($_) })
}

class Node {
    [int]$Value
    [Node[]]$Children

    Node([int]$value) {
        $this.Value = $value
        $this.Children = @()
    }

    [void] Add([Node]$node) {
        $this.Children += $node
    }
}

class Graph {
    [Node[]]$Nodes

    Graph() {
        $this.Nodes = @()
    }

    [void] Add([Node]$node) {
        $this.Nodes += $node
    }

    [Node] DepthFirstSearch([int]$target) {
        $visited = [Collections.Generic.HashSet[int]]::new()
        return $this.DepthFirstSearch($this.Nodes[0], $target, $visited)
    }

    hidden [Node] DepthFirstSearch([Node]$node, [int]$target, [Collections.Generic.HashSet[int]]$visited) {
        # If invalid node or target value found, return this node
        if (-not $node -or $node.Value -eq $target) {
            return $node
        }

        # Indicate this node is visited
        [void]$visited.Add($node.Value)

        foreach ($child in $node.Children) {
            # If this child not visited,
            if ($child.Value -notin $visited) {
                # Recursively search this child. If target value found, return the found node
                $foundNode = $this.DepthFirstSearch($child, $target, $visited)
                if ($foundNode) {
                    return $foundNode
                }
            }
        }

        return $null
    }
}

function Create-Graph([int[]]$connectionMatrix, [int[]]$vertices) {
    # Populate vertices
    $graph = [Graph]::new()
    foreach ($vertex in $vertices) {
        $graph.Add([Node]::new($vertex))
    }

    # Populate children for each vertex based on connection matrix
    $idx = 0
    $numVertices = $vertices.Length
    for ($row = 0; $row -lt $numVertices; $row++) {
        for ($col = 0; $col -lt $numVertices; $col++) {
            if ($connectionMatrix[$idx++] -gt 0) {
                $graph.Nodes[$row].Add($graph.Nodes[$col])
            }
        }
    }

    $graph
}

if ($args.Length -lt 3 -or -not $args[0] -or -not $args[1]) {
    Show-Usage
}

try {
    $connectionMatrix = Parse-IntList $args[0]
    $vertices = Parse-IntList $args[1]
    $target = [int]::Parse($args[2])
} catch {
    Show-Usage
}

$graph = Create-Graph $connectionMatrix $vertices
$node = $graph.DepthFirstSearch($target)
Write-Output (($node) ? "true" : "false")

```

{% endraw %}

Depth First Search in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).