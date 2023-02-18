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

[User-specified data types](https://openeuphoria.org/docs/lang_decl.html#_123_userdefinedtypes)
can be done based on these four data types. The way this is done is to declare a type
function that validates the input value. For example, if you wanted to define an
`hour` type that only allowed integers from 0 to 23, you would do this:

```euphoria
type hour(integer x)
    return x >= 0 and x <= 23
end type
```

Keywords in Euphoria are rather simple. For each type of keyword that does control flow or
declares a `function` or `procedure` (more on that later), there is a corresponding `end`
keyword that declares the end of that structure. For example:

```euphoria
if x = 42
then
    do_something_cool(x)
end if
```

Euphoria makes the distinction between functions and procedures. Functions returns
values, whereas procedures do not (think of it like a `void` function in C).
For example:

```euphoria
function foo(integer bar)
    return bar + 100
end function
```

The above function `foo` just returns the value of `bar` plus 100. Here's an example
of a procedure:

```euphoria
procedure baz(sequence s)
    fputs(1, s & '\n')
end procedure
```

The above procedure `baz` just outputs a string with a newline to standard out.

Parameter passing in Euphoria is rather unique. According to
[Wikipedia](https://en.wikipedia.org/wiki/Euphoria_(programming_language)#Parameter_passing):

> Arguments to routines are always passed by value; there is no pass-by-reference facility.
  Parameters are allowed to be modified locally (i.e., within the callee) which is implemented
  very efficiently as sequences have automatic copy-on-write semantics. In other words, when you
  pass a sequence to a routine, initially only a reference to it is passed, but at the point the
  routine modifies this sequence parameter the sequence is copied and the routine updates only a
  copy of the original.

If you'd like more information about this language, please see the
[OpenEuphoria manual](https://openeuphoria.org/docs/index.html).
