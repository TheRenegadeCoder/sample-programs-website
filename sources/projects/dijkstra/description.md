Dijkstra's algorithm (or Dijkstra's Shortest Path First algorithm, SPF algorithm) is an algorithm for finding the shortest paths between nodes in a graph, which may represent, for example, road networks. It was conceived by computer scientist Edsger W. Dijkstra in 1956 and published three years later.

Dijkstra’s algorithm doesn’t work for graphs with negative weight edges.

Below are the detailed steps used in Dijkstra’s algorithm to find the shortest path from a single source vertex to all other vertices in the given graph.
Algorithm
1) Create a set sptSet (shortest path tree set) that keeps track of vertices included in shortest path tree, i.e., whose minimum distance from source is calculated and finalized. Initially, this set is empty.
2) Assign a distance value to all vertices in the input graph. Initialize all distance values as INFINITE. Assign distance value as 0 for the source vertex so that it is picked first.
3) While sptSet doesn’t include all vertices

    a) Pick a vertex u which is not there in sptSet and has minimum distance value.
  
    b) Include u to sptSet.
  
    c) Update distance value of all adjacent vertices of u. To update the distance values, iterate through all adjacent vertices. For every           adjacent vertex v, if sum of distance value of u (from source) and weight of edge u-v, is less than the distance value of v, then update the  distance value of v.
    
Time Complexity is O(V^2).

Memory Complexity is O(V^2).

## Example

Dijkstra's algorithm to find the shortest path between a and b. It picks the unvisited vertex with the low distance, calculates the distance through it to each unvisited neighbor, and updates the neighbor's distance if smaller. Mark visited (set to red) when done with neighbors.

![Dijkstra_Animation](https://user-images.githubusercontent.com/35429211/67672949-a2dcfd80-f981-11e9-862a-96bd0ec9ba83.gif)
