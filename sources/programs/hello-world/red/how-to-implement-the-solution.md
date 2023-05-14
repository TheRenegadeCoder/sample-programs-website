Let's get right to our implementation of Hello World in Red.

Honestly, this is about the weirdest syntax I've ever seen, so I really
had to dig into the docs.

[According to Helpin'Red][1], the first line in our solution is the header,
and it's absolutely necessary for all scripts. The header is composed of two
parts: the `Red` keyword and the block..

Now, every script will have the `Red` keyword. As for the block, well, that
will vary per script. Honestly, the information in that block is largely
optional, but it can be used to declare script information such as a title,
a description, a version, and an author. In this case, I simply gave the
script a title.

In addition to arbitrary information, the first block can also be used to
import libraries. For example, we could have implemented Hello World in
Red as a GUI:

```red
Red [needs: 'view]

view [
  text "Hello, World!"
]
```

Here, we use the header block to import the graphics view library. Then,
we use that library to display a window containing "Hello, World!"

At any rate, the last line in our original implementation clearly prints
"Hello, World!" to the user. We've seen this plenty of times already so
no need to dig into it.

[1]: https://helpin.red/Helloworld-runandcompile.html
