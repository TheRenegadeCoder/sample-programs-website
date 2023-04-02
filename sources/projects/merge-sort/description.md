Merge sort is an algorithm that works by dividing a list into smaller lists.
It continues dividing until each list only has a single element in it
because lists of a single element are by definition already sorted.
It then merges each sublist in a sorted fashion until they all become a single sorted list.

Step by step the process is:

1. Divide the sorted list into lists of 1 element.
2. Continually merge the lists together until they become a single list. Do the merge as follows:
    * Compare the smallest items in each of the two lists to be merged.
    * Move the smaller of the two to the new merged list
    * Repeat until there are no unmerged items


### Performance

The performance of sorting algorithms is generally defined in "Big O notation".
If you are not familiar with such notations, please refer to the relevant
article by [Rob Bell][1] or the [Wikipedia][2] entry listed in further readings below.

| Cases        | Big O Notatation |
| ------------ | ---------------- |
| Best case    | O(n log n)       |
| Average case | O(n log n)       |
| Worst case   | O(n log n)       |

### Examples

The examples below were taken from [Wikipedia's article about Merge sort][3].

![Merge sort example image](https://upload.wikimedia.org/wikipedia/commons/e/e6/Merge_sort_algorithm_diagram.svg)

![Merge sort example gif](https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif)

[1]: https://robbell.io/2009/06/a-beginners-guide-to-big-o-notation
[2]: https://en.wikipedia.org/wiki/Big_O_notation
[3]: https://en.wikipedia.org/wiki/Merge_sort
