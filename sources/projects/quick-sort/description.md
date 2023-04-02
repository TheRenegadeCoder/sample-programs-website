Quick sort is an algorithm that works by dividing a list into smaller lists.
It recursively partially sorts and divides each sublist into further lists until it
reaches the base case of a list that is either empty or contains only a single element, because
those cases are by definition already sorted. After that it concatenates all of the sublists
together into a single sorted list.

Step by step the process is:

1. Pick an element. This element is called the pivot.
2. Move all elements in the list that are greater than the pivot after the pivot
3. Move all elements that are less than the pivot before the pivot.
4. Recursively repeat steps 1-4 until a list of size 0-1 is found.
5. Concatinate all the sublists into a single sorted list.

### Performance

The performance of sorting algorithms is generally defined in "Big O notation".
If you are not familiar with such notations, please refer to the relevant
article by [Rob Bell][1] or the [Wikipedia][2] entry listed in further readings below.

| Cases        | Big O Notatation |
| ------------ | ---------------- |
| Best case    | O(n log n)       |
| Average case | O(n log n)       |
| Worst case   | O(n<sup>2</sup>) |

As the name implies, quicksort is a rather efficient algorithm; however,
its performance can be affected by the pivot that is selected. For example,
always selecting the last element in the list (or sublist) can make the algorithm easy
to write, but on a sorted list that will lead to an efficiency of O(n<sup>2</sup>)
(the worst case).

### Examples

The example below was taken from [Wikipedia's article about Quick sort][3].
The __bolded__ elements are the pivots. In this example, the last element in each list/sublist
was chosen to be the pivot, but that is not necesary. (See the section about performance above.)
Each row shows the comparison of an element to the pivot (steps 2-3).
The arrows convey splitting each list into sublists and then bringing them back together (steps
4-5).

![Quick sort example](https://upload.wikimedia.org/wikipedia/commons/a/af/Quicksort-diagram.svg)

[1]: https://robbell.io/2009/06/a-beginners-guide-to-big-o-notation
[2]: https://en.wikipedia.org/wiki/Big_O_notation
[3]: https://en.wikipedia.org/wiki/Quicksort
