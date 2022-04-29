---

title: Hello World in Goby
layout: default
last-modified: 2020-05-02
featured-image: hello-world-in-goby-featured-image.JPEG
tags: [goby, hello-world]
authors:
  - the_renegade_coder

---

Welcome to the Hello World in Goby page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Goby
puts("Hello, World!")

```

{% endraw %}

## How to Implement the Solution

As seen many times in this collection, Hello World in Goby is actually
really simple. In total, it's one line of code which looks a lot like
Ruby:

```goby
puts("Hello, World!")
```

Alternatively, we can leave out the parentheses:

```goby
puts "Hello, World!"
```

Naturally, `puts` writes the "Hello, World!" string to the user, and that's it!



## How to Run the Solution

To run this solution, we can take advantage of the samplerunner script
included in the [Sample Programs repo][2]. If our system is setup
correctly, the following command should get the job done:

```shell
./samplerunner.sh run -s hello-world.gb
```

Alternatively, we may want to get a copy of the Goby interpreter. [According
to the documentation][1], there are a few ways to do that, but we won't 
dig into that now.

Unlike many other languages in this collection, Goby does not have an online 
interpreter at this time.
