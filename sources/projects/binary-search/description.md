Binary search is a special type of search function which relies on a few properties
of the search space. First, the search space must have constant time random access
(i.e. an array). In addition, the search space must be sorted by some attribute.
As a consequence, we're able to navigate the search space in O(log(N)) instead of
O(N). 

Jargon aside, binary search works by taking advantage of a sorted collection. As a result,
we don't have to search every element in the collection. Instead, we can try the middle.
If the middle element is greater than the element we want to find, we know that the element
must be "to the left" of that element, assuming the collection is sorted least to greatest. 
From there, we can try the element in the middle of the left half, and so on. 

Eventually, we'll find the element we're looking for, or we'll reach the end of our search.
In either case, we'll only explore O(log(N)) elements. This gives us a dramatic improvement
over linear search.
