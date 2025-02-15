---
authors:
- rzuckerm
date: 2023-02-19
featured-image: depth-first-search-in-every-language.jpg
last-modified: 2023-03-24
layout: default
tags:
- depth-first-search
- euphoria
title: Depth First Search in Euphoria
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/depth-first-search/euphoria/how-to-implement-the-solution.md
- sources/programs/depth-first-search/euphoria/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Depth First Search](https://sampleprograms.io/projects/depth-first-search) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```euphoria
include std/io.e
include std/types.e
include std/text.e
include std/get.e as stdget
include std/sequence.e
include std/utils.e

-- Indices for value() return value
enum VALUE_ERROR_CODE, VALUE_VALUE, VALUE_NUM_CHARS_READ

-- Indices for parse_int() return value
enum PARSE_INT_VALID, PARSE_INT_VALUE

function parse_int(sequence s)
    -- Trim off whitespace and parse string
    s = trim(s)
    sequence result = stdget:value(s,, GET_LONG_ANSWER)

    -- Error if any errors, value is not an integer, or any leftover characters
    boolean valid = (
        result[VALUE_ERROR_CODE] = GET_SUCCESS
        and integer(result[VALUE_VALUE])
        and result[VALUE_NUM_CHARS_READ] = length(s)
    )

    -- Get value if invalid
    integer value = 0
    if valid
    then
        value = result[VALUE_VALUE]
    end if

    return {valid, value}
end function

-- Indices for parse_int_list() return value
enum PARSE_INT_LIST_VALID, PARSE_INT_LIST_VALUES

function parse_int_list(sequence s)
    -- Split string on comma
    sequence list = split(s, ",")

    -- Parse each item
    integer valid = FALSE
    sequence values = {}
    for n = 1 to length(list)
    do
        sequence result = parse_int(list[n])
        valid = result[PARSE_INT_VALID]
        values &= result[PARSE_INT_VALUE]
        if not valid
        then
            exit
        end if
    end for

    return {valid, values}
end function

procedure usage()
    puts(
        STDOUT, 
        (
            "Usage: please provide a tree in an adjacency matrix form "
            & "(\"0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0\") "
            & "together with a list of vertex values (\"1, 3, 5, 2, 4\") "
            & "and the integer to find (\"4\")\n"
        )
    )
    abort(0)
end procedure

-- Indices for node values
enum NODE_VERTEX, NODE_CHILDREN

-- Create tree from adjacency matrix and vertex values.
-- The tree consists of a sequence of nodes.
-- Each node consists of a vertex value and sequence of child indices
function create_tree(sequence adjacency_matrix, sequence vertex_values)
    -- Initialize nodes
    sequence nodes = {}

    -- Get children for this vertex value based on non-zero values of adjacency matrix
    integer num_vertices = length(vertex_values)
    integer num_adjacencies = length(adjacency_matrix)
    integer index = 0
    for row = 1 to num_vertices
    do
        -- Initialize this node with no children
        nodes &= {{vertex_values[row], {}}}

        -- Add child node indices to this node
        integer col = 0
        while col < num_vertices and index < num_adjacencies
        do
            col += 1
            index += 1
            if adjacency_matrix[index] > 0
            then
                nodes[row][NODE_CHILDREN] &= col
            end if
        end while
    end for

    return nodes
end function

-- Indices for depth_first_search_rec return values
enum DFS_VISITED, DFS_FOUND

function depth_first_search(sequence tree, integer target)
    -- Perform depth first recursively starting at root of tree,
    -- indicating no visited nodes and not found
    sequence visited = repeat(FALSE, length(tree))
    sequence dfs_result = depth_first_search_rec(tree, target, 1, {visited, {}})

    -- Indicate where target value is found (if any)
    return dfs_result[DFS_FOUND]
end function

function depth_first_search_rec(sequence tree, integer target, integer node_index, sequence dfs_result)
    -- If invalid node, indicate not found
    if node_index = 0
    then
        return {dfs_result[DFS_VISITED], {}}
    end if

    -- If key of this node matches target, indicate found
    sequence node = tree[node_index]
    if node[NODE_VERTEX] = target
    then
        return {dfs_result[DFS_VISITED], node}
    end if

    -- Indicate this node is visited
    dfs_result[DFS_VISITED][node_index] = TRUE

    -- Perform depth first search on each unvisited child of this node (if any)
    for k = 1 to length(node[NODE_CHILDREN])
    do
        integer child_index = node[NODE_CHILDREN][k]
        if not dfs_result[DFS_VISITED][child_index]
        then
            dfs_result = depth_first_search_rec(tree, target, child_index, dfs_result)
            dfs_result[DFS_VISITED][child_index] = TRUE
            if length(dfs_result[DFS_FOUND]) > 0
            then
                return dfs_result
            end if
        end if
    end for

    return dfs_result
end function

-- Check command-line arguments
sequence argv = command_line()
if (
    length(argv) < 6
    or length(argv[4]) = 0
    or length(argv[5]) = 0
    or length(argv[6]) = 0
)
then
    usage()
end if

-- Parse 1st command-line argument
sequence list_result = parse_int_list(argv[4])
sequence adjacency_matrix = list_result[PARSE_INT_LIST_VALUES]
if not list_result[PARSE_INT_LIST_VALID]
then
    usage()
end if

-- Parse 2nd command-line argument
list_result = parse_int_list(argv[5])
sequence vertex_values = list_result[PARSE_INT_LIST_VALUES]
if not list_result[PARSE_INT_LIST_VALID]
then
    usage()
end if

-- Parse 3rd command-line argument
sequence result = parse_int(argv[6])
integer target = result[PARSE_INT_VALUE]
if not result[PARSE_INT_VALID]
then
    usage()
end if

-- Create tree from adjacency matrix and vertex values
sequence tree = create_tree(adjacency_matrix, vertex_values)

-- Run depth first search and indicate if value is found
sequence node = depth_first_search(tree, target)
puts(STDOUT, iif(length(node) > 0, "true\n", "false\n"))

```

{% endraw %}

Depth First Search in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).