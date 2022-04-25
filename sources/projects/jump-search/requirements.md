For the purposes of this project, we'll assume that the search space is a list of integers.
Specifically, we'll accept two inputs on the command line: the list of integers and the
integer to find:

```shell
./ python "jump search.py"
Enter array elements: 3 4 1 7
Sorting the array for better results!
Sorted array:
[1, 3, 4, 7]
Enter the element to be searched: 4
number 1 is at index 3
```

If successful, the script should return `true`. Otherwise, the script should return `false`.
If any user input errors occur, the script should output the following usage message:
