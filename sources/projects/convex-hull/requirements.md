Write a program that receives two command line arguments: strings in the form `x1, x2, x3 ...` and
`y1, y2, y3 ...` respectively, where `(xi, yi)` are the coordinates of the i-th point of the set.

Your program should be able to parse these lists into some internal representation in your choice
language (ideally an array). From there, the program should compute the convex hull of the set of points,
and output a list in the form

    (x1, y1)
    (x2, y2)
    ...

where `(xj, yj)` are the coordinates of the j-th vertex of the convex hull.

There are many algorithms to solve this problem. You may implement any of them.
Check this [great document by Jeff Erickson][2] for more details about the
problem and the different algorithms to solve it.

[2]: https://jeffe.cs.illinois.edu/pubs/pdf/convex.pdf
