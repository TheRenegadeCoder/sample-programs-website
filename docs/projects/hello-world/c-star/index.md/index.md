---

title: Hello World in C*
layout: default
last-modified: 2020-05-02
featured-image: hello-world-in-c-star-featured-image.JPEG
tags: [c-star, hello-world]
authors:
  - the_renegade_coder

---

Welcome to the Hello World in C\* page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```C\*
#include <stdio.h>
main ()
{
	printf ("Hello, World!")
}

```

## How to Implement the Solution

At long last, here�s Hello World in C*:

```cstar
#include <stdio.h>
main ()
{
    printf("Hello, World!")
}
```

As we can see, Hello World in C* looks alarmingly similar to C. That said, C*
is a superset of C, so this shouldn�t be too much of a surprise. At any rate,
let�s dig in.

Up first, we have the include statement which pulls in the stdio header. With
the standard IO header included, we�re able to write to standard output using
printf.

Next, we have our usual main function declaration which serves as the drop in
function for our program. We should be used to seeing this convention since it�s
common in the popular industrial languages like C++ and Java.

Finally, we make a call to printf which is a special print function that allows
for string formatting. Of course, all we�re going to pass to it is the �Hello,
World!� string. And, that�s it!


## How to Run the Solution

Unfortunately, I haven�t found a way to execute C* programs. That said, I did
find a handful of open-source C* compilers, so maybe those can help us out:

- <https://github.com/KayvanMazaheri/c-star-compiler>
- <https://github.com/renjithgr/cstar-compiler-Java>

In addition, the [user guide][1] does detail how to compile and run C* programs. But,
again, that information isn�t super helpful without the compiler.

If you know of an official compiler, let me know in the comments.
