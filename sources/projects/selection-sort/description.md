Selection sort is an algorithm that operates on two lists, one of sorted elements and one of unsorted.
With each pass, the algorithm finds the smallest item in the unsorted list and moves it
to the front of the sorted list. At the beginning the sorted list is empty, and the algorithm completes
when the unsorted list is empty (meaning that all elements have been moved to the sorted list).

There is also a variant that uses a single list and moves the elements in place. In this variant,
the sorted elements are just placed at the front of the list rather than in a separate list, and
the algorithm starts each pass with the index of the first unsorted element in the list.

### Performance

The performance of sorting algorithms is generally defined in "Big O notation".
If you are not familiar with such notations, please refer to the relevant
article by [Rob Bell][1] or the [Wikipedia][2] entry listed in further readings below.

| Cases        | Big O Notatation |
| ------------ | ---------------- |
| Best case    | O(n<sup>2</sup>) |
| Average case | O(n<sup>2</sup>) |
| Worst case   | O(n<sup>2</sup>) |

Selection sort always performs at O(n<sup>2</sup>). This is because the algorithm's
loops do not depend on the values of the items in the list. That means that even if
the list is already sorted, the full sorting process will still be performed.

### Examples: Two lists

In the examples below, each row is a single pass through all elements in the unsorted list.
The element in __bold__ is the one that will be moved to the sorted list after the pass.

#### "4, 5, 3, 1, 2"

| Sorted List | Unsorted List                 |
|-------------|-------------------------------|
|             |   4     5     3   __1__   2   |
| 1           |   4     5     3   __2__       |
| 1 2         |   4     5   __3__             |
| 1 2 3       | __4__   5                     |
| 1 2 3 4     | __5__                         |
| 1 2 3 4 5   |                               |

#### "3, 5, 4, 1, 2"

| Sorted List | Unsorted List                 |
|-------------|-------------------------------|
|             |   3     5     4   __1__   2   |
| 1           |   3     5     4   __2__       |
| 1 2         | __3__   5     4               |
| 1 2 3       |   5   __4__                   |
| 1 2 3 4     | __5__                         |
| 1 2 3 4 5   |                               |


### Examples: Single list

In the examples below, each row is a single pass through all elements in the unsorted list.
The element in __bold__ is the one that will be moved to the end of the sorted section after the pass.

#### "4, 5, 3, 1, 2"

-   4     5     3   __1__   2   
-   1     4     5     3   __2__ 
-   1     2     4     5   __3__ 
-   1     2     3   __4__   5   
-   1     2     3     4   __5__ 
-   1     2     3     4     5    

#### "3, 5, 4, 1, 2"

-   3     5     4   __1__   2   
-   1     3     5     4   __2__ 
-   1     2   __3__   5     4   
-   1     2     3     5   __4__ 
-   1     2     3     4   __5__ 
-   1     2     3     4     5    

[1]: https://robbell.io/2009/06/a-beginners-guide-to-big-o-notation
[2]: https://en.wikipedia.org/wiki/Big_O_notation
