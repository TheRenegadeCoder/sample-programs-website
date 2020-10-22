---
title: List/Array rotation in Python
layout: default
date: 2020-10-14
last-modified: 2020-10-14
featured-image: {FEATURED IMAGE NAME}
tags: [array-rotation]
authors:
  - agasheaditya
---

## Print/return maximum sum of weighted rotated array/list of size 'n' after 'n' rotations.
## Description

##### weight distribution array (a[0]* 0,a[1]* 1,a[2]* 2,a[3]* 3,...,a[n]*n)
 > array after 1st rotation ->[2, 8, 3, 1]
                                            0
                                            8
                                            6
                                            3
-----------------------------------------------
 > array after 2nd rotation ->[1, 2, 8, 3]
                                            0
                                            2
                                            16
                                            9
------------------------------------------------
 > array after 3rd rotation ->[3, 1, 2, 8]
                                            0
                                            1
                                            4
                                            24
------------------------------------------------
 > array after 4th rotation ->[8, 3, 1, 2]
                                            0
                                            3
                                            2
                                            6
------------------------------------------------

## Requirements

##### Python 3.* 

```shell
./sample-program.lang sample_input
```

## Testing

| Description | {EXAMPLE INPUT COLUMN} | Output             |
| ----------- | ---------------------- | ------------------ |
| List/ Array |    input =[8,3,1,2]    | Maximum Sum is:29  |
| List/ Array |  input = [15,18,20,70] | Maximum Sum is: 268|
| List/ Array |ip= [24,4,7,-8,6,77,14] | Maximum Sum is: 531|

## Articles

{% include article_list.md collection=site.categories.Array-rotation %}

## Further Reading

- > https://docs.python.org/3/tutorial/datastructures.html
