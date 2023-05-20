---
title: Depth First Search in Python
layout: default
date: 2021-11-12
featured-image: depth-first-search-in-every-language.jpg
last-modified: 2021-11-12

---

Welcome to the [Depth First Search](https://sampleprograms.io/projects/depth-first-search) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
import sys


def get_input(argv):
    error_message = 'Usage: please provide a tree in an adjacency matrix form ("0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0") together with a list of vertex values ("1, 3, 5, 2, 4") and the integer to find ("4")'

    # check input
    if len(argv) != 3:
        print(error_message)
        sys.exit(1)
    tree, vertex_values, target = argv
    if not tree or not vertex_values or not target:
        print(error_message)
        sys.exit(1)

    # convert strings to lists
    tree = list(map(int, tree.split(', ')))
    vertex_values = list(map(int, vertex_values.split(', ')))
    tree = [tree[i: i + len(vertex_values)] for i in range(0, len(tree), len(vertex_values))]
    target = int(target)

    return tree, vertex_values, target

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.connected = []

def create_tree(tree, vertex_values):
    nodes = {value: TreeNode(value) for value in vertex_values}
    for i, row in enumerate(tree):
        node = nodes[vertex_values[i]]
        for j, is_connected in enumerate(row):
            if j <= i:
                continue
            if is_connected:
                node.connected.append(nodes[vertex_values[j]])
    head = nodes[vertex_values[0]]
    return head

def depth_first_search(node, target):
    if node.val == target:
        return True
    for connected_node in node.connected:
        if depth_first_search(connected_node, target):
            return True
    return False

def main():
    tree, vertex_values, target = get_input(sys.argv[1:])
    tree_head = create_tree(tree, vertex_values)
    if depth_first_search(tree_head, target):
        print('true')
    else:
        print('false')

if __name__ == '__main__':
    main()
```

{% endraw %}

[Depth First Search](https://sampleprograms.io/projects/depth-first-search) in [Python](https://sampleprograms.io/languages/python) was written by:

- Nazar Stepan

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).