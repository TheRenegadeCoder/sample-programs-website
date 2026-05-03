---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-10
featured-image: dijkstra-in-every-language.jpg
last-modified: 2026-04-10
layout: default
tags:
- dijkstra
- java
title: Dijkstra in Java
title1: Dijkstra
title2: in Java
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/dijkstra/java/how-to-implement-the-solution.md
- sources/programs/dijkstra/java/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Dijkstra](https://sampleprograms.io/projects/dijkstra) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
import java.util.*;
import java.util.regex.Pattern;
import java.util.stream.Stream;

public class Dijkstra {
    private static final int INF = Integer.MAX_VALUE;

    public static void main(String[] args) {
        try {
            if (args.length != 3 || Stream.of(args).anyMatch(String::isBlank)) {
                throw new IllegalArgumentException();
            }

            final int[] weights = parseWeights(args[0]);
            final int size = (int) Math.round(Math.sqrt(weights.length));

            if (size * size != weights.length || size == 0) {
                throw new IllegalArgumentException();
            }

            final int sourceNode = Integer.parseInt(args[1].trim());
            final int targetNode = Integer.parseInt(args[2].trim());

            if (sourceNode < 0 || sourceNode >= size ||
                    targetNode < 0 || targetNode >= size) {
                throw new IllegalArgumentException();
            }

            int result = findShortestPath(weights, size, sourceNode, targetNode);
            System.out.println(result);

        } catch (Exception e) {
            System.err.println(
                    "Usage: please provide three inputs: a serialized matrix, a source node and a destination node"
            );
        }
    }

    private static int[] parseWeights(String input) {
        return Pattern.compile(",")
                .splitAsStream(input)
                .map(String::trim)
                .mapToInt(s -> {
                    int w = Integer.parseInt(s);
                    if (w < 0) throw new IllegalArgumentException();
                    return w;
                })
                .toArray();
    }

    record Node(int id, int cost) implements Comparable<Node> {
        public int compareTo(Node o) {
            return Integer.compare(this.cost, o.cost);
        }
    }

    private static int findShortestPath(int[] matrix, int n, int start, int target) {
        if (start == target) return 0;

        int[] dist = new int[n];
        Arrays.fill(dist, INF);
        dist[start] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(start, 0));

        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            int u = cur.id();

            if (cur.cost() > dist[u]) continue;
            if (u == target) return dist[u];

            for (int v = 0; v < n; v++) {
                int w = matrix[u * n + v];
                if (w <= 0) continue;

                int nd = dist[u] + w;

                if (nd >= dist[v]) continue;

                dist[v] = nd;
                pq.add(new Node(v, nd));
            }
        }

        throw new NoSuchElementException();
    }
}
```

{% endraw %}

Dijkstra in [Java](https://sampleprograms.io/languages/java) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).