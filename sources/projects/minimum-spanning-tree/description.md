A minimum spanning tree is defined as the minimum set of edges needed to connect
every node in a graph without cycles. For our purposes, we're concerned with
weighted undirected graphs. In other words, we want to find the minimum cost
spanning tree.

For example, let's say we have the following graph:

TODO: insert graph image

Then, a possible minimum spanning tree would have the lowest total weight
while also connected all nodes without cycles. Such as:

TODO: insert graph image

Naturally, there are a few ways to solve this problem, but the two most famous
are Prim's algorithm and Kruskal's algorithm. Check those out before implementing
this solution.
