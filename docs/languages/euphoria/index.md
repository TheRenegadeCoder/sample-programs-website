---

title: The Euphoria Programming Language
layout: default
date: 2023-02-12
last-modified: 2023-02-12
featured-image: 
tags: [euphoria]
authors:
  - rzuckerm

---

Welcome to the Euphoria page! Here, you'll find a description of the language as well as a list of sample programs in that language.

## Description

[According to OpenEuphoria](https://openeuphoria.org/), Euphoria is an imperative
interpretive programming language has the following features:

* A flexible memory manager unit that is capable of dynamically growing and shrinking
  memory usage
* A high-performance interpreter that is supposed to be faster the other interpretive
  languages like Python and Perl
* It is capable of being compiled to improve performance via a 
  [Euphoria to C Translator](https://openeuphoria.org/docs/e2c.html#_606_euphoriatoctranslator)
* It has run-time checking for out-of-bounds subscripts, bad passed parameters for
  library routines, and a full English description of the run-time issues, providing
  a full call-stack-trace and variable values
* It is hardware independent from word lengths and endianness
* It provide a full source-level debugging
* It has a built-in code editor
* It runs on a number of platforms like Windows, various Linux flavors, and MacOS
* It is not an object oriented language, so it has no concept of classes
* Simple data types

There are only four different data types:

* `object` - Base data type
* `atom` - A 31-bit signed integer or 64-bit floating point number depending upon the
  value stored
* `integer` - A 31-bit in signed integer
* `sequence` - A list of values. This list can be comprised of `atom`s or other
  `sequence`s

According to [Wikipedia](https://en.wikipedia.org/wiki/Euphoria_(programming_language)),
there is no actual `string` data type. Instead a `string` is just a `sequence`
of `atom`s. For example:
```
"ABC"
```

is actually this:
```
{65, 66, 67}
```

Also according to [Wikipedia](https://en.wikipedia.org/wiki/Euphoria_(programming_language)#Parameter_passing)):

> Arguments to routines are always passed by value; there is no pass-by-reference facility.
  Parameters are allowed to be modified locally (i.e., within the callee) which is implemented
  very efficiently as sequences have automatic copy-on-write semantics. In other words, when you
  pass a sequence to a routine, initially only a reference to it is passed, but at the point the
  routine modifies this sequence parameter the sequence is copied and the routine updates only a
  copy of the original.


## Articles

- [Hello World in Euphoria](https://sampleprograms.io/projects/hello-world/euphoria)