---
title: Hello World in C++
layout: default
last-modified: 2020-05-02
featured-image: hello-world-in-c-plus-plus.jpg
tags: [c-plus-plus, hello-world]
authors:
  - the_renegade_coder

---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>
using namespace std;

int main()
{
    cout << "Hello, World!";
    return 0;
}
```

{% endraw %}

[Hello World](https://sampleprograms.io/projects/hello-world) in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Jeremy Griffith
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 10 2022 16:05:09. The solution was first committed on Mar 21 2018 00:11:57. As a result, documentation below may be outdated.

## How to Implement the Solution

Even though C++ was built on C, the implementation of Hello World in 
C++ is slightly different.

It appears this implementation of Hello World may be competing with 
Java for hardest to learn. But at any rate, let's break it down.

Once again, the first line is an `include` statement. Here, we're including 
the IO stream code in our solution. This is how we gain access to the 
IO objects like `cout`.

Next, we gain access to the `std` namespace which basically allows us to 
shorten `std::cout` to `cout`. It's really just a style thing that eliminates 
a lot of verbosity that you might get with other languages like Java. 
Of course, if another namespace also has a `cout`, we'll run into problems.

After that, we make a `main` method as usual. This is exactly the same as 
C, so I won't bother explaining the return type bit again.

Finally, we write our string to the `cout` stream. The syntax is a bit 
strange, but basically we can imagine that the Hello World string is 
inserted into the `cout` stream. In fact, the double-arrow operator is 
the insertion operator, and it has some fun properties. For instance, 
the operator can be chained together, but that's a topic for another time.


## How to Run the Solution

Perhaps the easiest way to run the solution is to leverage the [online gdb compiler][1].

Alternatively, you can try to run the C++ code in a similar way described 
in the last article. Honestly, it's pretty easy to write and run C/C++ code 
on most platforms:

```console
gcc -o hello-world hello-world.cpp
./hello-world
```

Unfortunately, Windows pretty much requires the use of Visual Studio. So, 
instead of sharing platform specific directions, I'll fallback on my online 
compiler recommendation.

[1]: https://www.onlinegdb.com/online_c++_compiler
