---
title: Fizz Buzz in Every Language
layout: default
date: 2018-11-01
last-modified: 2020-05-02
featured-image: fizz-buzz.png
tags: [fizz-buzz]
authors:
  - the_renegade_coder
---

In this article, we're tackling the Fizz Buzz problem, its requirements, and
how to test a solution.

## Description

Fizz Buzz is a typical interview question which tests the developers knowledge
of flow control and operators. The goal of the problem is to output the
numbers 1 through 100 but with special cases for various intervals--traditionally
3 (Fizz) and 5 (Buzz).

## Requirements

For the purposes of this repository, the following rules apply:

> Write a program that prints the numbers 1 to 100. However, for multiples of three,
> print "Fizz" instead of the number. Meanwhile, for multiples of five, print "Buzz"
> instead of the number. For numbers which are multiples of both three and five,
> print "FizzBuzz"

To be even more specific, please output each value on its own line. The output
should look something like:

```console
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

The program should then be saved in a file called fizz buzz using the proper
naming conventions of your choice language.

## Testing

Verify that the actual output matches the expected output. See the
[requirements][3] section for an example of the expected output.

## Articles

{% include article_list.md collection=site.categories.fizz-buzz %}

## Further Reading

- [Fizz Buzz in Every Language by The Renegade Coder][2]

[1]: ../assets/Fizz_Buzz.png
[2]: https://therenegadecoder.com/series/fizz-buzz-in-every-language/
[3]: #requirements
