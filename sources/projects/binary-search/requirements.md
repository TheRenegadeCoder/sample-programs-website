For the purposes of this project, we'll assume that the search space is a list of integers.
Specifically, we'll accept two inputs on the command line: the list of integers and the
integer to find:

```shell
$ ./binary-search.lang "1, 4, 5, 11, 12" "4"
```

If successful, the script should return `true`. Otherwise, the script should return `false`. 
If any user input errors occur, the script should output the following usage message:
`Usage: please provide a list of sorted integers ("1, 4, 5, 11, 12") and the integer to find ("11")`.
