For the purposes of this project, we'll assume that the search space is a tree represented 
as an adjacency matrix together with a list of the vertex values in the tree.
Specifically, we'll accept three inputs on the command line: the tree adjacency matrix, the list of vertex
values (as integers) and the vertex value to find:

```console
./depth-first-search.lang "0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0" "2, 3, 6, 77, 44, 46, 1, 321, 5" "5"
```

Here we've chosen to represent the graph as a serialized list of integers. Since
the input string represents a square matrix, we should be able to take the
square root of the length to determine where the rows are in the string. In this
case, we have 81 values, so we must have 9 nodes.
If we reformat the input string as a matrix, we'll notice that the values in the
matrix represent the edges between vertices. Taking the vertex values into account as well, the resulting matrix
could look something like the following:

| Mapping | 2   | 3   | 6   | 77  | 44  | 46  | 1   | 321 | 5   |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2       | 0   | 1   | 1   | 1   | 0   | 0   | 0   | 0   | 0   |
| 3       | 1   | 0   | 0   | 0   | 1   | 1   | 0   | 0   | 0   |
| 6       | 1   | 0   | 0   | 0   | 0   | 0   | 1   | 1   | 0   |
| 77      | 1   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 1   |
| 44      | 0   | 1   | 0   | 0   | 0   | 0   | 0   | 0   | 0   |
| 46      | 0   | 1   | 0   | 0   | 0   | 0   | 0   | 0   | 0   |
| 1       | 0   | 0   | 1   | 0   | 0   | 0   | 0   | 0   | 0   |
| 321     | 0   | 0   | 1   | 0   | 0   | 0   | 0   | 0   | 0   |
| 5       | 0   | 0   | 0   | 1   | 0   | 0   | 0   | 0   | 0   |

This matrix will result in a tree that looks like this:

```console
            2
         /  |   \
       3    6    77
    /  |   / \     \
  44  46  1  321    5
```

If successful, the script should return `true`. Otherwise, the script should return `false`. 
If any user input errors occur, the script should output the following usage message:
`Usage: please provide a tree in an adjacency matrix form ("0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0") together with a list of vertex values ("1, 3, 5, 2, 4") and the integer to find ("4")`.
