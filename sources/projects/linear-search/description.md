Linear search is quite intuitive, it is basically searching an element in an array by traversing 
the array from the beginning to the end and comparing each item in the array with the key. If a 
particular array entry matches with the key the position is recorded and the loop is stopped. 
The algorithm for this is:

1. Define a flag (set it's value to 0) for checking if key is present in array or notation.
2. Iterate through every element in array.
3. In each iteration compare the key and the current element.
4. If they match set the flag to 1, position to the current iteration and break from the loop.
5. If entire loop is traversed and the element is not found the value of flag will be 0 and user 
can notified that key is not in array.

### Performance

The performance of searching algorithms is generally defined in "Big O notation".
If you are not familiar with such notations, please refer to the relevant
article by [Rob Bell][1] or the [Wikipedia][2] entry listed in further readings below.

| Cases        | Big O Notatation |
| ------------ | ---------------- |
| Best case    | O(1)             |
| Average case | O(n)             |
| Worst case   | O(n)             |

Linear search is not efficient for large arrays, but for relatively smaller arrays it works fine.

### Example: key=3, array=[1, 2, 3, 4, 5]

<b>Iteration 1</b>
<br>array[i] = array[0] = 1
<br>key = 3
<br>key != array[i]

<b>Iteration 2</b>
<br>array[i] = array[1] = 2
<br>key = 3
<br>key != array[i]

<b>Iteration 3</b>
<br>array[i] = array[2] = 3
<br>key = 3
<br>key = array[i]
<br>break
<br>flag = 1
<br>pos = 2

[1]: https://robbell.io/2009/06/a-beginners-guide-to-big-o-notation
[2]: https://en.wikipedia.org/wiki/Big_O_notation
