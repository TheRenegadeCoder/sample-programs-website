---
authors:
- koishi-dream
date: 2024-09-30
featured-image: depth-first-search-in-every-language.jpg
last-modified: 2024-09-30
layout: default
tags:
- depth-first-search
- java
title: Depth First Search in Java
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/depth-first-search/java/how-to-implement-the-solution.md
- sources/programs/depth-first-search/java/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Depth First Search](https://sampleprograms.io/projects/depth-first-search) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;

public class DepthFirstSearch {

    public static void main(String[] args) {
        if (args.length != 3 || args[0].isEmpty() || args[1].isEmpty() || args[2].isEmpty()) {
            handleError();
            return;
        }
        int matrixSize = args[0].split(",").length;
        if (matrixSize != Math.pow(args[1].split(",").length, 2)){
            handleError();
            return;
        }
        List<Integer> vertices = Stream.of(args[1].split(","))
                .map(String::trim)
                .map(Integer::parseInt)
                .toList();
        int[][] matrix = new int[matrixSize][matrixSize];
        int count = 0;
        for (int i = 0; i < vertices.size(); i++) {
            for (int j = 0; j < vertices.size(); j++) {
                matrix[i][j] = Integer.parseInt(args[0].split(",")[count].trim());
                count++;
            }
        }
        DFSGraph dfsGraph = new DFSGraph(matrix, vertices);
        int search = Integer.parseInt(args[2]);
        System.out.println(dfsGraph.depthFirstSearch(0, 0, search));

    }

    private static void handleError() {
        System.out.println("Usage: please provide a tree in an adjacency matrix form " +
                "(\"0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, " +
                "0\") together with a list of vertex values (\"1, 3, 5, 2, 4\") " +
                "and the integer to find (\"4\")");
    }

    public static class DFSGraph {

        int[][] matrix;
        List<Integer> vertices;
        List<Integer> visited;

        public DFSGraph(int[][] matrix, List<Integer> vertices) {
            this.matrix = matrix;
            this.vertices = vertices;
            this.visited = new ArrayList<>(vertices.size());
        }

        public int getNextNodeIndex(int row, int current_column) {
            for (int i = current_column; i < vertices.size(); i++) {
                if (!visited.contains(vertices.get(i)) && matrix[row][i] == 1) {
                    return i;
                }
            }
            return -1;
        }

        public boolean depthFirstSearch(int row, int column, int search) {
            // if the current node is the search node, return true
            boolean found = this.vertices.get(row) == search;
            if (found) {
                return true;
            }
            // if the current node is the first search node, that is not a valid connection,
            // get the next node of the current row
            if (matrix[row][column] == 0) {
                int nextNodeIndex = getNextNodeIndex(row, column);
                if (nextNodeIndex == -1) {
                    return false;
                } else {
                    column = nextNodeIndex;
                }
            }
            // mark the current node as visited
            visited.add(vertices.get(row));
            while (getNextNodeIndex(row, column) != -1) {
                boolean f = depthFirstSearch(getNextNodeIndex(row, column), row, search);
                if (f) {
                    return true;
                }
                column++;
            }
            return false;
        }

    }
}

```

{% endraw %}

Depth First Search in [Java](https://sampleprograms.io/languages/java) was written by:

- koishi-dream

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).