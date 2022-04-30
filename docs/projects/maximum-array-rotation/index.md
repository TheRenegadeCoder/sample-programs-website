---

title: Maximum Array Rotation
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Maximum Array Rotation page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

## Description

Given a list, L, of integers, we can compute the weighted sum, W, as followed:

```
W = L[0] * 0 + L[1] * 1 + ... + L[N - 1] * N - 1
```

In this case, N is the length of the list. As a result, if the list contained 5 items,
the last term in the list would be multiplied by 4.

Given that we can compute the weighted sum, the purpose of this project is to
find the maximum array rotation. In other words, if we were to rotate the list N 
times (note: rotation direction does not matter), what's the largest weighted sum 
we could get? Here's what that would look like with this list (2, 8, 3, 1):

1. `(2, 8, 3, 1) = (2 * 0) + (8 * 1) + (3 * 2) + (1 * 3) = 0 + 8 + 6 + 3 = 17`
2. `(1, 2, 8, 3) = (1 * 0) + (2 * 1) + (8 * 2) + (3 * 3) = 0 + 2 + 16 + 9 = 27`
3. `(3, 1, 2, 8) = (3 * 0) + (1 * 1) + (2 * 2) + (8 * 3) = 0 + 1 + 4 + 24 = 29`
4. `(8, 3, 1, 2) = (8 * 0) + (3 * 1) + (1 * 2) + (2 * 3) = 0 + 3 + 2 + 6 = 11`

Ultimately, we want to find the largest sum. That appears to happen during our
second rotation (i.e. line 3) where we get a weighted sum of 29. 


## Requirements

A Maximum Array Rotation program should function as follows:

```shell
$ ./maximum-array-rotation.lang "8, 3, 1, 2"
$ 29
```

In other words, the user should call the program on the command line with a string
of comma separeted integers. If done properly, the program should output the 
Maximum Array Rotation. See the following testing section for more specific requirements.


## Testing

| Description                  | Input                     | Output                                                         |
| ---------------------------- | ------------------------- | -------------------------------------------------------------- |
| No Input                     |                           | "Usage: please provide a list of integers (e.g. "8, 3, 1, 2")" |
| Empty Input                  | ""                        | "Usage: please provide a list of integers (e.g. "8, 3, 1, 2")" |
| Sample Input: No Rotation    | "3, 1, 2, 8"              | 29                                                             |
| Sample Input: One Rotation   | "1, 2, 8, 3"              | 29                                                             |
| Sample Input: Many Rotations | "8, 3, 1, 2"              | 29                                                             |


## Articles

- [Maximum Array Rotation in Python](https://sampleprograms.io/projects/maximum-array-rotation/python)