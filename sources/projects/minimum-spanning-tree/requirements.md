To implement this algorithm, your program should accept a square matrix of
strings in the following format:

```console
./minimum-spanning-tree "0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0"
```

Here we've chosen to represent the matrix as a serialized list of integers. Since
the input string represents a square matrix, we should be able to take the
square root of the length to determine where the rows are in the string. In this
case, we have 25 values, so we must have 5 nodes.

If we reformat the input string as a matrix, we'll notice that the values in the
matrix represent the edge weight between each node. For example, we
could reformat our example to look something like the following:

| Mapping | 0   | 1   | 2   | 3   | 4   |
| ------- | --- | --- | --- | --- | --- |
| 0       | 0   | 2   | 0   | 6   | 0   |
| 1       | 2   | 0   | 3   | 8   | 5   |
| 2       | 0   | 3   | 0   | 0   | 7   |
| 3       | 6   | 8   | 0   | 0   | 9   |
| 4       | 0   | 5   | 7   | 9   | 0   |

Here, we can see that there is no edge between node 0 and node 2. Meanwhile,
node 0 has an edge to node 3 with a weight of 6.

If we continue to look at this table, we'll notice that all the edges are mirrored
across the top to bottom diagonal. In other words, the weight from node 0 to node
1 is the same as the weight from node 1 to node 0. We can use this property to
differentiate between directed and undirected graphs.

For simplicity, the output sequence should print the minimum weight of the tree.
In other words, what is the cost of the minimum spanning tree?
