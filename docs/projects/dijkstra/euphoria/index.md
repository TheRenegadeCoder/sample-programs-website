---
authors:
- rzuckerm
date: 2023-02-28
featured-image: dijkstra-in-every-language.jpg
last-modified: 2023-02-28
layout: default
tags:
- dijkstra
- euphoria
title: Dijkstra in Euphoria
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/dijkstra/euphoria/how-to-implement-the-solution.md
- sources/programs/dijkstra/euphoria/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Dijkstra](https://sampleprograms.io/projects/dijkstra) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

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
    puts(
        STDOUT, 
        "Usage: please provide three inputs: a serialized matrix, a source node and a destination node\n"
    )
    abort(0)
end procedure

function validate_inputs(sequence weights, integer num_vertices, integer src, integer dest)
    -- Verify number of weights is a square
    integer num_weights = length(weights)
    if num_weights != num_vertices * num_vertices
    then
        return FALSE
    end if

    -- Verify weights greater than equal to zero and any non-zero weights
    if min(weights) < 0 or max(weights) <= 0
    then
        return FALSE
    end if

    -- Verify source and destination are in range
    if src < 0 or src >= num_vertices or dest < 0 or dest >= num_vertices
    then
        return FALSE
    end if

    return TRUE
end function

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

-- Indices for return values from dijkstra()
enum DIJKSTRA_DISTS, DIIJKSTRA_PREVS

-- Dijkstra's algorithm
-- Source: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Pseudocode
function dijkstra(sequence graph, integer src)
    -- Initialize distances to infinite and previous vertices to undefined
    -- Set first vertex distance to 0
    integer num_vertices = length(graph)
    sequence dists = repeat(PINF, num_vertices)
    sequence prevs = repeat(0, num_vertices)
    sequence q = repeat(0, num_vertices)
    for v = 1 to num_vertices
    do
        q[v] = v
    end for

    dists[src + 1] = 0

    -- Initialize unvisited nodes
    integer num_unvisited = num_vertices

    -- While any unvisited nodes
    integer u
    integer v
    integer alt
    while num_unvisited > 0
    do
        -- Pick a vertex u in Q with minimum distance
        u = min_distance(dists, q)

        -- Remove vertex u from Q
        if q[u] > 0
        then
            num_unvisited -= 1
        end if
        q[u] = 0

        -- For each neighbor v of vertex u in still in Q
        for index = 1 to length(graph[u])
        do
            v = graph[u][index][NODE_INDEX]
            if q[v] > 0
            then
                -- Get trial distance
                alt = dists[u] + graph[u][index][NODE_WEIGHT]

                -- If trial distance is smaller than distance v, update distance to v and
                -- previous vertex of v
                if alt < dists[v]
                then
                    dists[v] = alt
                    prevs[v] = u
                end if
            end if
        end for
    end while

    return {dists, prevs}
end function

function min_distance(sequence dists, sequence q)
    atom min_dist = PINF
    integer min_index
    for v = 1 to length(dists)
    do
        if q[v] > 0 and dists[v] < min_dist
        then
            min_dist = dists[v]
            min_index = v
        end if
    end for

    return min_index
end function

-- Check command-line arguments
sequence argv = command_line()
if (
    length(argv) < 4
    or length(argv[4]) = 0
    or length(argv[5]) = 0
    or length(argv[6]) = 0
)
then
    usage()
end if

-- Parse 1st command-line argument
sequence list_result = parse_int_list(argv[4])
sequence weights = list_result[PARSE_INT_LIST_VALUES]
if not list_result[PARSE_INT_LIST_VALID]
then
    usage()
end if

-- Parse 2nd command-line argument
sequence result = parse_int(argv[5])
integer src = result[PARSE_INT_VALUE]
if not result[PARSE_INT_VALID]
then
    usage()
end if

-- Parse 3rd command-line argument
result = parse_int(argv[6])
integer dest = result[PARSE_INT_VALUE]
if not result[PARSE_INT_VALID]
then
    usage()
end if

-- Validate inputs
integer num_weights = length(weights)
integer num_vertices = round(sqrt(num_weights))
if not validate_inputs(weights, num_vertices, src, dest)
then
    usage()
end if

-- Create graph from weights
sequence graph = create_graph(weights, num_vertices)

-- Run Dijkstra's algorithm on graph and show distance to destination
sequence dijkstra_result = dijkstra(graph, src)
integer dist = dijkstra_result[DIJKSTRA_DISTS][dest + 1]
printf(STDOUT, "%d\n", dist)

```

{% endraw %}

Dijkstra in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).