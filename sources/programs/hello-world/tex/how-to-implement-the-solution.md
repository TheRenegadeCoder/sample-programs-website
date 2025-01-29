Let's dive right into Hello World in Tex.

It is much simpler in Tex due to the fact the Tex is a markup language.

```tex
\newwrite\out
\immediate\openout\out=hello-world.txt
```

This first two lines create an output file called `hello-world.txt`.

```tex
\immediate\write\out{Hello, World!}
```

This writes `Hello, World!` to the output file.

```tex
\end
```

Finally, this is saying the document has ended by declaring (`\`) an `end`.
