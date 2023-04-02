Insertion sort is an algorithm that generally operates on a single list in place.
It tracks a pointer that iterates through the list a single time, takes each
item and inserts it sorted at the beginning of the list. At any given point
all elements, from the beginning of the list up through the pointer, are in order.
Once the pointer has iterated through the entire list, all elements have been inserted
in order at the front of the list, and the list is now fully sorted.

### Performance

The performance of sorting algorithms is generally defined in "Big O notation".
If you are not familiar with such notations, please refer to the relevant
article by [Rob Bell][1] or the [Wikipedia][2] entry listed in further readings below.

| Cases        | Big O Notatation |
| ------------ | ---------------- |
| Best case    | O(n)             |
| Average case | O(n<sup>2</sup>) |
| Worst case   | O(n<sup>2</sup>) |

Although the main pointer of insertion sort only iterates through the list once
it must also iterate through the existing sorted items at the beginning of the list
every time an element is inserted. Thus the average case is O(n<sup>2</sup>), but so
is the worst case.


### Examples

In the examples below, each row inserts the element from the main pointer 
into the front of the list and moves the main pointer to the next element.
The element in __bold__ is the main pointer.

#### "4, 5, 3, 1, 2"

- __4__   5     3     1     2   
-   4   __5__   3     1     2   
-   4     5   __3__   1     2   
-   3     4     5   __1__   2   
-   1     3     4     5   __2__ 
-   1     2     3     4     5    

#### "3, 5, 4, 1, 2"

- __3__   5     4     1     2   
-   3   __5__   4     1     2   
-   3     5   __4__   1     2   
-   3     4     5   __1__   2   
-   1     3     4     5   __2__ 
-   1     2     3     4     5    

[1]: https://robbell.io/2009/06/a-beginners-guide-to-big-o-notation
[2]: https://en.wikipedia.org/wiki/Big_O_notation
