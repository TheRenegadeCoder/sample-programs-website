---
authors:
- Jeremy Grifski
- rzuckerm
- Vee Ng
- "\u0218tefan-Iulian Alecu"
date: 2019-04-05
featured-image: file-input-output-in-every-language.jpg
last-modified: 2026-04-11
layout: default
tags:
- file-input-output
- scala
title: File Input Output in Scala
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/scala/how-to-implement-the-solution.md
- sources/programs/file-input-output/scala/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Scala](https://sampleprograms.io/languages/scala) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```scala
import java.nio.charset.StandardCharsets
import java.nio.file.{Files, Path, Paths}
import scala.jdk.CollectionConverters.*
import scala.util.Try

extension (p: Path)
  def readLines: Try[List[String]] =
    Try(Files.readAllLines(p, StandardCharsets.UTF_8).asScala.toList)

  def writeString(content: String): Try[Unit] =
    Try(Files.writeString(p, content, StandardCharsets.UTF_8)).map(_ => ())

object FileInputOutput:
  private val path = Paths.get("output.txt")
  private val content =
    """I am a string.
      |I am also a string.
      |Scala is fun!""".stripMargin

  def main(args: Array[String]): Unit =
    val program =
      for
        _ <- path.writeString(content)
        lines <- path.readLines
      yield lines

    program.fold(
      err => System.err.println(s"File operation failed: ${err.getMessage}"),
      res => res.foreach(println)
    )
```

{% endraw %}

File Input Output in [Scala](https://sampleprograms.io/languages/scala) was written by:

- rzuckerm
- Ștefan-Iulian Alecu

This article was written by:

- Jeremy Grifski
- rzuckerm
- Vee Ng

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Apr 11 2026 13:25:12. The solution was first committed on May 15 2023 16:11:44. The documentation was last updated on May 15 2023 15:51:23. As a result, documentation below may be outdated.

## How to Implement the Solution

First of all let's look at the read / write functions as a whole, and their usages.

### Read from a file

In many real world scenario, your program usually takes one of the two approaches when dealing with undeterministic I/O
(also called side-effects): fail loudly or fail silently.

We want to fail loudly, i.e. throw exception, stop execution flow or output error as results, when the I/O is critical
for the program to proceed.

```scala
  // reading file then write to stdout
  // write exception when fail
  def readFromFile(filename: String) {
    try {
      val buffer = Source.fromFile(filename)
      val lines = buffer.getLines

      lines.foreach(println)
      buffer.close
    } catch {
      case e: FileNotFoundException => println(s"File ${filename} does not exist.")
      case e: IOException => println(s"I/O Exception when reading from ${filename}.")
      case e: Throwable => println(s"Error ${e.getMessage} when reading from ${filename}.")
    }
  }
```

Similar to many other language, `scala.io.Source` provides the ability to get a file into a buffer-like instance,
in our case `BufferedSource`, using `fromFile`. `Source` is built-in with `Java` exceptions to let us know what
causes the failure in opening / reading the file.

Since we are dealing with a text file, we can simply use `getLines` to convert `BufferedSource` to a `Iterator[String]`.
We can also convert `Iterator[String]` to a `List[String]` or `Array[String]` using `.toList` and `.toArray`
respectively.

`Iterator` interface allows us to traverse each line, using `foreach`. The syntactic sugar `lines.foreach(println)`
you see here is short-hand for:

```scala
lines.foreach(line => println(line))
```

or

```scala
for (line <- lines) {
  println(line)
}
```

After extracting the buffer, we close it with `buffer.close`.

`catch` block here demonstrate Scala's pattern matching feature. By default, all exceptions can be caught
as a `Throwable`.
However we have the option to deal with specific exception (`FileNotFoundException` or `IOException`) separately.

Usage is simple:

```scala
readFromFile("output.txt")
```

### Write to a file

Similar pattern for writing to files. Unlike read, which is usually at the beginning of some logic and having
the input type determined gains us benefits, write is usually a void function with no return types, and called
at the end of execution (result, log, etc.).

```scala
// write to file
// stdout exception when fail
def writeToFile(filename: String, contents: String) {
  try {
    val writer = new PrintWriter(new File(filename))
    writer.write(contents)
    writer.close
  } catch {
    case e: FileNotFoundException => println(s"Cannot write into file ${filename}.")
    case e: Throwable => println(s"Error ${e.getMessage} when writing to file ${filename}.")
  }
}

Usage is straightforward, simply call the function:

```scala
writeToFile("output.txt", "I am a string.\nI am also a string.\nScala is fun!\n")
```


## How to Run the Solution

The source requires standard scala compiler and runtime: `scalac` and `scala`. Before running the program, make sure
the files are in the same directory as the compiled `.class`.

```console
$ scalac FileInputOutput.scala
$ scala FileInputOutput
```
