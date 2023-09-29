---
authors:
- Faiz Nurullah
date: 2023-29-09
featured-image: data-type-transformation.png
last-modified: 2023-29-09
layout: default
tags:
- python
- data-type-transformation
title: Data Type Transformation
---

In programming, we often need to change (transform) data types from one form to another. This can be an important step in data processing. In Python, there are various ways to perform data type transformations. Let's explain some of them.

## Data Type Conversion (Type Casting)

  ### Converting String to Integer or Float

  ```python

    string_number = "123"
    number_integer = int(string_number) 
    number_float = float(string_number)  

  ```

  ### Converting Integer or Float to String

 ```python

   number = 123
   string_number = str(number) 

  ```

  ### Converting List to String

 ```python

  my_list = [1, 2, 3, 4, 5]
  string_list = ', '.join(map(str, my_list)) 

  ```

## Cutting (Slicing) and Retrieving Substrings

You can extract a portion of the string by using the slicing operator. For example, to retrieve the second through fifth characters of a string:

 ```python

  my_string = "Hello, World!"
  substring = my_string[1:5]

  ```

## Using the format() function for formatting

The format() function is used to combine variables into strings with different data types.

 ```python

 name = "John"
 age = 30
 messege = "Hello, My name is {} and I {} Year Old.".format(name, age)

  ```

These are some common ways to perform data type transformations in the Python programming language. It is important to understand how to change data types correctly to ensure that your data meets your needs in programming.