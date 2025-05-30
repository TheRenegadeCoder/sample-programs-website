---
authors:
- rzuckerm
date: 2023-02-27
featured-image: minimum-spanning-tree-in-every-language.jpg
last-modified: 2023-02-27
layout: default
tags:
- euphoria
- minimum-spanning-tree
title: Minimum Spanning Tree in Euphoria
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/minimum-spanning-tree/euphoria/how-to-implement-the-solution.md
- sources/programs/minimum-spanning-tree/euphoria/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Minimum Spanning Tree](https://sampleprograms.io/projects/minimum-spanning-tree) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```euphoria
include std/io.e
include std/types.e
include std/text.e
include std/get.e as stdget
include std/sequence.e
include std/utils.e
include std/math.e
include std/mathcons.e

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
    puts(STDOUT, "Usage: please provide a comma-separated list of integers\n")
    abort(0)
end procedure

-- Indices for node values
enum NODE_INDEX, NODE_WEIGHT

-- Create graph from weights.
-- The graph consists of a sequence of nodes.
-- Each node consists of a weight and sequence of neighbor indices
function create_graph(sequence weights, integer num_vertices)
    -- Initialize nodes
    sequence nodes = repeat({}, num_vertices)

    -- Get neighbors for this node based on weights
    integer num_weights = length(weights)
    integer index = 0
    for row = 1 to num_vertices
    do
        -- Add neighbor node indices and weights to this node
        for col = 1 to num_vertices
        do
            index += 1
            if weights[index] > 0
            then
                nodes[row] &= {{col, weights[index]}}
            end if
        end for
    end for

    return nodes
end function

-- Indices for Minimum Spanning Tree
enum MST_VERTEX1, MST_VERTEX2, MST_WEIGHT

-- Prim's Minimum Spanning Tree (MST) Algorithm based on C implementation of
-- https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
function prim_mst(sequence graph)
    integer num_vertices = length(graph)

    -- Array to store constructed MST. Indicate no parents yet
    sequence parents = repeat(0, num_vertices)

    -- Key values used to pick minimum weight edge. Initialize to infinity
    sequence keys = repeat(PINF, num_vertices)

    -- Array used to indicate if vertex is in MST. Indicate nothing in MST yet
    sequence mst_set = repeat(FALSE, num_vertices)

    -- Include first vertex in MST
    keys[1] = 1

    -- The MST will include all vertices
    for i = 1 to num_vertices - 1
    do
        -- Pick index of the minimum key value not already in MST
        integer u = find_min_key(keys, mst_set)

        -- Add picked vertex to MST set
        mst_set[u] = TRUE

        -- Update key values and parent indices of picked adjacent
        -- vertices. Only consider vertices not yet in MST
        for j = 1 to length(graph[u])
        do
            integer v = graph[u][j][NODE_INDEX]
            integer graph_value = graph[u][j][NODE_WEIGHT]
            if not mst_set[v] and graph_value < keys[v]
            then
                parents[v] = u
                keys[v] = graph_value
            end if
        end for
    end for

    -- Construct MST information to return
    sequence mst = {}

    -- Skip over root and adjust vertex numbers to account for 1-based indexing
    for k = 2 to num_vertices
    do
        mst &= {{parents[k] - 1, k - 1, keys[k]}}
    end for

    return mst
end function

-- Find vertex with minimum key values not already in MST
function find_min_key(sequence keys, sequence mst_set)
    atom min_value = PINF
    integer min_index
    for v = 1 to length(keys)
    do
        if keys[v] < min_value and not mst_set[v]
        then
            min_value = keys[v]
            min_index = v
        end if
    end for

    return min_index
end function

-- Get total MST weight
function get_total_mst_weight(sequence mst)
    return sum(vslice(mst, MST_WEIGHT))
end function

-- Check command-line arguments
sequence argv = command_line()
if length(argv) < 4 or length(argv[4]) = 0
then
    usage()
end if

-- Parse 1st command-line argument and make sure number of values is a square
sequence list_result = parse_int_list(argv[4])
sequence weights = list_result[PARSE_INT_LIST_VALUES]
integer num_weights = length(weights)
integer sqrt_num_weights = round(sqrt(num_weights))
if (
    not list_result[PARSE_INT_LIST_VALID]
    or num_weights != sqrt_num_weights * sqrt_num_weights
)
then
    usage()
end if

-- Create graph from weights
sequence graph = create_graph(weights, sqrt_num_weights)

-- Get MST using Prim's algorithm
sequence mst = prim_mst(graph)

-- Calculate total weight of MST and display
integer total_weight = get_total_mst_weight(mst)
printf(STDOUT, "%d\n", total_weight)

```

{% endraw %}

Minimum Spanning Tree in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).